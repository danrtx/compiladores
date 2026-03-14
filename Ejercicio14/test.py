import sys
from antlr4 import *
from Expr4Lexer import Expr4Lexer
from Expr4Parser import Expr4Parser

def main():
    input_code = "(3+4)*5" 
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = Expr4Lexer(input_stream)
    lexer.removeErrorListeners() 
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>" else "LITERAL"
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = Expr4Parser(stream)
    parser.removeErrorListeners() 
    tree = parser.expr()

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()