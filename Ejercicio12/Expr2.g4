grammar Expr2;
expr: expr MAS expr    
    | expr MUL expr    
    | NUM    
    ;

MAS: '+' ;
MUL: '*' ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;