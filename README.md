**Machine Learning-based Phishing URL Detection System for Web Browser**
  
  Phishing link constantly evolving so it's hard to keep track the newly develop link and check in blacklist, This system solve that by predicting possible phishing site by training a model to categorize legitimate and phishing site based on their link structure.

**Prerequisites**
  
  Python (v3.12.7 or higher)
  Flask 3.1.3
  Werkzeug 3.1.8

**Installation**

  Install all file in one folder.

  /Phishing Detection System
  - app.py
  - phishing_dataset.csv
  - train_model.py
  - index.html

**Deployment**

  To start you have to train the model first by running the command `python3 train_model.py` and generate the trained model `phishing_model.pkl`, to deploy command `python3 app.py` to run the server. Open `index.html`.



  

