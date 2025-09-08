"""
# STRING FUNCTIONS & METHODS IN PYTHON (50+)

String   : "Vikash Kumar"
Purpose  : To demonstrate Python's built-in string methods and related functions with examples.


1.  Length & Representation → len(), str(), repr()
2.  Case Conversion          → upper(), lower(), title(),
                               capitalize(), swapcase(), casefold()
3.  Whitespace Handling      → strip(), lstrip(), rstrip()
4.  Search & Replace         → find(), rfind(), index(), rindex(),
                               replace(), count()
5.  Splitting & Joining      → split(), splitlines(),
                               join(), partition(), rpartition()
6.  Checking Content         → isalpha(), isdigit(), isnumeric(),
                               isalnum(), isascii(), isprintable(),
                               isspace(), istitle(), islower(),
                               isupper()
7.  Alignment & Formatting   → center(), ljust(), rjust(), zfill(),
                               format(), format_map()
8.  Encoding & Translation   → encode(), expandtabs(),
                               maketrans(), translate()
9.  Prefix & Suffix          → startswith(), endswith(),
                               removeprefix(), removesuffix()
10. Iteration & Operators    → __contains__(), __getitem__(),
                               __iter__(), __len__()
11. Character Utilities      → ord(), chr(), min(), max(), sorted()
12. Logic Utilities          → any(), all()

"""

# Define example string
text = "Vikash Kumar"
print("Original string:", text)  # "Vikash Kumar"
print("-" * 60)  # Separator line

# 1. len()
print("1. len(text):", len(text))  # 12

# 2. str()
num = 2025
print("2. str(num):", str(num))  # "2025"

# 3. upper()
print("3. text.upper():", text.upper())  # "VIKASH KUMAR"

# 4. lower()
print("4. text.lower():", text.lower())  # "vikash kumar"

# 5. strip()
text_space = "   Vikash Kumar   "
print("5. text_space.strip():", text_space.strip())  # "Vikash Kumar"

# 6. lstrip()
print("6. text_space.lstrip():", text_space.lstrip())  # "Vikash Kumar   "

# 7. rstrip()
print("7. text_space.rstrip():", text_space.rstrip())  # "   Vikash Kumar"

# 8. replace()
print(
    "8. text.replace('Kumar', 'Sharma'):", text.replace("Kumar", "Sharma")
)  # "Vikash Sharma"

# 9. split()
print("9. text.split():", text.split())  # ['Vikash', 'Kumar']

# 10. splitlines()
multiline = "Vikash\nKumar\nPython"
print(
    "10. multiline.splitlines():", multiline.splitlines()
)  # ['Vikash', 'Kumar', 'Python']

# 11. find()
print("11. text.find('Kumar'):", text.find("Kumar"))  # 7

# 12. rfind()
print("12. text.rfind('a'):", text.rfind("a"))  # 9

# 13. index()
print("13. text.index('Kumar'):", text.index("Kumar"))  # 7

# 14. rindex()
print("14. text.rindex('a'):", text.rindex("a"))  # 9

# 15. join()
words = ["Vikash", "Kumar", "Python"]
print("15. '-'.join(words):", "-".join(words))  # "Vikash-Kumar-Python"

# 16. count()
print("16. text.count('a'):", text.count("a"))  # 2

# 17. isalpha()
print("17. text.isalpha():", text.isalpha())  # False (contains space)

# 18. isdigit()
print("18. '12345'.isdigit():", "12345".isdigit())  # True

# 19. isnumeric()
print("19. '2025'.isnumeric():", "2025".isnumeric())  # True

# 20. isalnum()
print("20. 'Vikash123'.isalnum():", "Vikash123".isalnum())  # True

# 21. isascii()
print("21. text.isascii():", text.isascii())  # True

# 22. isprintable()
print("22. text.isprintable():", text.isprintable())  # True

# 23. isspace()
print("23. '   '.isspace():", "   ".isspace())  # True

# 24. istitle()
print("24. text.istitle():", text.istitle())  # True

