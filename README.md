# TDS-tarea1

## Descripción del programa

Este programa solicita al usuario que ingrese una cadena de texto y la comprime según sus repiticiones, si la cadena original es de menor largo que la comprimida, se devuelve la original.
En caso de que se encuentren números, al comprimirse será agregado el caracter reservado "-" entre los números.
Los logs del programa son guardados en el archivo debug.log

## Tecnologías usadas

Python 3.9.1

## Instrucciones para iniciar programa

Ejecutar en la raiz del proyecto:

```bash
python tarea1.py
```

## Ejemplos de uso

- Entrada: aabcccccaaa, Salida: a2b1c5a3
- Entrada: aabcccccaaa1111, Salida: a2b1c5a3-1-4
- Entrada: aabc, salida: aabc
