import unittest

from word_fun import palindrome

def test_palindrome_single_word():
    assert palindrome('racecar')

def test_palindrome_mixed_case():
    assert palindrome('RaCeCaR')

def test_palindrome_multiple_words():
    assert palindrome('a man a plan a canal panama')

def test_palindrome_mutliple_words_with_punctuation():
    assert palindrome('A man, a plan, a canal, Panama!')
