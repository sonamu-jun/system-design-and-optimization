# Environment Setup for Windows with WSL Ubuntu

Use this guide for Windows 10 version 2004 or later, or Windows 11. You will use two apps: VS Code in Windows and Ubuntu for course commands. Complete one step at a time.

## 1. WSL and Ubuntu Installation

Open PowerShell as Administrator and run:

```powershell
wsl --install -d Ubuntu-24.04
```

Restart Windows if prompted. Then open **Ubuntu** from the Start menu and create a Linux username and password. Use the Ubuntu app for the commands in the rest of this guide.

More detailed installation instructions are available in the following videos:
- WSL Installation: [Video Link](https://youtu.be/6shiT1kHUq8?si=Iex6cnc9us71eY8W)
- VS Code Installation and WSL Integration: [Video Link](https://youtu.be/zV0qxmJSSBE?si=Q0NpOxAnZW2v8a-k)

## 2. VS Code Installation on Windows

Download and install [Visual Studio Code](https://code.visualstudio.com/download).

During installation, select `Add to PATH`. Open VS Code and install the `WSL` extension from the Extensions view.

## 3. Python and Git Installation in Ubuntu

Open the Ubuntu terminal and run:

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv git
python3.12 --version
```

Type your password if Ubuntu asks for it. You will not see the password while typing; that is normal. The last command should show `Python 3.12`.

## 4. Course Repository Download in Ubuntu

```bash
cd ~
git clone https://github.com/sonamu-jun/system-design-and-optimization.git
cd system-design-and-optimization
```

For later updates, use the GitHub guide: [Download and update the course files](https://github.com/sonamu-jun/system-design-and-optimization/blob/main/01-0_Introduction/004_github_download_and_update.md).

## 5. Course Environment Creation

This creates a separate Python workspace for this course. Run these commands inside the `system-design-and-optimization` folder.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 6. Repository Access through WSL

Run this command in the Ubuntu terminal:

```bash
code .
```

Confirm that the lower-left corner of VS Code says **WSL**. In that VS Code window, install:

- Python
- Jupyter
- Pylance

## 7. Notebook Execution

1. Press `Ctrl+Shift+P`.
2. Choose `Python: Select Interpreter`.
3. Select the interpreter ending in `.venv/bin/python`.
4. Open a course notebook and select `Select Kernel`.
5. Select the same `.venv` environment.
6. Run the first code cell.

If `code .` does not open VS Code, ask your instructor for help.
