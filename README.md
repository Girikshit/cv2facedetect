# cv2facedetect
A face recognition program using OpenCV and DeepFace.

The program is a modified version of NeuralNine's face recognition program.
His program uses DeepFace to compare the camera feed at regular intervals against a reference face and displays "Match" on the screen if they match.

This modified version is suitable for lower end devices as it prevents the CPU from being bombarded with comparisons after each iteration (a DeepFace comparison can be quite CPU intensive).
This version implements threading to prevent a comparison from being made if another comparison(thread) is still ongoing. 

Reference: NeuralNine - Live Face Recognition in Python (https://www.youtube.com/watch?v=pQvkoaevVMk)
