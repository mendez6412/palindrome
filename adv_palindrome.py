import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    return re.sub('[^A-Za-z0-9]', '', sentence).lower() == re.sub('[^A-Za-z0-9]', '', sentence)[::-1].lower()

def main():
    # TODO: put your input/output code here
    pal = input("Please enter a potential palindrome: ")
    if is_palindrome(pal):
        print("Pal, you entered a palindrome!")
    else:
        print("Oh no, that's not a palindrome!")

if __name__ == '__main__':
    main()
