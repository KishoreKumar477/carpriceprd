import pandas as pd
from src.logger import get_logger
logger= get_logger(__name__)
def predict_price(model,input_dic):
     try:
        logger.info(f"Prediction request received: {input_dic}")
        df=pd.DataFrame([input_dic])
        predictions = model.predict(df)
        logger.info(f"Prediction made successfully: {predictions[0]}")  
        return predictions[0]
     except Exception as e:
         logger.error(f"Error making predictions(failed): {e}",exc_info=True)
         return None