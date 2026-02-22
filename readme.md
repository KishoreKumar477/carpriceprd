# 🚗 Car Price Prediction ML Project

This project predicts the selling price of a car using Machine Learning.

## 📂 Project Structure

carpriceprd/
│
├── src/
│   ├── config_loader.py      # Loads configuration
│   ├── data_loader.py        # Loads dataset
│   ├── preprocessing.py      # Feature encoding
│   ├── train.py              # Model training
│   ├── evaluate.py           # Model evaluation
│   ├── predict.py            # Prediction logic
│   └── logger.py             # Logging setup
│
├── app.py                    # Streamlit Web App
├── main.py                   # Pipeline entry point
├── config.yaml               # Configuration file
├── car data.csv              # Dataset
├── model.pkl                 # Trained model
├── requirements.txt          # Dependencies
└── README.md

## 📸 Web Application Preview

<p align="center">
  <img src="webapp.png" width="850">
</p>

## ⚙️ How to Run
## clone to use
git clone https://github.com/KishoreKumar477/carpriceprd.git
cd carpriceprd
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
