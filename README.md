# [flask tip] to run 2 flask app dual
```shell
$ export FLASK_APP=appGUI.py
$ flask run --host 0.0.0.0 --port 5001
```
# ano-webGUI
this is GUI front-end of our repo [futureframes for abnormal detection](https://github.com/deathvn/anopred-futureframe.git)   
to run this GUI app, follow below comand.
```shel
python appGUI.py
```
open the link appear on browser, the home screen will be like this:  
![homescreen](assets/homeapp.png)
Choose model, and data, after that, click Run button, the result will be appear like this:  
Video output: red-retangle frame is abnormal, yellow dot is where abnormal events  
![videoout](assets/videooutput.png)
Score graph: score/frames of each video  
![score](assets/scoregraph.png)
ROC curve: the ROC curve, and AUC metric  
![auc](assets/roccurve.png)
