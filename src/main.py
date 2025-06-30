from tokeniser import Tokeniser
from parser import Parser

def main():
    tokens = Tokeniser("21 + 3 * 43")
    tokens = tokens.tokenise()
    parser = Parser(tokens)
    parsed = parser.parse_add()
    print(parsed.eval())


if __name__ == "__main__":
    main()
