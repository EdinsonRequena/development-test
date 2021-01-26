# singles test for developers

1) Clona el repositorio.

2) Crea una nueva rama con tu nombre de usuario.

3) Crea 2 carpetas, en una estaran las soluciones en python y en otra las soluciones en Javascritpt.

4) Una vez terminado los ejercicios haz un pull request a este mismo repositorio.

## Ejercicio de prueba 1

Escribe una función que retorne la cadena "¡Hola, mundo!"; ésta deberá requerir 2 parámetros tipo cadena,
“Hola” y “Mundo”.

## Ejercicio de prueba 2

Deberás convertir un número en una cadena que contenga sonidos de gotas de agua correspondientes a
ciertos factores potenciales. Un factor es un número que se divide uniformemente en otro número, sin dejar
resto.
Las reglas de las gotas son para números determinados:

Si tiene 3 como factor, agregue 'Plic' al resultado.

Si tiene 5 como factor, agregue ‘Plac’ al resultado.

Si tiene 7 como factor, agregue ‘Ploc’ al resultado.

Si no tiene 3, 5 o 7 como factor, el resultado deben el numero como cadena de texto(string) y no como entero(int)


Ejemplos:

28 tiene 7 como factor, pero no 3 o 5, por lo que el resultado sería "Ploc’".

30 tiene 3 y 5 como factores, pero no 7, por lo que el resultado sería "PlicPlac".

34 no se factoriza por 3, 5 o 7, por lo que el resultado sería "34".


## Ejercicio de prueba 3

Dado un array de enteros, retorna la suma de los elemmentos del array

Tu codigo debera funcionar para estos 3 casos de prueba que se presentaran a continuacion:

### Caso de prueba 1

Input: nums = [1,2,3,4]

Output: [1,3,6,10]

Explicacion: Corriendo tu codigo el mismo debera sumar los enteros del array de la siguente manera: [1, 1+2, 1+2+3, 1+2+3+4]

### Caso de prueba 2

Input: nums = [1,1,1,1,1]

Output: [1,2,3,4,5]

Explanation: Corriendo tu codigo el mismo debera sumar los enteros del array de la siguente manera: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

### Caso de prueba 3

Input: nums = [3,1,2,10,1]

Output: [3,4,6,16,17]

---
En esta prueba tecnica tambien se evaluara tus conocimientos de git y github asi que es importante que realices 4 primeros pasos. Se evaluara tambien tu estilo de codigo y tu manera de solucinar los problemas.
En la medida de lo posible intenta utilizar operadores ternarios y arrow functions.

Que la fuerza te acompañe!!!
