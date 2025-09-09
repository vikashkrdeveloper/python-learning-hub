"""
Replacing and Chaining String Methods in Python
-----------------------------------------------
This file demonstrates:
1. Using str.replace()
2. Chaining multiple string methods together
"""

# 1. str.replace()
print("\n--- str.replace() ---")

text = "I love Java. Java is powerful, but I prefer Python over Java."

# Replace all occurrences
replaced_all = text.replace("Java", "Python")
print("Replace all:", replaced_all)

# Replace only first occurrence
replaced_one = text.replace("Java", "Python", 1)
print("Replace first only:", replaced_one)

# Replace with empty string (removal)
removed_word = text.replace("Java", "")
print("Removed 'Java':", removed_word)

# 2. Chaining String Methods

print("\n--- Chaining String Methods ---")

sentence = "   hello world, python is FUN!   "

# Chain: strip → replace → lower → capitalize
chained = sentence.strip().replace("FUN", "awesome").lower().capitalize()
print("Chained result:", chained)

# Chain: replace → upper
upper_case = sentence.replace("python", "Java").upper()
print("Replace + upper:", upper_case)

# Chain: strip → title case
title_case = sentence.strip().title()
print("Title case:", title_case)

# Chain: strip → split → join
joined = " | ".join(sentence.strip().split())
print("Split + join:", joined)
