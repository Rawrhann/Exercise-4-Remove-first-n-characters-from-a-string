#Exercise 4: Remove first n characters from a string
#Write a program to remove characters from a string starting from zero up to n and return a new string.

word_input = input("Input Word ")
print("your word is", word_input)
chosen_number = int(input())
length_of_the_word = len(word_input)
print("your number is", chosen_number)
for i in range(chosen_number, length_of_the_word , 1):
    print(word_input[i])