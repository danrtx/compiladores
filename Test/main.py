import sys
from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser

def main():
    input_code = """
    a = 10
    b = 20
    a + b * 2
    """
    
    print("--- CÓDIGO DE ENTRADA ---")
    print(input_code.strip())
    print("\n-------------------------")

    input_stream = InputStream(input_code + "\n")
    lexer = CalculadoraLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("--- TOKENS RECONOCIDOS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>":
                token_name = lexer.symbolicNames[token.type]
            elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]
            else:
                token_name = f"LITERAL '{token.text.strip()}'"
            
            display_text = token.text.replace('\n', '\\n').replace('\r', '\\r')
            print(f"Token: {display_text:8} | Tipo: {token_name}")
            
    print("\n-------------------------")

    parser = CalculadoraParser(stream)
    tree = parser.prog()

    print("--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()