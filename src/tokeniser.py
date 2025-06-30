class Tokeniser:

    def __init__(self, string):
        self.data = [i for i in string]
        self.index = 0
        self.tokens = list()

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
    
    def peek(self):
        if self.index >= len(self.data):
            return None
        return self.data[self.index]
    
    def next_if(self, fn):
        if fn(self.peek()):
            return next(self, None)
        
    
    def tokenise(self):

        while token := next(self, None):
            match token:
                case ch if ch.isspace(): continue
                case '+' | '-' | '*' | '/': self.tokens.append(token)
                case ch if ch.isdigit():
                    while num := self.next_if(lambda x: x and x.isdigit()):
                        ch += num
                    self.tokens.append(int(ch))
                case _: raise Exception("L")

        return self.tokens