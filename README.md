**Machine Learning-based Phishing URL Detection System for Web Browser**
  
  Phishing link constantly evolving so it's hard to keep track the newly develop link and check in blacklist, This system solve that by predicting possible phishing site by training a model to categorize legitimate and phishing site based on their link structure.

**Prerequisites**
  
  Python (v3.12.7 or higher)
  Flask 3.1.3
  Werkzeug 3.1.8

**Installation**
  
  1. Clone or download this project into a single folder:

    Phishing Detection System/
    |- app.py
    |- phishing_dataset.csv
    |- train_model.py
    |- frontend
      |-index.html
      
  2. Create virtual machine environment:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate      # Linux/macOS
    venv\Scripts\activate         # Windows

**Deployment**
  1. Train the model with the dataset (only needed to be train once).
     `python3 train_model.py`.
     
  2. Start the flask server.
     `python3 app.py`
  
  3. Open the website UI.
     `frontend/index.html`

**Note**

  If you ever update the dataset `phishing_dataset.csv`, rerun training the model `python3 train_model.py`



  

