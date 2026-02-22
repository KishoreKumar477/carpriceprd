# 🚗 Car Price Prediction ML Project

This project predicts the selling price of a car using Machine Learning.

## 📂 Project Structure

carpriceprd/
│
├── src/
│   ├── config_loader.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── logger.py
│
├── app.py               # Streamlit Web App
├── main.py              # Pipeline entry point
├── config.yaml          # Configuration file
├── car data.csv         # Dataset
├── model.pkl            # Trained model
├── requirements.txt
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
