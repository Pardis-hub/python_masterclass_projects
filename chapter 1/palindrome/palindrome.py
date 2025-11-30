#input a string
def input_string():
    return input("Please enter a word: ")

#check whether the string is a palindrome
def check_palindrome(word):
    if word.lower() == word[::-1].lower():
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

#run 
check = 'y'
while check.lower() == 'y':
    check_palindrome(input_string())
    check = input("Do you want to continue? (y/n)")
else:
    print("End of program")