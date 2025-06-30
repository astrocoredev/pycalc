class Node:
    __match_args__ = ("op", "left", "right", "num")

    def __init__(self, op = None, left = None, right = None, num = None):
        self.op = op
        self.left = left
        self.right = right
        self.num = num

    def __str__(self):
        return f"op: ({self.op}) left: ({self.left}), right: ({self.right})"

    def eval(self):
        match self:
            case Node( None, None, None, num ): 
                return num
            case Node( op, left, right, None ):
                l = left.eval()
                r = right.eval()
                match op:
                    case '+': return l + r
                    case '-': return l - r
                    case '*': return l * r
                    case '/': return l / r

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.tokens):
            raise StopIteration
        value = self.tokens[self.index]
        self.index += 1
        return value
    
    def peek(self):
        if self.index >= len(self.tokens):
            return None
        return self.tokens[self.index]
    
    def parse_add(self):
        node = self.parse_mult()
        while token := self.peek():
            match token:
                case '+' | '-':
                    op = next(self, None)
                    right = self.parse_mult()
                    node = Node(op, node, right, None)
                case _:
                    break
        return node

    
    def parse_mult(self):
        node = self.parse_num()
        while token := self.peek():
            match token:
                case '*' | '/':
                    op = next(self, None)
                    right = self.parse_num()
                    node = Node(op, node, right, None)
                case _:
                    break
        return node
    
    def parse_num(self):
        return Node(num = int(next(self, None)))
