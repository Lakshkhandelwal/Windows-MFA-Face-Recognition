# Windows MFA Based on Face-Recognition
A Windows 10 Dual Factor Authentication Tool based on ML that runs continuously and locks the system if user has left the machine unattended

## Instructions for direct execution without python or any other dependency installed.
1. Download or Clone the repository.
2. Open the "exeFile" folder.
3. Execute the "program.exe"
4. Use the Options in order

    i) Capture Your Face 

    ii) Train program to detect faces

    iii) Start Windows Lock
    
![Image of programexe](https://raw.githubusercontent.com/Lakshkhandelwal/Windows-MFA-Face-Recognition/master/Images/program.png)
  
5. This will start the program and the lock mechanism, as soon as the program stops detecting your face it will lock the Screen in 5        Seconds.

Caution : Do not rename the input file or exe file.

## Instructions for executing the program on Python 2.7 Version.
1. Download or Clone the repository.
2. The program is dependent on the [numpy](https://pypi.org/project/numpy/), [pillow](https://pypi.org/project/Pillow/) and [openCV](https://opencv.org/) libraries.
3. Execute the program from cmd or IDLE or your preferred method.

  `Command - python program.py`
  
  ![Image of cmd](https://raw.githubusercontent.com/Lakshkhandelwal/Windows-MFA-Face-Recognition/master/Images/python.png)
    
4. Use the steps as described above to train and start the program and the lock mechanism.

#### Demo Video Link
[Linkedin Link](https://www.linkedin.com/in/laksh-khandelwal/)


## LICENSE
This repository is licensed under the MIT License - see the LICENSE file for details.
