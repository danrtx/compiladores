grammar Calc;
prog: stat+ ;
stat: ID IGUAL expr | PRINT expr ;
expr: term ( (MAS|MENOS) term )* ;
term: factor ( (MUL|DIV) factor )* ;
factor: NUM | ID | LPAREN expr RPAREN ;

IGUAL: '=' ;
PRINT: 'print' ;
MAS: '+' ;
MENOS: '-' ;
MUL: '*' ;
DIV: '/' ;
LPAREN: '(' ;
RPAREN: ')' ;
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;