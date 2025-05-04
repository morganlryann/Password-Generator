# 🔐 Random Password Generator (Python)

This is a simple command-line Python app that creates strong, random passwords based on user preferences. It also allows you to save generated passwords to a local file for later use.

---

## 🚀 Features

- Choose your password length
- Optionally include:
  - Uppercase letters
  - Numbers
  - Special characters
- Automatically saves passwords to a `.txt` file with timestamps

---

## 🧪 Example
Your secure password is: g8W#Lm9rX1@z
How long should the password be? 12
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Your secure password is: g8W#Lm9rX1@z

Would you like to save this password? (y/n): y
✅ Password saved to saved_passwords.txt

---

## 📁 Project Structure

Password_Generator/
├── pw_generator.py
├── saved_passwords.txt # (created when you save a password)
└── README.md

---

## 🛠️ How to Run

1. Make sure you have Python installed
2. Open your terminal and navigate to the project folder
3. Run the script:

```bash
python pw_generator.py

If you choose to save your password, it will be stored in saved_passwords.txt along with a timestamp:

2025-05-03 17:45:22 - G#82mZp!cWxT