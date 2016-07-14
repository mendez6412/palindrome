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
    if is_palindrome(pal):
        print("That is a palindrome, pal!")
    else:
        print("That isn't a palindrome, pal!")

if __name__ == '__main__':
    main()


# START ADVANCED SOLUTION
# import re
#
# def is_palindrome(sentence):
#     print(re.sub('[^A-Za-z0-9]', '', sentence)[::-1])
#     # TODO: return True or False if the sentence is or isn't a palindrome
#     if re.sub('[^A-Za-z0-9]', '', sentence).lower() == re.sub('[^A-Za-z0-9]', '', sentence)[::-1].lower():
#         return True
#     else:
#         return False
#
#
# def main():
#     # TODO: put your input/output code here
#     pal = input("Please enter a potential palindrome: ")
#     return pal
#
# if __name__ == '__main__':
#     if is_palindrome(main()):
#         print("Yes!")
#     else:
#         print("No!")

# START LOOP SOLUTION
# import re
#
# def is_palindrome(sentence):
#     sentence = simplify(sentence)
#     print(sentence)
#     # TODO: return True or False if the sentence is or isn't a palindrome
#     while len(sentence) >= 0:
#         print(len(sentence))
#         if len(sentence) == 1 or len(sentence) == 0:
#             return True
#         if compare_first_and_last(sentence):
#             sentence = remove_first_and_last(sentence)
#         else:
#             return False
#
# def simplify(sentence):
#     return re.sub('[^A-Za-z0-9]', '', sentence).lower()
#
# def compare_first_and_last(sentence):
#     if sentence[0] == sentence[-1]:
#         return True
#
# def remove_first_and_last(sentence):
#     return sentence[1:-1]
#
# def main():
#     # TODO: put your input/output code here
#     pal = input("Please enter a potential palindrome: ")
#     return pal
#
# if __name__ == '__main__':
#     if is_palindrome(main()):
#         print("Yes!")
#     else:
#         print("No!")
