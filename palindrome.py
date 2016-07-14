import re

def is_palindrome(sentence):
    sentence = simplify(sentence)
    if len(sentence) == 1:
        return True
    if len(sentence) == 2 and sentence[0] == sentence[-1]:
        return True
    if sentence[0] == sentence[-1]:
        return is_palindrome(sentence[1:-1])
    else:
        return False

def simplify(sentence):
    return re.sub('[^A-Za-z0-9]', '', sentence).lower()

def main():
    # TODO: put your input/output code here
    pal = input("Please enter a potential palindrome: ")
    return pal

if __name__ == '__main__':
    if is_palindrome(main()):
        print("That is a palindrome, pal!")
    else:
        print("That isn't a palindrome, pal!")
