#range of UNICODE integer IDs for lowercase latin
rangeLowercase = range(97, 123)

#exception class for shiftNumber length exceeding int length
class LengthError (Exception):
    pass

#exception class for finishing main loop
class FinishException (Exception):
    pass

#index for keyword looping
keyIndex = 0

#list for joining characters
characterList = []

#encode function
def encode(inputText, key, keyIndex, characterList):
    for originalLetter in inputText:
        if originalLetter.isupper() == True:
            loweredLetter = originalLetter.lower()
        else:
            loweredLetter = originalLetter
        letterIndex = ord(loweredLetter) - 97
        if letterIndex + 97 in rangeLowercase:
            pass
        elif letterIndex + 97 not in rangeLowercase:
            characterList.append(chr(letterIndex+97))
            continue
        keyOrd = ord(key[keyIndex]) - 97
        encryptedIndex = (letterIndex + keyOrd) % 26 + 97
        encryptedLetter = chr(encryptedIndex)
        if originalLetter.isupper() == True:
            characterList.append(encryptedLetter.upper())
        else:
            characterList.append(encryptedLetter)
        keyIndex = keyIndex + 1
        if keyIndex >= len(key):
            keyIndex = 0
        else:
            continue
    characterListString = "".join(characterList)
    print("Encrypted text: ", end="")
    print(characterListString)
    print()
    characterList.clear()

#decode function
def decode(inputText, key, keyIndex, characterList):
    for originalLetter in inputText:
        if originalLetter.isupper() == True:
            loweredLetter = originalLetter.lower()
        else:
            loweredLetter = originalLetter
        encryptedIndex = ord(loweredLetter) - 97
        if encryptedIndex + 97 in rangeLowercase:
            pass
        elif encryptedIndex + 97 not in rangeLowercase:
            characterList.append(chr(encryptedIndex+97))
            continue
        keyOrd = ord(key[keyIndex]) - 97
        letterIndex = (encryptedIndex - keyOrd) % 26 + 97
        loweredLetter = chr(letterIndex)
        if originalLetter.isupper() == True:
            characterList.append(loweredLetter.upper())
        else:
            characterList.append(loweredLetter)
        keyIndex = keyIndex + 1
        if keyIndex >= len(key):
            keyIndex = 0
        else:
            continue
    characterListString = "".join(characterList)
    print("Original text: ", end="")
    print(characterListString)
    print()
    characterList.clear()

print("Welcome to the Vigenere cipher encoder & decoder. Specify your parameters below.\nOnly latin lowercase & uppercase letters are encoded, special characters are ignored!\n")
while True:
    #try executing main loop
    try:
        #try getting operartionType
        try:
            print("Choose operation type:\n1) Encryption \n2) Decryption")
            print("Operation: ", end="")
            operationType = int(input())
            if operationType == 1 or operationType == 2:
                pass
            else:
                raise ValueError
        #except operationType !=1 or !=2 print error and start again
        except ValueError:
            print("\nInvalid input! Choose correct operation type.\n")
            continue
        #if no error continue
        else:
            while True:
                #try to get inputText
                try:
                    print("\nInput text: ", end="")
                    inputText = str(input())
                    if inputText == "":
                        raise ValueError
                    else:
                        pass
                #except inputText is blank print error and start again
                except ValueError:
                    print("\nInvalid input! Enter correct phrase.")
                    continue
                #if no error continue
                else:
                    while True:
                        #try to get keyword
                        try:
                            print("\nKeyword: ", end="")
                            key = str(input())
                            if key == "":
                                raise ValueError
                            else:
                                #print("\n")
                                pass
                        except ValueError:
                            print("\nInvalid input! Enter correct phrase.")
                            continue
                        #if no error continue
                        else:
                            print()
                            if operationType == 1:
                                encode(inputText, key, keyIndex, characterList)
                            elif operationType == 2:
                                decode(inputText, key, keyIndex, characterList)
                            while True:
                                try:
                                    print("More? (blank = yes), (y/n)")
                                    wantMore = str(input())
                                    if wantMore == "" or wantMore == "y":
                                        pass
                                    elif wantMore == "n":
                                        quit()
                                    else: 
                                        raise ValueError
                                except ValueError:
                                    continue
                                else:
                                    raise FinishException
    #except FinishException is raised finish main loop and start again
    except FinishException:
        continue
