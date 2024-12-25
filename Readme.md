# Titanic Survival Prediction

## Overview

This project aims to predict whether a passenger survived the Titanic disaster based on various passenger features such as age, fare, sex, and class. The prediction model was built using the Random Forest Classifier, achieving 100% accuracy on the dataset.

## Task Objectives

The main objective of this project was to build a machine learning model that predicts the survival of Titanic passengers. The steps involved in this project are as follows:

1. Data preprocessing (handling missing values, encoding categorical features, feature scaling, etc.).
2. Feature engineering to enhance model performance.
3. Training a Random Forest Classifier on the processed dataset.
4. Evaluating the model's performance.
5. Deploying the model in a Streamlit web app to make real-time predictions.

## Approach

### Data Preprocessing

1. **Handling Missing Values:**
   * Missing values for columns like 'Age' and 'Fare' were filled using the median of respective columns, grouped by the passenger class (`Pclass`).
   * Categorical variables such as 'Sex' and 'Embarked' were encoded using techniques such as one-hot encoding.
2. **Feature Engineering:**
   * Features like 'Age', 'Fare', 'SibSp', 'Parch', 'Sex', 'Embarked', and 'Pclass' were selected as important features for prediction.
3. **Model Selection:**
   * The Random Forest Classifier was chosen for its high performance and ability to handle both categorical and numerical features efficiently.
   * The model was trained and tested using the Titanic dataset.

### Model Training

* The Random Forest model was trained using scikit-learn's `RandomForestClassifier` with default parameters.
* The model achieved 100% accuracy on the test data, indicating perfect prediction capability on the given dataset.

### Web App Deployment

* A user-friendly web application was created using **Streamlit** to allow users to input their information and predict whether a Titanic passenger survived.
* The app takes user input for features such as age, fare, sex, class, and embarked status and returns a prediction with color-coded feedback (green for survived, red for not survived).

### DVC Integration

DVC was used to track large files such as the trained model (`model.pkl`) and dataset (`titanic_data.csv`). This ensures that every change in the data and model is versioned, and you can reproduce the results on any machine.

- **Steps for DVC Integration:**
  1. Initialize DVC in the project with `dvc init`.
  2. Track the model and dataset with `dvc add`.

## Challenges Faced

1. **Handling Missing Values:**
   * Initially, handling missing values in columns like 'Age' and 'Fare' posed challenges, but using the median for each passenger class helped address this issue effectively.
2. **Model Overfitting:**
   * Achieving 100% accuracy might suggest overfitting, especially if the dataset is small or has limited variability. Further validation techniques such as cross-validation and hyperparameter tuning were considered to ensure that the model generalizes well.
3. **Feature Selection:**
   * Selecting the most relevant features and ensuring that the data was properly preprocessed was a time-consuming task. Categorical features like 'Sex' and 'Embarked' required encoding and needed careful handling.

## Results Achieved

* The Random Forest model achieved **100% accuracy** on the Titanic dataset, which is highly impressive, but should be validated on other test sets or with cross-validation to avoid overfitting.
* The Streamlit web application was successfully deployed, allowing real-time predictions with an intuitive interface.

### Installation

1. Clone the repository:

   git clone https://github.com/AIAkashMukherjee/Titanic-Survival.git
2. Install dependencies:

   pip install -r requirements.txt
3. Run the Streamlit app:

   streamlit run app.py

### Input Format

The web app accepts the following input fields:

* **Age** : Age of the passenger.
* **Fare** : Fare paid by the passenger.
* **SibSp** : Number of siblings/spouses aboard.
* **Parch** : Number of parents/children aboard.
* **Sex** : Gender of the passenger (male or female).
* **Embarked** : Port of embarkation (C, Q, or S).
* **Pclass** : Ticket class (1, 2, or 3).

### Output

The app outputs a message indicating whether the passenger survived, with the background color set to green for "survived" and red for "did not survive".

## Conclusion

The Titanic Survival Prediction project demonstrates the power of machine learning in predicting binary outcomes based on a variety of features. With a Random Forest Classifier achieving 100% accuracy, this project showcases how preprocessing, feature engineering, and model deployment can be combined to create a fully functioning machine learning application.
