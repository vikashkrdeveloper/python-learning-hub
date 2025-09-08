"""
Negative Slicing in Python
--------------------------
This script demonstrates how to use negative slicing in Python.
Negative indices count from the end of the string:
    -1 → last character
    -2 → second last character
    ... .....
    -n → nth last character
    ...
"""

# Step 1: Define the string
text = "Vikash Kumar"

# Show index mapping for clarity
# Forward Index :  0   1   2   3   4   5   6   7   8   9   10  11
# Characters    :  V   i   k   a   s   h       K   u   m   a   r
# Negative Index: -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# Step 2: Last 4 characters
last_four = text[-4:]  # Start at -4, go till the end
print("Step 2 → Last four characters:", last_four)  # "mar"

# Step 3: Characters from 5th last to 2nd last
middle_section = text[-5:-1]  # Start at -5, stop before -1
print("Step 3 → Characters from 5th last to 2nd last:", middle_section)  # "uma"

# Step 4: All characters except the last 3
except_last_three = text[:-3]  # Start at beginning, stop before -3
print("Step 4 → All except last three:", except_last_three)  # "Vikash Ku"

# Step 5: Every second character from the end
every_second_from_end = text[-1::-2]  # Start at -1, step back by 2
print("Step 5 → Every 2nd char from end:", every_second_from_end)  # "ramKhsV"

# Step 6: Reverse the string
reversed_text = text[::-1]  # Step -1 reverses string
print("Step 6 → Reversed string:", reversed_text)  # "ramuK hsakiV"

# Step 7: Last 3 characters
first_three_from_end = text[-3:]  # Take last 3 chars
print("Step 7 → Last 3 characters:", first_three_from_end)  # "mar"

# Step 8: Characters from 7th last to 4th last
specific_section = text[-7:-4]  # From -7 to -4 (exclusive)
print("Step 8 → Characters from 7th last to 4th last:", specific_section)  # " Ku"

# Step 9: Every third character from the end
every_third_from_end = text[-1::-3]
print("Step 9 → Every 3rd char from end:", every_third_from_end)  # "ruai"

# Step 10: All except first 2 and last 2
except_first_last_two = text[2:-2]
print("Step 10 → All except first 2 and last 2:", except_first_last_two)  # "kash Ku"

# Step 11: Last 5 characters in reverse order
last_five_reversed = text[-1:-6:-1]
print("Step 11 → Last 5 chars reversed:", last_five_reversed)  # "ramuK"

# Step 12: Characters from 6th last to 3rd last
another_section = text[-6:-3]
print("Step 12 → From 6th last to 3rd last:", another_section)  # "Kum"

# Step 13: Every fourth character from the end
every_fourth_from_end = text[-1::-4]
print("Step 13 → Every 4th char from end:", every_fourth_from_end)  # "raV"

# Step 14: All characters except the last 4
except_last_four = text[:-4]
print("Step 14 → All except last four:", except_last_four)  # "Vikash K"

# Step 15: Last 4 characters
first_four_from_end = text[-4:]
print("Step 15 → Last 4 characters:", first_four_from_end)  # "mar"

# Step 16: Characters from 8th last to 5th last
section_eight_to_five = text[-8:-5]
print("Step 16 → From 8th last to 5th last:", section_eight_to_five)  # "ash"

# Step 17: Every fifth character from the end
every_fifth_from_end = text[-1::-5]
print("Step 17 → Every 5th char from end:", every_fifth_from_end)  # "riV"

# Step 18: All characters except the first 3 and last 3
except_first_last_three = text[3:-3]
print("Step 18 → All except first 3 and last 3:", except_first_last_three)  # "ash Ku"

# Step 19: Last 6 characters in reverse order
last_six_reversed = text[-1:-7:-1]
print("Step 19 → Last 6 chars reversed:", last_six_reversed)  # "ramuK "

# Step 20: Characters from 9th last to 6th last
section_nine_to_six = text[-9:-6]
print("Step 20 → From 9th last to 6th last:", section_nine_to_six)  # "kas"

# Step 21: Every sixth character from the end
every_sixth_from_end = text[-1::-6]
print("Step 21 → Every 6th char from end:", every_sixth_from_end)  # "rKV"
