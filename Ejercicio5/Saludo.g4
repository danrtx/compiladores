grammar Saludo;
saludo: HOLA NOMBRE ;
HOLA: 'hola' ;
NOMBRE: [A-Z][a-z]+ ;
WS: [ \t\r\n]+ -> skip ;