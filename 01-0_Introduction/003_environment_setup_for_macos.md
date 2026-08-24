# Environment Setup for macOS

Use this guide for macOS 14 or later. Start at Step 1 and complete one step at a time. You do not need to understand every command yet.

## 1. Command-Line Tools and Homebrew Installation

Open Terminal and run:

```bash
xcode-select --install
```

After the installer finishes, run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the final Homebrew message, then open a new Terminal window. Homebrew helps macOS install programming tools.

## 2. Python, Git, and VS Code Installation

```bash
brew install python@3.12 git
brew install --cask visual-studio-code
python3.12 --version
```

The last command should show `Python 3.12`.

## 3. Course Repository Download

```bash
cd ~
git clone https://github.com/sonamu-jun/system-design-and-optimization.git
cd system-design-and-optimization
```

For later updates, use the GitHub guide: [Download and update the course files](https://github.com/sonamu-jun/system-design-and-optimization/blob/main/01-0_Introduction/004_github_download_and_update.md).

## 4. Course Environment Creation

This creates a separate Python workspace for this course. Run these commands inside the `system-design-and-optimization` folder.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 5. VS Code and Notebook Execution

Open VS Code, choose `File` then `Open Folder`, and select `system-design-and-optimization`.

In the Extensions view, install:

- Python
- Jupyter
- Pylance

Then:

1. Press `Command+Shift+P`.
2. Choose `Python: Select Interpreter`.
3. Select the interpreter ending in `.venv/bin/python`.
4. Open a course notebook and select `Select Kernel`.
5. Select the same `.venv` environment.
6. Run the first code cell.

If you cannot find `.venv/bin/python`, ask your instructor for help.
