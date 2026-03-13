import sys
from antlr4 import *
from OperadoresLexer import OperadoresLexer
from OperadoresParser import OperadoresParser

def main():
    input_code = "+"  # Probando el operador suma
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = OperadoresLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>" else "LITERAL"
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = OperadoresParser(stream)
    tree = parser.op()

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()