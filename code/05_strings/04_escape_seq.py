r"""
Escape Sequences in Python
--------------------------

Escape sequences are special characters preceded by a backslash `\`.
They let you include characters in strings that are otherwise hard to type.

Common Escape Sequences:
- \n : Newline
- \t : Tab
- \\ : Backslash
- \' : Single Quote
- \" : Double Quote
- \r : Carriage Return
- \b : Backspace
- \f : Form Feed
- \v : Vertical Tab
- \ooo : Octal value (1–3 octal digits)
- \xhh : Hexadecimal value (1–2 hex digits)
- \uXXXX : Unicode character (4 hex digits)
- \UXXXXXXXX : Unicode character (8 hex digits)
- \N{name} : Named Unicode character
"""

# Example usage of escape sequences in Python

Vikash_Kumar = "Hello, I am Vikash Kumar.\nI live in India.\nI love programming.\n\tI also love to travel.\nHere is a backslash: \\"
print(Vikash_Kumar)

quote = 'He said, "It\'s a beautiful day!"'
print(quote)

# File path examples
path1 = "C:\\Users\\Vikash\\Documents"  # Escaped backslashes
path2 = r"C:\Users\Vikash\Documents"  # Raw string
print(path1)
print(path2)

# Unicode examples
unicode_example = "Unicode character: \u03a9"  # Greek capital letter Omega
print(unicode_example)

named_unicode_example = "Named Unicode character: \N{GREEK CAPITAL LETTER OMEGA}"
print(named_unicode_example)

# Other escape sequences
form_feed_example = "Hello\fWorld"
print(form_feed_example)

vertical_tab_example = "Hello\vWorld"
print(vertical_tab_example)

carriage_return_example = "Hello\rWorld"
print(carriage_return_example)

backspace_example = "Hello\bWorld"
print(backspace_example)

octal_example = "Octal character: \101"  # 'A' in octal
print(octal_example)

hex_example = "Hexadecimal character: \x41"  # 'A' in hexadecimal
print(hex_example)
