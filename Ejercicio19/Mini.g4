grammar Mini;
prog: stat+ ;
stat: ID IGUAL expr | PRINT expr ;
expr: expr MAS expr | NUM | ID ;

IGUAL: '=' ;
PRINT: 'print' ;
MAS: '+' ;
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;