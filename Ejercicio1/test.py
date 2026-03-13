import sys
from antlr4 import *
from NumerosLexer import NumerosLexer
from NumerosParser import NumerosParser

def main():
    # Entrada de prueba sugerida por el ejercicio
    input_code = "31f32A434"
    print(f"--- ENTRADA ---\n{input_code}\n---------------")

    input_stream = InputStream(input_code)
    lexer = NumerosLexer(input_stream)
    stream = CommonTokenStream(lexer)

    print("--- TOKENS ---")
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            # Búsqueda segura del nombre del token
            if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] != "<INVALID>":
                token_name = lexer.symbolicNames[token.type]
            elif token.type < len(lexer.literalNames) and lexer.literalNames[token.type] != "<INVALID>":
                token_name = lexer.literalNames[token.type]
            else:
                token_name = "LITERAL"
            print(f"Texto: {token.text:8} | Tipo: {token_name}")

    parser = NumerosParser(stream)
    tree = parser.numero() # OJO: Aquí llamamos a la regla inicial de esta gramática

    print("\n--- ÁRBOL SINTÁCTICO ---")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()