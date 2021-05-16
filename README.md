## Gesture Recognition using OpenCV

This is a Gesture Recognition Project. It uses Google's `mediaPipe` library for tracking Hand Movement and pyautoGUI for mouse and Keyboard controlling.

- Libraries Used:  `openCV` `mediapipe` and `pyautoGUI`
- It currently supports `3 Types` of gestures:
  * The tip of index for **Cursor Movement**.
  * Mid-point of *Tip of Index Finger* and *Tip of Middle Finger* for ***Single Click***.
  * When all *Five Fingers* are up **SPACEBAR** is pressed.
- The file [`HandTrackingModule.py`](./HandTrackingModule.py) contains all the functionalities used in this project and can be used in other Projects as well.
- Most of the part of this project is only possible because of [*Murtaza's Workshop - Robotics and AI*](https://www.youtube.com/c/MurtazasWorkshopRoboticsandAI) channel. Do check it out. He makes amazing videos on Computor Vision.


Feel free to use this code for your own projects or make pull requests on this project itself if you have any new ideas.

### To use this package. Follow these steps:
  - go to the directory in which you want to clone this project.
  - open cmd in the same directory and type ```git clone https://github.com/AlphaGamer5/Gesture_Recognition_using_OpenCV.git```.
  - after the cloning is complete, type ``` pip install -r requirements.txt```.
  - to start using the gesture, run the [```virtualMouse.py```](./virtualMouse.py) file.

**Note: If you are using a webcam, other than the one provided with the laptop, change the value of `cam` variable in [virtualMouse.py Line: 15](./virtualMouse.py).**

***Happy Learning***
