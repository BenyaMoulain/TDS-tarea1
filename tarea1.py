import logging

logging.basicConfig(level=logging.DEBUG, filename="debug.log")
logging.getLogger().addHandler(logging.StreamHandler())
logging.info("Inicio del programa")

kSpecialChar = "-"


inputString = input("Ingrese la cadena a comprimir: ")
logging.info("Cadena ingresada: {string}".format(string=inputString))

if "-" in inputString:
    logging.error("La cadena ingresada contiene un \"-\".")
    raise ValueError("Ingresaste el caracter especial reservado '-'.")
if len(inputString) == 0:
    logging.error("Se ingresó una cadena vacía.")
    raise ValueError("Ingresaste una cadena vacía")

compressedString = ""
savedChar = ""
repetitions = 1

for charIndex in range(len(inputString)):
    char = inputString[charIndex]

    isNotFirstChar = True if savedChar != "" else False
    isLastChar = True if charIndex+1 == len(inputString) else False
    isDifferentChar = True if char != savedChar else False

    if not isDifferentChar:
        repetitions += 1

    if isNotFirstChar and (isDifferentChar or isLastChar):
        logging.info("Se encontraron {repetitions} repeticiones del caracter '{character}'.'.".format(
            repetitions=repetitions, character=savedChar))
        if savedChar.isnumeric():
            savedChar = "{separator}{character}{separator}".format(
                character=savedChar, separator=kSpecialChar)
        compressedString += "{character}{repetitions}".format(
            character=savedChar, repetitions=repetitions)
        repetitions = 1

    if (isDifferentChar and isLastChar):
        logging.info("Se encontraron {repetitions} repeticiones del caracter '{character}'.'.".format(
            repetitions=repetitions, character=char))
        if char.isnumeric():
            char = "{separator}{character}{separator}".format(
                character=char, separator=kSpecialChar)
        compressedString += "{character}{repetitions}".format(
            character=char, repetitions=repetitions)
    savedChar = char

logging.info("El largo de la cadena original es: {len}.".format(
    len=len(inputString)))
logging.info("El largo de la cadena comprimida es: {len}.".format(
    len=len(compressedString)))
result = compressedString if len(
    compressedString) < len(inputString) else inputString
logging.info("La cadena devuelta es: {string}.".format(string=result))

logging.info("Fin del programa.\n")
