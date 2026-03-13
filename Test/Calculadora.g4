grammar Calculadora;

// --- REGLAS SINTÁCTICAS (PARSER) ---
// Punto de entrada del mini lenguaje
prog:   stat+ ;

// Las sentencias pueden ser expresiones o asignaciones
stat:   expr NEWLINE            # printExpr
    |   ID '=' expr NEWLINE     # assign
    |   NEWLINE                 # blank
    ;

// Jerarquía de operaciones (Manejo de precedencia)
expr:   expr ('*'|'/') expr     # MulDiv
    |   expr ('+'|'-') expr     # AddSub
    |   INT                     # int
    |   ID                      # id
    |   '(' expr ')'            # parens
    ;

// --- REGLAS LÉXICAS (LEXER) ---
// Palabras clave y Operadores
MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
EQ  : '=' ;

// Reconocimiento de números e identificadores
ID  : [a-zA-Z]+ ;      // Letras mayúsculas y minúsculas
INT : [0-9]+ ;         // Números enteros

// Ignorar espacios en blanco y manejar saltos de línea
NEWLINE : '\r'? '\n' ;
WS  : [ \t]+ -> skip ;