# 25. islower()
print("25. text.islower():", text.islower())  # False

# 26. isupper()
print("26. text.isupper():", text.isupper())  # False

# 27. startswith()
print("27. text.startswith('Vik'):", text.startswith("Vik"))  # True

# 28. endswith()
print("28. text.endswith('mar'):", text.endswith("mar"))  # True

# 29. capitalize()
print("29. text.capitalize():", text.capitalize())  # "Vikash kumar"

# 30. title()
print("30. text.title():", text.title())  # "Vikash Kumar"

# 31. swapcase()
print("31. text.swapcase():", text.swapcase())  # "vIKASH kUMAR"

# 32. casefold()
print("32. text.casefold():", text.casefold())  # "vikash kumar"

# 33. center()
print("33. text.center(20, '*'):", text.center(20, "*"))  # "*****Vikash Kumar*****"

# 34. ljust()
print("34. text.ljust(20, '-'):", text.ljust(20, "-"))  # "Vikash Kumar-------"

# 35. rjust()
print("35. text.rjust(20, '-'):", text.rjust(20, "-"))  # "-------Vikash Kumar"

# 36. zfill()
print("36. text.zfill(20):", text.zfill(20))  # "0000000000Vikash Kumar"

# 37. format()
print("37. 'Hello {}'.format(text):", "Hello {}".format(text))  # "Hello Vikash Kumar"

# 38. format_map()
print(
    "38. '{name} is learning'.format_map({'name':'Vikash'}):",
    "{name} is learning".format_map({"name": "Vikash"}),
)  # "Vikash is learning"

# 39. encode()
print("39. text.encode():", text.encode())  # b'Vikash Kumar'

# 40. expandtabs()
tab_text = "Vikash\tKumar"
print("40. tab_text.expandtabs(4):", tab_text.expandtabs(4))  # "Vikash   Kumar"

# 41. maketrans() + translate()
trans_table = str.maketrans("V", "B")
print("41. text.translate(trans_table):", text.translate(trans_table))  # "Bikash Kumar"

# 42. partition()
print("42. text.partition(' '):", text.partition(" "))  # ('Vikash', ' ', 'Kumar')

# 43. rpartition()
print("43. text.rpartition(' '):", text.rpartition(" "))  # ('Vikash', ' ', 'Kumar')

# 44. removeprefix() (Python 3.9+)
print("44. text.removeprefix('Vik'):", text.removeprefix("Vik"))  # "ash Kumar"

# 45. removesuffix() (Python 3.9+)
print("45. text.removesuffix('mar'):", text.removesuffix("mar"))  # "Vikash Ku"

# 46. __contains__()
print("46. 'Kumar' in text:", "Kumar" in text)  # True

# 47. __getitem__()
print("47. text[0]:", text[0])  # 'V'

# 48. __iter__()
print(
    "48. list(iter(text)):", list(iter(text))
)  # ['V', 'i', 'k', 'a', 's', 'h', ' ', 'K', 'u', 'm', 'a', 'r']

# 49. __len__()
print("49. text.__len__():", text.__len__())  # 12

# 50. repr()
print("50. repr(text):", repr(text))  # "'Vikash Kumar'"

# 51. ord()
print("51. ord('A'):", ord("A"))  # 65

# 52. chr()
print("52. chr(65):", chr(65))  # 'A'

# 53. min()
print("53. min(text):", min(text))  # ' ' (space has the lowest ASCII value)

# 54. max()
print("54. max(text):", max(text))  # 'u' (u has the highest ASCII value)

# 55. sorted()
print(
    "55. sorted(text):", sorted(text)
)  # [' ', 'K', 'V', 'a', 'a', 'h', 'i', 'k', 'm', 'r', 's', 'u']

# 56. any()
print("56. any(c.isupper() for c in text):", any(c.isupper() for c in text))  # True

# 57. all()
print(
    "57. all(c.isalpha() or c.isspace() for c in text):",
    all(c.isalpha() or c.isspace() for c in text),
)  # True
