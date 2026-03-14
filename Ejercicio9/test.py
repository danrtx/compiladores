import sys
from antlr4 import *
from SumaLexer import SumaLexer
from SumaParser import SumaParser

def main():
    input_code = "3+4" # Prueba de suma simple
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = SumaLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>" else "LITERAL"
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = SumaParser(stream)
    tree = parser.expr()

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()