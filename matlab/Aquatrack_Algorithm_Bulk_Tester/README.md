# AquaTrack Algorithm Bulk Tester

This program used Matlab, Blender, and Python to test all proposed algorithms with one set of data for direct comparison

#Prerequisite steps for linking Matlab and Python with OpenCV functionality:

1) Install a clean version of python, it should NOT be through a 3rd party (ex. Anaconda). I am using 3.11.0 https://www.python.org/downloads/release/python-3110/

2) Install OpenCV and imutils via the CMD prompt (Make sure that your path or virtual enviornment is using the right python version first)
 ` pip install opencv-python`  
 ` pip install imutils`

3) Run one of the algorithm scripts from the python team to verify opencv was properly installed. I have been using the following script from Ethan: https://discordapp.com/channels/1339009595288326206/1346979811331149886/1354566300436791407
`python ball_tracking.py --video Green_Ball.mp4 `

4) Make sure you have the right version of Matlab (R2024a)

5) Open Matlab and set the python environment to the clean installation (https://www.mathworks.com/help/matlab/matlab_external/install-supported-python-implementation.html)
`pyenv    %Check to see what versions (if any) Matlab is connected to` 

   If it is not showing 3.11.0, use the following command to set it

`pyenv(Version="PATH_TO_python.exe")`

6) Use the following command to open python file (Remember to check the Matlab environment path is correct) (https://www.mathworks.com/help/matlab/ref/pyrunfile.html)
`pyrunfile("ball_tracking.py --video Green_Ball.mp4")`

If this does not work, you may need to install one or all of the following add-ons:
 - Computer Vision Toolbox 
 - MATLAB Support for MinGW-w64 C/C++/Fortran Compiler
 
#Steps to run the testing app

1) Open Blender and launch the tennis court (Make sure it is the most recent one by the Blender Team)

2) Load the Blender - Matlab Script provided by the professor, and run the script

3) Open the app in Matlab, and run the app.

4) Configure any settings you wish to modify

5) Start the Server in Blender

6) Press the Run Selection for one specified file, or the run all selected for all of selected play type. If you are running all, or a
   increased framerate, you will have some time on your hands while it runs. The light will turn green when complete.
   
7) Once run is complete, save the data (generating .dat files is the next TODO item), then stop the Blender server. If you wish to run again,
   simply repeat steps 5 and 6.