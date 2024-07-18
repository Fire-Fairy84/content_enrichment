import string
import webbrowser


def generateSearchTerm():
    userInput = input("tema a buscar: ")
    capsInput = string.capwords(userInput)
    wordsList = capsInput.split()
    searchTerm = "_".join(wordsList)
    print(f"el tema que quieres buscar es: {userInput} ")
    return searchTerm

def saveFile():
    userFileName = input("Escoger un nombre para tu archivo: ")
    filenameSplit = userFileName.split()
    filename = "_".join(filenameSplit)
    userFileExtension = input("Por favor, escoger la extension: 'pdf' o 'txt'")
    print(f"el nombre de tu archivo es: {filename}.{userFileExtension}")
    return filename,userFileExtension


def translator():
    translator = input("desea traductir el tema a castellano")
    userText = input("Escribe el texto que quieres traducir: ")
    targetLanguage = input("Por favor, elige el idioma de destino (por ejemplo, 'es' para español, 'en' para inglés): ")
    translated = translator.translate(userText, dest=targetLanguage)
    print(f"Texto traducido: {translated.text}")
    return translated.text, targetLanguage


print(generateSearchTerm())
print(saveFile())
print(translator())


"""
            print("Traducir esto al inglés? (sí/no)")
            translate = get_user_input("> ")
            if translate.lower() not in ['sí', 'no']:
                print("Por favor, responde 'sí' o 'no'.")
                continue

            print("¿Te ha sido útil la información? (sí/no)")
            useful = get_user_input("> ")
            if useful.lower() not in ['sí', 'no']:
                print("Por favor, responde 'sí' o 'no'.")
                continue
"""