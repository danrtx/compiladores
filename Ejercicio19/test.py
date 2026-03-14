import sys
from antlr4 import *
from MiniLexer import MiniLexer
from MiniParser import MiniParser

def main():
    input_code = "x = 5 y = 10 print x print y" 
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = MiniLexer(input_stream)
    lexer.removeErrorListeners()
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>" else "LITERAL"
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = MiniParser(stream)
    parser.removeErrorListeners()
    tree = parser.prog() 
    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()