# knockoffroblox

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Lightweight Python project that provides a menu UI to run simple "game" scripts from a games/ folder. This repository is a learning/prototype project inspired by sandbox platforms.

## Project overview

- Entry point: `main.py`
- UI: CustomTkinter + CTkMessagebox
- Discord Rich Presence: pypresence
- GitHub integration: PyGithub (uses an Auth.Token object in the code)
- Game scripts live in the `games/` directory. Each `.py` file in `games/` appears as a button in the menu and is launched as a subprocess.

## Quick start

1. Clone the repository:
   git clone https://github.com/RoshanGamer7791/knockoffroblox.git
   cd knockoffroblox

2. Create and activate a virtual environment (recommended):
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows (PowerShell)
   .\.venv\Scripts\Activate.ps1

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   python main.py

When you run `main.py`, a login/signup popup appears. Signing up encrypts the username/password and writes `logindetails.json` in the repo directory. The menu lists `.py` files inside the `games/` folder (excluding `__init__.py`) and launches them as separate Python subprocesses.

## Requirements

The repository’s requirements file lists:
- cryptography==46.0.6
- CTkMessagebox==2.7
- customtkinter==5.2.2
- PyGithub==2.9.0
- pypresence==4.6.1
- ursina==8.3.0

Install with:
pip install -r requirements.txt

Adjust versions as needed.

## How the code works (notes from `main.py`)

- The program changes working directory to the repo directory and initializes a Fernet cipher with a hard-coded key.
- It decrypts a hard-coded encrypted token and constructs a PyGithub Auth.Token to create a Github client.
- The main GUI (CustomTkinter) shows a horizontally scrollable frame of buttons for `.py` files in `games/`.
- Launching a game runs it in a subprocess and updates Discord RPC presence while the subprocess runs.
- Login/signup encrypted credentials are stored in `logindetails.json`.

## Games folder

- Put any simple game/demo script in `games/` with a `.py` extension.
- Each file will appear as a large button on the main menu; clicking it runs the script via the same Python interpreter.

Example placeholder:

```python
# games/example_game.py
print("Example game started")
input("Press Enter to exit")
```

## Development / Contributing

- Follow PEP8 and use linters/formatters like black/flake8 if desired.
- Add new games as independent `.py` files inside `games/`.
- If you add new dependencies, update `requirements.txt`.

Suggested workflow:
1. Fork → branch → changes → PR
2. Keep secrets out of commits
3. Add tests for game components if you formalize APIs

## License

This project is licensed under the MIT License — see the `LICENSE` file for details.

## Contact

Repository owner: RoshanGamer7791

---
