#!/usr/bin/env python

import hashlib

"""
A string manipulation library.
"""


# TODO: This code is broken for some reason :(
def reverse(s):
    result = ""

    for i in xrange(len(s)):
        result += s[len(s) - i]

    return result


# TODO: Find more Pythonic way to do this
def character_count(s):
    result = {}
    unique_characters = set(s)

    for unique_character in unique_characters:
        result[unique_character] = s.count(unique_character)

    return result


# TODO: Find more Pythonic way to do this
def redact(s, words_to_redact, redact_word="REDACTED"):
    result = ""
    words = s.split(" ")

    for word in words:
        if word in words_to_redact:
            result += (redact_word + " ")
        else:
            result += (word + " ")

    return result


# TODO: Move to a stronger hashing algorithm
def get_default_string_hash(s):
    h = hashlib.md5(s)

    return h.hexdigest()


# TODO: Find more Pythonic way to do this
def contains(haystack, needle):
    result = False

    for i in xrange(len(needle) - 1, len(haystack) + 1):
        if haystack[i - len(needle): i] == needle:
            result = True
            break

    return result


# TODO: This doesn't work as expected on Windows for some reason...
def strip_newlines(list_of_strings):
    result = [s.rstrip("\n") for s in list_of_strings]

    return result


# TODO: Generalize this function to find arbitrary letter indices
def find_vowel_indices(s):
    vowels = ["a", "e", "i", "o", "u"]

    # Fuck it...
    vowels += ["y"]

    result = {v: [] for v in vowels}
    for vowel in vowels:
        for i, char in enumerate(s):
            if char in vowels:
                result[vowel].append(i)

    return result
