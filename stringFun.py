str1 = input("Enter the string 1:")
str2 = input("Enter the String 2:")
#Concatentation: Adding two or more then two strings
finalStr = str1 + str2
print(finalStr)
#Len : This function returns the length of the string
length = len(str1)
print(length)
#Count :This function returns the occurance of the String
word = input("Enter Your word you want to find:")
print(str1.find(word))
#Find: This Function retuns the strting index of the Word 
print(str1.count(word))
#replace :This function replaces the old word with new word
newWord = input("Enter the New word you want to replace")
oldWord = input("Enter the old word you want to replace") 
str2 = str2.replace(oldWord,newWord)
print(str2)
#Capitalize :This function makes the first Word captial of the string
str1 = str1.capitalize()
print(str1)
