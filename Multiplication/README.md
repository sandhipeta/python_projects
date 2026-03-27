# 🔢 Multiplication Table Generator (Python)

## 📌 Project Description
This is a simple Python program that prints the multiplication table of a number entered by the user.

The program uses a **for loop** to generate the table from 1 to 10.

This project helps beginners understand:
- user input
- loops
- variables
- basic arithmetic operations

---

## 🎯 Objective
Create a program that:
1. Takes a number as input from the user
2. Uses a loop to calculate multiplication values
3. Displays the multiplication table from 1 to 10

---

## 🧠 Concepts Used
- `input()` function
- `int()` type conversion
- `for loop`
- `range()` function
- formatted string (f-string)
- arithmetic operator (*)

---

## 💻 Python Code

```python
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
