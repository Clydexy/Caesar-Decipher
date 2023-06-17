#Dependencies needed for menu
import os
import sys

#Define a dictionary of the english letter frequencies
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

#Define a function that takes a string and caesar shifts it by a given amount
def caesarShift(text, shift):
    #Create an empty string to store the shifted text
    cipher = ""
    #Loop through the text
    for char in text:
        #Check if the character is a letter
        if char.isalpha():
            #Shift the character by the shift amount
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        #If the character is not a letter, add it to the cipher as is
        else:
            cipher += char
    #Return the shifted text
    return cipher

#Define a function to crack a caesar cipher using frequency analysis through the mean squared error
def decodeBruteForce(text):
    #Store the errors to find the lowest
    errors = []
    
    #Go through each possible shift
    #TODO: Make this more efficient by shifting the freqeuncies rather than the text
    for i in range(25):
        shiftedText = caesarShift(text, i)
        
        #Compute the frequencies
        letterFreq = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0}
        for char in shiftedText:
            if char in letterFreq:
                letterFreq[char] += 1
        
        #Calcluate error
        meansquarederror = 0
        for char in englishLetterFreq:
            meansquarederror += ((letterFreq[char] / len(text) * 100) - englishLetterFreq[char])**2
        errors.append(meansquarederror)
    return errors.index(min(errors)), caesarShift(text, errors.index(min(errors)))
    
    
# Menu System
if __name__ == "__main__":
    if not len(sys.argv) == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        text  = input("Enter the text: ").upper()
    if not len(sys.argv) ==1 and sys.argv[1] == "-d":
        os.system('cls' if os.name == 'nt' else 'clear')
        solutions = decodeBruteForce(text)
        print("The most likely shift was: " + str((26 - solutions[0]) % 26))
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The decoded text is: " + solutions[1])
    elif not len(sys.argv) ==1 and sys.argv[1] == '-e':
        os.system('cls' if os.name == 'nt' else 'clear')
        shift = int(input("Enter the shift amount: "))
        os.system('cls' if os.name == 'nt' else 'clear')
        print("The encoded text is: " + caesarShift(text, shift))
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Usage: python3 FreqAnalysisCaes.py -d (decode) or -e (encode)")
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
    
    