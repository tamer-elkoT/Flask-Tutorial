# Installation & Setup

1. Open the Terminal in VS Code
Launch VS Code.

Open your project folder (or create a new one).

Open the integrated terminal by pressing Ctrl + ` (backtick) or going to Terminal > New Terminal.

2. Create the Conda Environment
In your terminal, run the following command. We will specify Python 3.11 for this environment to ensure stability with most Flask extensions, but you can swap it for python=3.13 if you prefer.

Bash
conda create --name flask_env python=3.11
--name flask_env: This sets the name of your environment.

python=3.11: This tells Conda exactly which version to install.

3. Activate the Environment
Once the installation finishes, activate the environment so your terminal uses this specific Python instance:

Bash
conda activate flask_env
You should now see (flask_env) prepended to your terminal prompt.

4. Install Flask
With the environment active, install Flask using pip (which is the standard for web libraries even inside Conda):

Bash
pip install flask
5. Connect VS Code to the Environment
This is a crucial step to ensure VS Code’s IntelliSense and debugging tools know which Python version you are using.

Press Ctrl + Shift + P to open the Command Palette.

Type "Python: Select Interpreter" and select it.

Look for the entry that says Python 3.11.x ('flask_env': conda).

Select it. You will see the environment name appear in the bottom-right corner of the VS Code status bar.

