import string

class UserInteraction:
    def __init__(self):
        pass

    def generateSearchTerm(self):
        userInput = input("tema a buscar: ")
        capsInput = string.capwords(userInput)
        wordsList = capsInput.split()
        searchTerm = "_".join(wordsList)
        print(f"el tema que quieres buscar es: {userInput} ")
        return searchTerm

    def saveFile(self):
        userFileName = input("Escoger un nombre para tu archivo: ")
        filenameSplit = userFileName.split()
        filename = "_".join(filenameSplit)
        userFileExtension = input("Por favor, escoger la extension: 'pdf' o 'txt'")
        print(f"el nombre de tu archivo es: {filename}.{userFileExtension}")
        return filename,userFileExtension


    def translator(self):
        translatorResponse = input("¿Desea traducir el tema al inglés? (Y / N): ").lower()
        if translatorResponse not in ['y', 'n']:
            print("Por favor, responde 'y' o 'n'.")
        return translatorResponse
