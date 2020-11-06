#2. Reverse a string and check if it is a Palindrome
#Ex : malayalam - "is a palindrome"
       #english - "is not a palindrome"
word = input('Please enter a string to reverse(case-sensitive): ')
reversedString=[] #new emptylist called reversedString
index = len(word) # calculate length of string and save in index
while index > 0:
    reversedString += word[ index - 1 ] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
palindrome = True #initialize boolean
#loop through length of both strings & compare each character
for i in range(0, int(len(word))): #from 0 to length of the string
    if word[i] != reversedString[i]: #if the character at any index of the string = the
        # character at the same spot of it's reverse
        print(word, " is not a palindrome")
        palindrome = False
#    else
 #       print(word, "is a palindrome")
print(palindrome)
