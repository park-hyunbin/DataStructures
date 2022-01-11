from stack import *
import re

word = input("회문 체크용 문자열 : ")
word = re.sub("[^a-zA-Z0-9]","",word)
word = word.lower()
word = word.replace(" ","")


def palindrome(word):
    stack = []
    for letter in word:
        stack.append(letter)
    for letter in word:
        if stack.pop() != letter:
            return ("회문아님!!")
    return f"{word} : 회문임!!"

print(palindrome(word))
