# loop_tasks.py
# Task 4: Loops & Iterations

print("===== TASK 4: LOOPS & ITERATIONS DEMO =====\n")

# 1. For loop: Print numbers from 1 to 100
print("1) Printing numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# 2. While loop: Countdown timer
print("2) Countdown Timer:")
count = 10
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Time's up!\n")

# 3. Break and Continue example
print("3) Break and Continue Example:")
for i in range(1, 11):
    if i == 5:
        print("Skipping 5 using continue")
        continue
    if i == 8:
        print("Stopping loop at 8 using break")
        break
    print("Number:", i)
print()

# 4. Iterate over string characters
print("4) Iterating over string characters:")
name = "Python"
for ch in name:
    print(ch)
print()

# 5. Multiplication Table
print("5) Multiplication Table of 7:")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print()

# 6. Range with steps
print("6) Numbers from 0 to 20 with step 2:")
for i in range(0, 21, 2):
    print(i, end=" ")
print("\n")

# 7. Loop with condition
print("7) Even numbers between 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print("\n")

# 8. Real-world example: Shopping cart total
print("8) Real-world Example: Shopping Cart Total")
prices = [199, 299, 499, 150]
total = 0

for price in prices:
    total += price

print("Total bill amount:", total)

print("\n===== END OF TASK =====")
