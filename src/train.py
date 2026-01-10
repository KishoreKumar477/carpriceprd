from sklearn.model_selection import train_test_split    
from sklearn.linear_model import LinearRegression
from src.logger import get_logger
logger = get_logger(__name__)
def train_model(df,test_size=0.1,random_state=42):
    logger.info("Starting model training")


    X=df.drop(['Car_Name','Selling_Price'],axis=1)
    y=df['Selling_Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    model = LinearRegression()

   
    model.fit(X_train, y_train)
    logger.info("Model training completed")
 

    return model,X_test,y_test