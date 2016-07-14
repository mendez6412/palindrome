import sys

# This is the file I want to read!!!
sys.argv[1]

f = open(sys.argv[1], 'r')
pal_file = f.read().splitlines()
f.close()

f = open(sys.argv[1], 'r')
whole_file = f.read()
f.close()

import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    if re.sub('[^A-Za-z0-9]', '', sentence).lower() == re.sub('[^A-Za-z0-9]', '', sentence)[::-1].lower():
        return True
    else:
        return False


def main():
    # TODO: put your input/output code here
    pal = "string"

if __name__ == '__main__':
    for item in pal_file:
        if is_palindrome(item):
            print(item)
            print("Yes, the above line is a palindrome!")
            print()
        else:
            print(item)
            print("No, the above line is not a palindrome.")
            print()
    if is_palindrome(whole_file):
        print("Interestingly, the entire file (if read from start to finish) is a palindrome")
