# knockoffroblox

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Lightweight Python project that provides a menu UI to run simple "game" scripts from a games/ folder. This repository is a learning/prototype project inspired by sandbox platforms.

> Warning: This project currently contains hard-coded secrets in `main.py` (an encryption key and an encrypted token). See the Security section below and rotate/remove secrets immediately.

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

## Security (urgent)

I found two major security issues in the current repository state:

1. Hard-coded Fernet key and encrypted token inside `main.py`:
   - `main.py` contains a plaintext Fernet key and an encrypted token string. Anyone with access to the repo can decrypt or misuse these values, depending on how the token was created.
   - The code creates a PyGithub `Auth.Token` from the decrypted secret — this is effectively a GitHub access token embedded in the repo.

2. Persisted credentials in JSON after encryption/decryption:
   - Signing up writes an encrypted username/password into `logindetails.json` inside the repo. While the values are encrypted with the same hard-coded key, keeping them in the repository directory is risky.

Recommended immediate actions:
- Rotate and revoke the exposed token(s) immediately (GitHub personal access tokens or OAuth apps that were used). If it’s a GitHub token, revoke it in GitHub account settings.
- Remove the hard-coded key and encrypted token from the code. Replace with environment variables (e.g., FERNET_KEY, GITHUB_TOKEN, DISCORD_APP_ID).
- Remove sensitive values from git history (use git filter-repo or BFG) and force-push the cleaned history, or create a new repository if necessary.
- Add `.env` to `.gitignore` and use python-dotenv or OS environment variables for local development.

If you want, I can:
- Create a safe patch that updates `main.py` to read secrets from environment variables and remove hard-coded values.
- Generate a `.env.example` and update `.gitignore`.
- Provide step-by-step commands to purge secrets from git history.

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