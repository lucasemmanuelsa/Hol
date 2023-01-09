def encripty(key, text):

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    

    #i = 0
    #while i < 26:
    output = ''
    for character in text:
        if(character.isalpha() == False):
            output += character
        else:
            if(character.upper() == character):
                output += alpha[((alpha.index(character.upper()) + key) % 26)]
            else:
                output += alpha[((alpha.index(character.upper()) + key) % 26)].lower()
            
    #i += 1
    return output

print(encripty(23,input("Text: ")))
