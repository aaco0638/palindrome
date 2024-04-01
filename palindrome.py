def is_palindrome(text): # function that returns the string if it is a palindrome 
    text = ''.join(char.lower() for char in text if char.isalnum()) # this goes through each character and converts it to lowercase, the .isalnum makes sure only numbers and letters are the focus of the palindrome check. the .join rejoins all newly lowercased chars back into the string.
    return text == text[:: -1] # checks if input text is equal to the reverse of itself. 

# test
text1 = "racecar" 
text2 = "morning"
text3 = "mom"

print(f"{text1} is a palindrome: {is_palindrome(text1)}") #using an f string to include functiion call and the variable in the string output this runs the is_palindrome function.
print(f"{text2} is a palindrome: {is_palindrome(text2)}")
print(f"{text3} is a palindrome: {is_palindrome(text3)}")