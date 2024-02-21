# Using EnergyPlus Wheel

EnergyPlus has traditionally been packaged up using desktop install wizards and scripts, most recently with the Qt install framework.
Users have requested an easier install experience, and with the growing popularity of the Python API, we are pushing toward a Python-centric distribution option.
The actual form is still being worked out, but we are starting to put wheels on test-pypi.
These should not be trusted to remain there for any given amount of time, and will break without notice.

# Using This Demo

This repository is a demonstration of using the new EnergyPlus wheel approach.
If you are using an IDE, you are likely able to just clone the repo, install reqs, and run the main.py script using IDE tools directly.
If not, the commands are still super simple (I'm assuming a Unix-like shell and Python install):
 - Clone this repository: `git clone https://github.com/Myoldmopar/UseEnergyPlusWheel`
 - Change into that directory: `cd UseEnergyPlusWheel`
 - Set up a Python virtual environment: `python -m venv venv`
 - Activate this virtual environment: `. ./venv/bin/activate`
 - Install the EnergyPlus Wheel: `pip install -r requirements.txt`
 - Run the main script: `python main.py`

You should see a progress bar going across in the terminal, which is showing progress during the simulation run.

# Testing

As of right now the wheel has only been tested on Linux, but it looks like it should already be working on Mac.
I will employ minimal little GitHub Action workflows to do basic exercising here.
