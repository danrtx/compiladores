grammar InstruccionPrint;
stat: PRINT expr ;
expr: NUM | ID ;

PRINT: 'print' ;
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;