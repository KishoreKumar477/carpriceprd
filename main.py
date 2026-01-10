from src.config_loader import load_config
from src.data_loader import load_data
from src.preprocessing import encode_features
from src.train import train_model
from src.evaluate import evaluate
from src.predict import predict_price
from src.logger import get_logger

logger = get_logger(__name__)

logger.info("Application started")


config=load_config()
df = load_data(config["data"]["path"])
df = encode_features(df)

model, X_test, y_test = train_model(df,test_size=config["train"]["test_size"],random_state=config["train"]["random_state"])
r2 = evaluate(model, X_test, y_test)
# prediction. 
print(predict_price(model,{
    'Year': 2018,
    'Present_Price': 6.5,
    'Kms_Driven': 35000,
    'Fuel_Type': 0,
    'Seller_Type': 1,
    'Transmission': 0,
    'Owner': 0
}))

print("Test R²:", r2)
