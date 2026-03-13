import sys
from antlr4 import *
from IdentificadorLexer import IdentificadorLexer
from IdentificadorParser import IdentificadorParser

def main():
    input_code = "valor1"  
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = IdentificadorLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "LITERAL"
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = IdentificadorParser(stream)
    
    tree = parser.id_() 

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()