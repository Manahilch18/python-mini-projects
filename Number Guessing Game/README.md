# 🎯 Number Guessing Game

A fun and interactive **command-line number guessing game** built with pure Python. Guess the secret number within limited attempts and earn points based on how quickly you solve it!

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🎲 **Random number generation** between 1 and 50 every round
- 📉 **Hot & cold hints** — tells you if your guess is too high or too low
- 🏆 **Score system** — earn more points for guessing in fewer attempts
- 🔁 **Play again option** — replay instantly without restarting the script
- 🛡️ **Input validation** — handles non-numeric input gracefully

---

## 🏆 Scoring System

Points are awarded based on how many attempts you use:

| Attempts Used | Points Earned |
|---|---|
| 1 | 100 pts |
| 2 | 80 pts |
| 3 | 60 pts |
| 4 | 40 pts |
| 5 | 20 pts |

> Formula: `points = (max_attempts - attempts + 1) × 20`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x (no third-party packages needed)

### Run the Game

```bash
# 1. Clone the repository
git clone https://github.com/Manahilch18/number-guessing-game.git
cd number-guessing-game

# 2. Run the script
python guessing_game.py
```

---

## 📁 Project Structure

```
number-guessing-game/
├── guessing_game.py   # Main game script
└── README.md          # This file
```

---

## 💡 Example Gameplay

```
Welcome to Number Guessing Game
Guess a number between 1 and 50
You have 5 attempts.

Enter your guess: 25
Too high, try again
Enter your guess: 12
Too low, try again
Enter your guess: 18
Congratulations! You guessed the number in 3 attempts.
Attempts used: 3
🏆 Your score: 60 points

Do you want to play again? (yes/no): no
👋 Thanks for playing!
```

---

## ⚙️ Game Rules

- The secret number is randomly chosen between **1 and 50** each round.
- You have a maximum of **5 attempts** to guess correctly.
- After each wrong guess, you get a **Too High** or **Too Low** hint.
- If you fail all 5 attempts, the correct number is revealed.
- Type `yes` to play again or `no` to quit after each round.

---

## 🔮 Future Improvements

- [ ] Difficulty levels (Easy: 10 attempts, Hard: 3 attempts)
- [ ] Wider number range options (1–100, 1–500)
- [ ] Persistent leaderboard to track high scores
- [ ] Countdown timer for extra challenge
- [ ] GUI version using Tkinter or Pygame

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).