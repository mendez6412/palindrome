import re

def is_palindrome(sentence):
    sentence = simplify(sentence)
    # TODO: return True or False if the sentence is or isn't a palindrome
    while len(sentence) >= 0:
        if len(sentence) == 1 or len(sentence) == 0:
            return True
        if compare_first_and_last(sentence):
            sentence = remove_first_and_last(sentence)
        else:
            return False

def simplify(sentence):
    return re.sub('[^A-Za-z0-9]', '', sentence).lower()

def compare_first_and_last(sentence):
    if sentence[0] == sentence[-1]:
        return True

def remove_first_and_last(sentence):
    return sentence[1:-1]

def main():
    # TODO: put your input/output code here
    pal = input("Please enter a potential palindrome: ")
    return pal

if __name__ == '__main__':
    if is_palindrome(main()):
        print("Pal, you entered a palindrome!")
    else:
        print("Oh no, that's not a palindrome!")
