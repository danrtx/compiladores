import sys
from antlr4 import *
from Saludo2Lexer import Saludo2Lexer
from Saludo2Parser import Saludo2Parser

def main():
    input_code = "buenosdias Pedro"
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = Saludo2Lexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>":
                token_name = lexer.symbolicNames[token.type]
            elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]
            else:
                token_name = "LITERAL"
            print(f"Texto: {token.text:12} | Tipo: {token_name}")

    parser = Saludo2Parser(stream)
    tree = parser.saludo()

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()