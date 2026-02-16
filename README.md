# ❄️ Polar CLI Bot

Polar CLI is an interactive, terminal-based bot designed to help you manage files with style. It features a custom command loop, rich text animations, and powerful file management tools.

## ✨ Features
* **Interactive Shell:** Persistent command loop (REPL).
* **File Management:**
    * `fb`: Find "big" files by size threshold (e.g., find all files > 100MB).
    * `del`: Safely delete files with confirmation prompts.
    * `cd`: Change directories navigation.
* **Visuals:** Startup and shutdown animations using `Rich` and `Pyfiglet`.

## 🛠️ Prerequisites
* **Python 3.12** or higher.
* (Optional) **uv** package manager (recommended for fastest setup).

## 🚀 Installation

### Option 1: Using uv (Recommended)
This project uses `uv` for dependency management.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/polarcli.git](https://github.com/yourusername/polarcli.git)
    cd polarcli
    ```

2.  **Sync dependencies:**
    ```bash
    uv sync
    ```

3.  **Run the bot:**
    ```bash
    uv run main.py
    ```

### Option 2: Using standard pip
If you don't use `uv`, you can install the dependencies manually.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/polarcli.git](https://github.com/yourusername/polarcli.git)
    cd polarcli
    ```

2.  **Install requirements:**
    ```bash
    pip install typer rich pyfiglet
    ```

3.  **Run the bot:**
    ```bash
    python main.py
    ```

## 🎮 Usage Guide

Once the bot is running, you will see the `polar>` prompt. Here are the commands you can use:

| Command | Example | Description |
| :--- | :--- | :--- |
| **fb** | `fb 10 mb` | Finds all files larger than 10 MB in the current folder (recursive). |
| **del** | `del data.txt` | Deletes a file safely (asks for confirmation). |
| **cd** | `cd ..` or `cd /users` | Changes the current working directory. |
| **help** | `help` | Displays the help menu with all commands. |
| **exit** | `exit` | Plays the shutdown animation and closes the bot. |

## 📦 Project Structure
* `main.py`: The entry point and main loop for the bot.
* `files.py`: Helper module for file operations.

## ❄️ Stay Frosty!
