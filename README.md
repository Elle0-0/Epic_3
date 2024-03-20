# EPIC – Block 3 <br /><br /><sup>Performing Prescriptive Analysis for Societal Impact</sup>

<br />

### Project Overview
The aim of this project is to leverage analytical techniques to extract valuable insights from our chosen datasets, 
with a focus on addressing societal concerns. For our project, we are analysing CO<sub>2</sub> levels in the atmosphere and surface
temperatures for a significant number of countries across the globe.<br /><br />
By applying a systematic Data Science Workflow, we aim to thoroughly explore and understand the various intricacies of our
datasets, allowing us to develop and create predictive machine learning models that can provide prescriptive solutions to 
the continuing global concern of rising temperatures, global warming, climate change, and CO<sub>2</sub> emissions.

<br />

### Project Setup Guide

Follow the steps below to setup the project. After the steps are complete, you will be able to
run any Python or Jupyter Notebook files inside the ``src`` folder.

<br />

#### Step 1. Cloning the Repository
>  Navigate to a suitable directory on your machine and clone the repository as shown below, then 
>  switch to this new directory, whose name is ``Epic_3`` (unless you specify otherwise).
>  ```
>  ~ > cd projects
>  ~/projects > git clone https://github.com/Elle0-0/Epic_3.git
>  ~/projects > cd ./Epic_3
>  ~/projects/Epic_3 (main) > 
>  ```

<br />

#### Step 2. Installing Project Dependencies
>  Use the appropriate setup script for your machine, stored in the ``setup`` folder. 
>  These scripts are designed to handle the creation and activation of a Python virtual environment,
>  and automatically install the project requirements.
>
>  Windows (cmd)
>  ```
>  ~/projects/Epic_3 (main) > .\setup\setup.bat
>  ```
>  Windows (Powershell)
>  ```
>  ~/projects/Epic_3 (main) > ./setup/setup.ps1
>  ```
>  Linux (bash)
>  ```
>  ~/projects/Epic_3 (main) > source ./setup/setup.sh
>  ```

<br />


### Project Execution Guide (Terminal)

Follow the relevant steps below to execute the Python or Jupyter Notebook files.
If you have an Integrated Development Evironment (IDE), you may already have this functionality
built in; in which case, you can ignore the steps below. These steps are intended for those
operating from a terminal, such as Windows' `cmd`. 

<br />

#### Executing Python Files
>  If you want to run ``.py`` files, like ``src/preprocessing/main.py``, for example,
>  navigate to the ``src`` directory, and type the command as shown below.
> 
>  Windows (cmd / Powershell) & Linux (bash)
>  ```
>  ~/projects/Epic_3 (main) > cd src
>  ~/projects/Epic_3/src (main) > python ./preprocessing/main.py
>  ```
> 
>  If the "python" command is not recognised try "python3" or "py" instead.
>  If this issue persists, try troubleshooting the issue using the official [Python documentation](https://docs.python.org/3/using/cmdline.html).

<br />

#### Executing Jupyter Notebook Files
>  If you want to run ``.ipynb`` files, like ``src/models/linear_regression.ipynb``, for example,
>  navigate to the ``src`` directory, and type the command as shown below.
> 
>  Windows (cmd / Powershell) & Linux (bash)
>  ```
>  ~/projects/Epic_3 (main) > cd src
>  ~/projects/Epic_3/src (main) > jupyter notebook ./models/linear_regression.ipynb
>  ```
> 
>  This should automatically open a new interactive notebook tab in your browser, where you
>  can begin executing the code cells.

If you are having issues with navigation or specifying files for execution for either of the guides above,
try switching the forward slashes with backslashes.

<br />
