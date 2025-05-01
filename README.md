

# Typing Game

A simple terminal-based typing game built in Python. The game measures your typing speed by asking you to replicate a randomly generated text as quickly and accurately as possible.

---

### 🎮 Features

- Displays a stylish ASCII-art start menu
- Option to start the game or exit
- Generates random sentences to type
- Live typing feedback with color-coded output (correct text in green)
- Displays typing duration and words-per-minute (WPM) at the end
- Terminal-width adaptive centering for UI elements

---

### 🚀 How to Run

1. **Requirements**
   - Python 3.x
   - Install dependencies with:
     ```bash
     pip install colorama lorem
     ```

2. **Run the game**
   ```bash
   python <filename>.py
   ```

---

### 📝 Controls

- At the start menu, type `1` to start the game or `2` to exit.
- Type the displayed text exactly as it appears.
- Typing progress is updated live in the terminal.

---

### 🖥️ Notes

✅ Works best on Windows due to use of `msvcrt.getwch()` for real-time key input.

✅ For cross-platform support (Linux/macOS), replace `msvcrt.getwch()` with an alternative (e.g., `getch` from `getch` library or `curses`).

✅ Clears terminal screen dynamically depending on OS.

---

### 📂 File Structure

```
typing_game.py    # Main game script
README.md         # This file
```

---

### 👤 Author

- Telegram: [@RedSnows](https://t.me/RedSnows)
- GitHub: [mmd-dll](https://github.com/mmd-dll)

Enjoy the game! 🎉

