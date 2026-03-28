# 🎯 Number Guessing Game in Python

A fun beginner-friendly Python game where the computer randomly selects a number, and the player must guess it within limited attempts.

This project helps beginners understand:
- Python basics
- Loops
- Conditional statements
- User input handling
- Random number generation
- Basic game logic

---

## 📌 Project Description

The program generates a random number between **1 and 10**, and the player has **4 chances** to guess the correct number.

After each incorrect guess, the program gives a hint whether the actual number is **higher or lower** than the guessed number.

The score depends on how quickly the correct number is guessed.

---

## 🚀 Features

- Random number generation using Python
- Limited number of attempts (4 chances)
- Hint system (Higher / Lower)
- Score calculation based on remaining attempts
- Beginner-friendly code structure

---

## 🛠 Technologies Used

- Python 3
- Built-in libraries:
  - `random`
  - `time`

---

## 💻 Code

```python
import random
import time

print('Hello World! Welcome to the game')
time.sleep(2)

n = random.randint(1, 10)

print('Number has been generated!!\nYou have 4 chances to guess the number')

count = 4
score = 0

while count != 0:
    a = int(input('Guess the number: '))

    if a == n:
        print("Yay! That's right. You won!")
        score = count * 10
        print("Your score is:", score)
        break

    elif a > n:
        print('The number is less than', a)

    else:
        print('The number is greater than', a)

    count -= 1

print(count)
