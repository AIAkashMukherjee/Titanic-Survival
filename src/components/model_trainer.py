
from src.entity.config_entity import ModelTrainerConfig
from src.logger.custom_logging import logger
import sys,joblib
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src.utils.utlis import *
from src.exceptions.expection import CustomException


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    @staticmethod
    def save_model(path: Path, model: BaseEstimator):
        """Save the trained model to the specified path."""
        try:
            joblib.dump(model, path)
            print(f"Model saved at {path}")
        except Exception as e:
            print(f"Error saving model: {e}")
            logger.error(f"Error saving model: {e}")
            raise CustomException(e, sys)      


    
    def train(self):
        train_data=pd.read_csv(self.config.training_data_path)
        test_data=pd.read_csv(self.config.testing_data_path)
        try:
            X_train = train_data.iloc[:, :-1].values
            y_train = train_data.iloc[:, -1].values
            X_test = test_data.iloc[:, :-1].values
            y_test = test_data.iloc[:, -1].values   

            model = RandomForestClassifier()
            
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            test_model_score = accuracy_score(y_test, y_pred)

            print(f"Test model score: {test_model_score}")

            # Save the best model
            self.save_model(path=self.config.train_model_path,model=model)
        except Exception as e:
            logger.error(f'Error occurred: {e}')
            raise CustomException(e, sys)