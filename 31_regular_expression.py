# Python program to demonstrate regular expressions

import re

text = "My phone number is 9876543210 and my age is 22."

# Find all numbers
numbers = re.findall(r'\d+', text)

print("Numbers found:", numbers)
