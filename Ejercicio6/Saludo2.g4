grammar Saludo2;
saludo: saludoTipo NOMBRE ;
saludoTipo: HOLA | BUENOSDIAS ;
HOLA: 'hola' ;
BUENOSDIAS: 'buenosdias' ;
NOMBRE: [A-Z][a-z]+ ;
WS: [ \t\r\n]+ -> skip ;