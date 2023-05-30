# OMD
Object Movement Detection

A preliminary version of the web-application was developed that allows you to configure areas in the video image in which objects defined by the user should be located, and to receive information about the disappearance of objects from the user-defined area.
A list of the key features of the development functioning:
1. Number of objects that can be recognized in one frame: 100. 
2. Recognition accuracy: 𝐴𝑃=51.4%, 𝐴𝑃_50=69.7%, 𝐴𝑃_75=55.9%.

Planned improvements: 
1. Integration with video server to view video from cameras in real time.
2. Expanding the list of tracked objects and retraining the model on the scene-generated dataset to obtain higher accuracy.
3. Developing new usage scenarios.
4. Installation of load balancing nodes and database server and migration from SQLite to Postrgres.
5. Implementing an object classifier within the same class.
6. Refining the "tracker" plugin in deepstream to track object movements.

Information for importing the YOLO model into DeepStream:
1. https://github.aiurs.co/marcoslucianops/DeepStream-Yolo
2. https://github.com/visualcortex-official/yolov7-deepstream
