kSpecialChar = "-"

inputString = input("Ingrese la cadena a comprimir: ")
print(inputString)

if "-" in inputString:
    raise ValueError("Ingresaste el caracter especial reservado '-'")
if len(inputString) == 0:
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
        print(repetitions, savedChar)
        if savedChar.isnumeric():
            savedChar = "{separator}{character}{separator}".format(
                character=savedChar, separator=kSpecialChar)
        compressedString += "{character}{repetitions}".format(
            character=savedChar, repetitions=repetitions)
        repetitions = 1

    if (isDifferentChar and isLastChar):
        print(repetitions, char)
        if char.isnumeric():
            char = "{separator}{character}{separator}".format(
                character=char, separator=kSpecialChar)
        compressedString += "{character}{repetitions}".format(
            character=char, repetitions=repetitions)
    savedChar = char

print(len(compressedString), len(inputString))
result = compressedString if len(
    compressedString) < len(inputString) else inputString

print(result)
