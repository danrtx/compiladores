grammar ExprVar;
expr: expr MAS expr | ID | NUM ;

MAS: '+' ;
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;