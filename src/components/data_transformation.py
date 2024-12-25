from src.entity.config_entity import DataTransformationConfig
from src.exceptions.expection import CustomException
from src.logger.custom_logging import logger
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import sys
import numpy as np
from src.utils.utlis import *

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def create_preprocessor(self):
        try:
            logger.info('Creating data transformation pipeline')

            num_col=['Age', 'Fare','Pclass','SibSp','Parch']
            cat_col=['Sex','Embarked']

            
            preprocessor = ColumnTransformer(
            transformers=[
            ('num', StandardScaler(), num_col),  
            ('cat', OrdinalEncoder(), cat_col)  
            ])

            return preprocessor

        except Exception as e:
            logger.error(f"Error in creating data transformation pipeline: {str(e)}")
            raise CustomException(e, sys)

    def transform_data(self):
        train_path=self.config.train_file_path
        test_path=self.config.test_file_path
        
        try:
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)

            target_column = 'Survived'
            drop_columns = [target_column, 'Name', 'PassengerId', 'Ticket', 'Cabin']

            

            logger.info("Filling missing values for 'Fare' column grouped by 'Pclass'")
            train_data['Fare'] = train_data.groupby('Pclass')['Fare'].transform(lambda x: x.fillna(x.median()))
            test_data['Fare'] = test_data.groupby('Pclass')['Fare'].transform(lambda x: x.fillna(x.median()))

            logger.info("Filling missing values for 'Age' column grouped by 'Pclass' and 'Sex'")
            train_data['Age'] = train_data.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median()))
            test_data['Age'] = test_data.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median()))

            preprocessor=self.create_preprocessor()
            input_feature_train_data = train_data.drop(columns=drop_columns)
            target_feature_train_data = train_data[target_column]
            input_feature_test_data = test_data.drop(columns=drop_columns)
            target_feature_test_data = test_data[target_column]

            input_train_arr=preprocessor.fit_transform(input_feature_train_data)
            input_test_arr=preprocessor.transform(input_feature_test_data)

            train_array=np.c_[input_train_arr, target_feature_train_data.values.reshape(-1, 1)]
            test_array=np.c_[input_test_arr, target_feature_test_data.values.reshape(-1, 1)]

            save_obj(file_path=self.config.preprocessor_obj,obj=preprocessor)

            train_df = pd.DataFrame(train_array)
            test_df = pd.DataFrame(test_array)

            train_df.to_csv(self.config.save_train_path, index=False,header=True)
            test_df.to_csv(self.config.save_test_path, index=False,header=True)


        except Exception as e:  
            raise CustomException(e, sys)    
    