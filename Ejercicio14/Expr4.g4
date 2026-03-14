grammar Expr4;

expr: term ( (MAS|MENOS) term )* ;
term: factor ( (MUL|DIV) factor )* ;
factor: NUM | LPAREN expr RPAREN ;

MAS: '+' ;
MENOS: '-' ;
MUL: '*' ;
DIV: '/' ;
LPAREN: '(' ;
RPAREN: ')' ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;