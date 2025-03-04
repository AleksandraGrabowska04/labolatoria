# zad 1

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_selector(numbers: list[int]) -> list[int]:
    return [num for num in numbers if is_prime(num)]

print(prime_selector([1,2,3,4,5]))

# zad 2

import math

def round_down_to_nearest_ten(number: int) -> int:
    return math.floor(number // 10) * 10

def round_up_to_nearest_ten(number: int) -> int:
    return ((number + 9) // 10) * 10

def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    result = []

    for i in numbers:
        if i < threshold:
            result.append(round_down_to_nearest_ten(i))
        elif i > threshold:
            result.append(round_up_to_nearest_ten(i))
        else:
            result.append(i)

    return result

print(round_numbers([111,222,9999,8888,654], 500))

# zad 3

def longest_increasing_subsequence(sequence: list[int]) -> int:
    if not sequence:
        return 0

    max_length = 1  
    length = 1      

    for i in range(1, len(sequence)):
        if sequence[i-1] < sequence[i]:
            length += 1  
        else:
            max_length = max(max_length, length)  
            length = 1 

    max_length = max(max_length, length)  
    return max_length

print(longest_increasing_subsequence([1, 2, 3, 0, 1, 2]))  

# zad 4

def is_balanced(expression: str) -> bool:
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i in expression:
        if i == "(":
            count_1 += 1
        elif i == ")":
            count_1 -= 1
        if i == "[":
            count_2 += 1
        elif i == "]":
            count_2 -= 1
        if i == "{":
            count_3 += 1
        elif i == "}":
            count_3 -= 1

    
    return count_1 == 0 and count_2 == 0 and count_3 == 0


print(is_balanced("({[]})")) 
print(is_balanced("({[)"))  

# zad 5

def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text

    result = list(text)

    for i in range(0, len(text) - key, key):
        result[i], result[i + key] = result[i + key], result[i]

    return ''.join(result)


print(transposition_cipher("abcdefgh", 3))  
print(transposition_cipher("hello world", 5)) 

# zad 6

def fibonacci_generator(n: int): # Nie potrzeba pisa typu zwracanego
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)  # Dodaj aktualną liczbę Fibonacciego do listy
        a, b = b, a + b  # Przejdź do kolejnej liczby w ciągu
    return fib_sequence

print(fibonacci_generator(10))

# zad 7

from collections import Counter

def most_frequent_element(data: list):
    counter = Counter(data) # licznik 
    most_common = counter.most_common(1)
    
    return most_common[0][0]


data = [1, 2, 3, 1, 2, 1, 4]
print(most_frequent_element(data))  

# zad 8

import re

def count_syllables(word: str) -> int:
    # Usuwamy niealfabetyczne znaki
    word = re.sub(r'[^a-zA-Z]', '', word.lower())
    
    # Liczymy liczbę samogłoskowych ciągów w słowie
    vowels = "aeiouy"
    syllables = 0
    previous_char_was_vowel = False
    
    for char in word:
        if char in vowels:
            if not previous_char_was_vowel:
                syllables += 1
            previous_char_was_vowel = True
        else:
            previous_char_was_vowel = False
    
    return syllables

def readability_score(text: str) -> float:
    sentences = re.split(r'[.!?]', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    word_count_per_sentence = 0
    for sentence in sentences:
        words = sentence.split()
        word_count_per_sentence += len(words)
    avg_words_per_sentence = word_count_per_sentence / len(sentences) if sentences else 0

    syllable_count_per_word = 0
    word_count = 0
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            syllable_count_per_word += count_syllables(word)
            word_count += 1
    avg_syllables_per_word = syllable_count_per_word / word_count if word_count else 0
    
    
    readability = (avg_words_per_sentence + avg_syllables_per_word) / 2
    
    return readability

text = "To jest przykładowe zdanie! A tutaj mamy kolejne zdanie. Czytelność tekstu jest ważna."
score = readability_score(text)
print(f"Wskaźnik czytelności: {score:.2f}")

# zad 9

import itertools

def unique_permutations(elements: list):
    perm = set(itertools.permutations(elements))
    
    return [list(p) for p in perm]

elements = [1, 2, 3]
result = unique_permutations(elements)
print(result) 
  
# zad 10
def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    word_groups = {}
    
    for word in words:
        word_length = len(word)  
        
        if word_length in word_groups:
            word_groups[word_length].append(word)
        else:
            word_groups[word_length] = [word]  
    return word_groups

words = ["111", "222", "3333", "4444", "5", "6"]
result = group_words_by_length(words)
print(result)
