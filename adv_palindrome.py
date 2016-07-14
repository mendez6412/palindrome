import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    return re.sub('[^A-Za-z0-9]', '', sentence).lower() == re.sub('[^A-Za-z0-9]', '', sentence)[::-1].lower()

def main():
    # TODO: put your input/output code here
    pal = input("Please enter a potential palindrome: ")
    return pal

if __name__ == '__main__':
    if is_palindrome(main()):
        print("Yes!")
    else:
        print("No!")
