"""
# Working of all `Bitwise Operators` with truth table
print("Truth Table for Bitwise Operators:")
print("A B | A&B A|B A^B ~A A<<1 A>>1")
print("-------------------------------")
for A in [0, 1]:
    for B in [0, 1]:
        print(f"{A} {B} |  {A & B}   {A | B}   {A ^ B}  {~A & 1}   {A << 1}   {A >> 1}")
print()
"""

# Working of all `Bitwise Operators` with truth table
print("Truth Table for Bitwise Operators:")
print("A B | A&B | A|B | A^B | ~A | A<<1 | A>>1")
print("----|-----|-----|-----|----|------|-----")
for A in [0, 1]:
    for B in [0, 1]:
        print(f"{A} {B} |  {A & B}  |  {A | B}  |  {A ^ B}  | {~A & 1}  |  {A << 1}   |  {A >> 1}")
print()
