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
   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/your-username/titanic-survival-prediction.git
   </code></div></div></pre>
2. Install dependencies:
   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
   </code></div></div></pre>
3. Run the Streamlit app:
   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">streamlit run app.py</code></div></div></pre>


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
