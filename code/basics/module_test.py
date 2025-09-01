import pyjokes
import textwrap

# Get a joke (use 'neutral' instead of 'programming')
joke = pyjokes.get_joke()

# Prepare the box border
border = "+" + "-" * 60 + "+"
title = "|{:^60}|".format("Joke of the Day")
footer = "|{:^60}|".format("Enjoy your coding!")

# Split joke into lines if it's too long
wrapped_joke = textwrap.wrap(joke, width=58)
joke_lines = [f"| {line:<58} |" for line in wrapped_joke]

# Print the formatted joke
print(border)
print(title)
print(border)
for line in joke_lines:
    print(line)
print(border)
print(footer)
print(border)


# This is single line comment example
"""
This is a multi-line comment example.
You can use triple quotes for longer comments.
"""
'''This is another way to write multi-line comments.'''
# End of the code
# This script fetches a joke and displays it in a formatted box.