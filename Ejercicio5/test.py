import sys
from antlr4 import *
from SaludoLexer import SaludoLexer
from SaludoParser import SaludoParser

def main():
    input_code = "hola Juan"
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = SaludoLexer(input_stream)
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
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = SaludoParser(stream)
    tree = parser.saludo()

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()