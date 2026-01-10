from sklearn.metrics import r2_score 
import matplotlib.pyplot as plt

def evaluate(model,X_test,y_test):
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Selling Price")
    plt.ylabel("Predicted Selling Price")
    plt.title("Actual vs Predicted Selling Price")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
    plt.show()
    
    return r2   