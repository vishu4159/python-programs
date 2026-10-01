# Python program to perform various operations on strings using functions

def string_length(s):
    return len(s)


def convert_uppercase(s):
    return s.upper()


def convert_lowercase(s):
    return s.lower()


def reverse_string(s):
    return s[::-1]


def concatenate_strings(s1, s2):
    return s1 + s2


def count_character(s, ch):
    return s.count(ch)


def find_substring(s, sub):
    return s.find(sub)


str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

print("\n--- String Operations ---")

print("Length of first string:", string_length(str1))
print("Uppercase:", convert_uppercase(str1))
print("Lowercase:", convert_lowercase(str1))
print("Reverse:", reverse_string(str1))
print("Concatenation:", concatenate_strings(str1, str2))

ch = input("Enter a character to count: ")
print("Occurrences of", ch, ":", count_character(str1, ch))

sub = input("Enter a substring to search: ")
print("Position of substring:", find_substring(str1, sub))
