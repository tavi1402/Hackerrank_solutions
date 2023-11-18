'''This code defines a function is_vowel that checks if a given letter is a vowel (either 'a', 'e', 'i', 'o', 'u', or 'y').
 It then defines another function score_words that calculates a score based on the number of vowels in each word in a 
 given list of words. The score is incremented by 2 if the word has an even number of vowels and by 1 if the word has 
 an odd number of vowels. Finally, the code reads an integer n representing the number of words, reads a list of words 
 from the user, and prints the total score.'''

# Define a function 'is_vowel' that checks if a letter is a vowel.
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

# Define a function 'score_words' that calculates a score based on the number of vowels in each word.
def score_words(words):
    score = 0
    # Iterate through each word in the list.
    for word in words:
        num_vowels = 0
        # Iterate through each letter in the word.
        for letter in word:
            # Check if the letter is a vowel and increment the count.
            if is_vowel(letter):
                num_vowels += 1
        # Increment the score based on the parity of the number of vowels in the word.
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

# Read an integer 'n' from the user.
n = int(input())

# Read a list of words from the user.
words = input().split()

# Print the total score calculated using the 'score_words' function.
print(score_words(words))
