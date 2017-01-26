'''
Remove all vowels from the sentence
'''


def remove_vowels(string):

    vowels = "aeiou"
    new_string = ""

    for character in string:
        if character not in vowels:
            new_string += character

    return new_string

sentence = "I love to learn python"
sentence_without_vowels = remove_vowels(sentence)

print(sentence_without_vowels)