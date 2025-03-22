import random
import nltk
import time
from tqdm import tqdm
from fuzzywuzzy import fuzz
from nltk.corpus import words as nltk_words
from nltk.tokenize import word_tokenize
import os

# Constants
SIMILARITY_THRESHOLD = 50
DYSLEXIA_SCORE_THRESHOLD = 3.5

# Ensure necessary NLTK resources are available
def ensure_nltk_resources():
    nltk.download('punkt')
    nltk.download('words')

ensure_nltk_resources()

# Create a set of English words from NLTK
english_vocab = set(w.lower() for w in nltk_words.words())

# Dyslexic confusions
DYSLEXIC_LETTER_CONFUSIONS = [
    ('b', 'd'), ('p', 'q'), ('m', 'w'), ('n', 'u'), ('n', 'r'),
    ('i', 'j'), ('a', 'e'), ('s', 'z'), ('f', 't'), ('c', 'k'),
    ('g', 'q'), ('h', 'n'), ('v', 'w'), ('b', 'p'), ('c', 's'),
    ('d', 't'), ('o', 'e'), ('a', 'o'), ('u', 'v'), ('m', 'n')
]

DYSLEXIC_WORD_CONFUSIONS = [
    ('was', 'saw'), ('there', 'their'), ('here', 'hear'),
    ('you', 'your'), ('where', 'wear'), ('to', 'too', 'two'),
    ('their', 'there'), ('its', "it's"), ('new', 'knew'),
    ('there', 'their', "they're"), ('your', "you're"), ('break', 'brake'),
    ('bare', 'bear'), ('peace', 'piece'), ('where', 'wear'),
    ('right', 'write'), ('flower', 'flour'), ('buy', 'by', 'bye'),
    ('no', 'know'), ('for', 'four'), ('sun', 'son'),
    ('allowed', 'aloud'), ('hour', 'our'), ('blew', 'blue'),
    ('sew', 'sow'), ('be', 'bee'), ('one', 'won'), ('here', 'hair'),
    ('you', 'ewe'), ('toe', 'tow'), ('threw', 'through'),
    ('role', 'roll'), ('mail', 'male'), ('tail', 'tale')
]

# Tokenization function
def tokenize_and_clean_text(text):
    words = word_tokenize(text.lower())
    return [word for word in words if word.isalnum()]

# Check if two strings match exactly
def is_exact_match(user_text, random_sentence):
    return user_text.lower().strip() == random_sentence.lower().strip()

# Check string similarity using fuzzy matching
def are_strings_similar(str1, str2, threshold=SIMILARITY_THRESHOLD):
    similarity_score = fuzz.ratio(str1.lower(), str2.lower())
    return similarity_score >= threshold

# Calculate dyslexia score for a word
def calculate_word_dyslexia_score(word, random_sentence):
    word_tokens = tokenize_and_clean_text(word)
    sentence_tokens = tokenize_and_clean_text(random_sentence)
    dyslexia_score = 0

    if word_tokens == sentence_tokens:
        return 0

    for word_token in word_tokens:
        token_dyslexia_score = 0

        if word_token not in english_vocab:
            token_dyslexia_score += 3.0

        for confusion in DYSLEXIC_LETTER_CONFUSIONS:
            if confusion[0] in word_token and confusion[1] in word_token:
                token_dyslexia_score += 3.0

        for confusion in DYSLEXIC_WORD_CONFUSIONS:
            if any(conf_word == word_token for conf_word in confusion):
                token_dyslexia_score += 4.0

        if word_token[::-1] in sentence_tokens:
            token_dyslexia_score += 3.0

        dyslexia_score += token_dyslexia_score

        if token_dyslexia_score == 0:
            dyslexia_score -= 0.3

    return dyslexia_score

# Dyslexia analysis function
def dyslexia_analysis(user_text, random_sentence):
    if is_exact_match(user_text, random_sentence):
        return 0

    words = tokenize_and_clean_text(user_text)
    dyslexia_scores = [calculate_word_dyslexia_score(word, random_sentence) for word in words]
    avg_score = round(sum(dyslexia_scores) / len(dyslexia_scores), 3) if dyslexia_scores else 0.0
    return avg_score

# Process Dyslexia Test
def process_dyslexia_test(user_text, random_sentence):
    score = dyslexia_analysis(user_text, random_sentence)
    diagnosis = "Dyslexia Detected" if score >= DYSLEXIA_SCORE_THRESHOLD else "No Dyslexia Detected"
    return {"score": score, "diagnosis": diagnosis}
