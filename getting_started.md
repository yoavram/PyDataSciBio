# Getting Started: Python & Data Science for Biologists

Please complete **all steps below before the first class**. It should take about 15–20 minutes. Bring your laptop even if something doesn't work — we'll troubleshoot together.

---

## Step 1: Install Python

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the **latest stable version** (3.11 or newer).
2. Run the installer.
   - **Windows:** On the first screen, check **"Add Python to PATH"** before clicking Install. This is easy to miss — don't skip it.
   - **Mac:** Follow the installer prompts.
3. Verify the installation by opening a terminal and running:
   ```
   python --version
   ```
   You should see something like `Python 3.12.x`.

---

## Step 2: Install Visual Studio Code

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
2. Run the installer and follow the default prompts.
3. Open VS Code when installation is complete.

---

## Step 3: Install Required Extensions

Inside VS Code, click the **Extensions** icon in the left sidebar (four squares icon) and search for and install each of the following:

| Extension | Publisher |
|---|---|
| **Python** | Microsoft |
| **Jupyter** | Microsoft |
| **GitHub Copilot Chat** | GitHub |

---

## Step 4: Sign In to GitHub Copilot

1. After installing the Copilot extension, click the **Copilot icon** in the bottom status bar (or a sign-in prompt will appear automatically).
2. Select **Sign in to GitHub**. If you don't have a GitHub account, create a free one at [github.com](https://github.com) — it only takes a minute.
3. A browser window will open — sign in and authorize VS Code when prompted.
4. Return to VS Code. The Copilot icon in the status bar should show as active.

> **Test it:** Open any `.py` file, type a comment like `# Function to say hello`, press Enter, and wait a moment. Copilot should suggest code in gray — press **Tab** to accept.

---

## Step 5: Set Up Your Course Project Folder

1. Create a folder on your computer for this course, e.g., `python-bio-course`.
2. In VS Code, go to **File → Open Folder** and select that folder.
3. Open the integrated terminal with **Ctrl + `** (Windows/Linux) or **Ctrl + `** (Mac).
4. Create a virtual environment:
   ```
   python -m venv .venv
   ```
5. Activate it:
   - **Windows:** `.\.venv\Scripts\activate`
   - **Mac/Linux:** `source .venv/bin/activate`

   Your terminal prompt should now start with `(.venv)`.
6. Install NumPy:
   ```
   pip install numpy
   ```

---

## Step 6: Test Your Jupyter Notebook Setup

1. Create a new file in your course folder named `test.ipynb`.
2. In the **top-right corner** of the editor, click **Select Kernel → Python Environments** and select `.venv`.
3. If prompted to install `ipykernel`, click **Install**.
4. In the first cell, type `import numpy as np` and press **Shift + Enter**.

No errors? You're all set — see you in class!

---

## Quick Checklist

- [ ] Python installed and working in the terminal
- [ ] VS Code installed
- [ ] Python, Jupyter, and GitHub Copilot extensions installed
- [ ] Signed in to Copilot in VS Code
- [ ] Course folder created with `.venv` activated and NumPy installed
- [ ] Jupyter notebook runs successfully
