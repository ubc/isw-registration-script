# ISW Registration Script

## OSX or Linux

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

## Windows

New Install (Windows)

Step 1: Install Python

* Download from python.org/downloads (last tested with 2.7.11)
* Install from download. If version 2.x, install location should be c:\python27 
* Add python path to system path
  * Control Panel > System and Security > System
  * Advanced System Settings > Environment Variables
  * System Variables > Path > Edit..
  * Add the following: ;c:\python27\
  * Hit OK three times
* Install 'csvkit'
  * at the Command line:
*       pip install csvkit

Step 2: Copy ISW-registraiton-script folder

* Recommend: save entire directory in c:\

Step 3: Running the Python server and Loading the User Interface

1. From Terminal or Windows Command line:  Go into the 'isw-registration-script' directory

        cd isw-registration-script

2. Run the script:

        python isw.py

3. Open your favorite web browser and go to ((Double check the url listed after running the command below)):

        localhost:8080
