# ISW Registration Script

Running (steps 2 to 4 are only for the first time)

1. Go into the 'isw-registration-script' directory on the terminal.

        cd isw-registration-script

2. Check if python version 2.7 is installed, by running `python`.
  - If python 2.7.x shows up, then go to step 4.
  - If any other versions or python is not installed, go to step 3.

3. Install the latest stable version of 2.7.x by going to https://www.python.org/downloads/.
  - You can use virtualenv (https://virtualenv.pypa.io/en/latest/installation.html), if you prefer to install python 2.7.x locally instead of globally (optionally)
  
4. Install `csvkit`

        pip install csvkit

5. Run the script and go to `localhost:8080` (Double check the url listed after running the command below)

        python isw.py
