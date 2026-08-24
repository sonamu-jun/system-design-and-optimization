# Environment Setup for Linux

Use this guide for Ubuntu 24.04. Start at Step 1 and complete one step at a time. You do not need to understand every command yet.

## 1. Python, Git, and VS Code Installation

Open Terminal and run:

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv git
sudo snap install code --classic
python3.12 --version
```

Type your password if Ubuntu asks for it. You will not see the password while typing; that is normal. The last command should show `Python 3.12`.

## 2. Course Repository Download

```bash
cd ~
git clone https://github.com/sonamu-jun/system-design-and-optimization.git
cd system-design-and-optimization
```

For later updates, use the GitHub guide: [Download and update the course files](https://github.com/sonamu-jun/system-design-and-optimization/blob/main/01-0_Introduction/004_github_download_and_update.md).

## 3. Course Environment Creation

This creates a separate Python workspace for this course. Run these commands inside the `system-design-and-optimization` folder.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4. VS Code Workspace

```bash
code .
```

When VS Code opens, install these three extensions from the Extensions view:

- Python
- Jupyter
- Pylance

## 5. Notebook Execution

1. Press `Ctrl+Shift+P`.
2. Choose `Python: Select Interpreter`.
3. Select the interpreter ending in `.venv/bin/python`.
4. Open a course notebook and select `Select Kernel`.
5. Select the same `.venv` environment.
6. Run the first code cell.

If you cannot find `.venv/bin/python`, ask your instructor for help.
