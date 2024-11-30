import random


# Start : 11/19/2024

#test change

def main():
    
    inputUser = input("Enter in the Encrypted Message: ")
    caesearUser = inputUser.split()
    caeser_cipher(caesearUser)

def caeser_cipher(encrypt):
    message = encrypt
    finalStatus = [False,message]
    wordList = getWords()

    for i in range(1,27):
        for y in range(len(message)):
            if len(message[y]) >= 4:
                checkList = message[y].split()
                for x in range(len(checkList)):
                    checkList[x] = chr(ord(checkList[x])+i)
                if checkList in wordList:
                    print("Found"+checkList)
                    break




def getWords():
    wordlist = open("1000-most-common-words.txt","r")
    words = wordlist.read().split()
    wordlist.close()
    return words

    

#main()


def bugging():
    message = "g`ud"
    
    for i in range(1,27):
        if len(message) >= 4:
            checking = message.split()
            for x in range(len(message)):
                checking[x] = chr(ord(checking[x])+i)
        print(checking)
    

bugging()

# a b c d e f g h i j k l m n o p q r s t u v w x y z