#  Loan Prediction App

A machine learning web application that predicts whether a loan application will be Approved or Rejected based on applicant financial and demographic information, built with Streamlit** and XGBoost Classifier.

The primary focus of the model is accurately evaluating loan approval outcomes using financial indicators, credit scores, and asset information.

🔗 **Live Demo:** https://myloanpredictionapp.streamlit.app/


#  Model Performance

## Overall Metrics

| Metric                 | Score  |
| ---------------------- | ------ |
| Accuracy               | 0.9794 |
| Macro Avg Precision    | 0.9774 |
| Macro Avg Recall       | 0.9792 |
| Macro Avg F1-Score     | 0.9783 |
| Weighted Avg Precision | 0.9795 |
| Weighted Avg Recall    | 0.9794 |
| Weighted Avg F1-Score  | 0.9794 |



## Classification Report

| Class    | Precision | Recall | F1-Score | Support |
| -------- | --------- | ------ | -------- | ------- |
| Approved | 0.9862    | 0.9802 | 0.9832   | 657     |
| Rejected | 0.9687    | 0.9781 | 0.9734   | 411     |

> The model demonstrates excellent performance in predicting loan approval outcomes using applicant income, loan details, credit score, and asset-related features.
> Precision, Recall, and F1-Score are used as the primary evaluation metrics for loan classification effectiveness.



##  Model Details

* Algorithm: XGBoost Classifier (`XGBClassifier`)

* Preprocessing: Feature transformation pipeline

* Input Features:

  * Number of Dependents
  * Education Level
  * Self Employment Status
  * Annual Income
  * Loan Amount
  * Loan Term
  * CIBIL Score
  * Residential Asset Value
  * Commercial Asset Value
  * Luxury Asset Value
  * Bank Asset Value

* Output: Predicted loan status

  * Approved
  * Rejected

* Evaluation Metrics:

  * Precision
  * Recall
  * F1-Score
  * Accuracy

### 1. Clone the repository


git clone https://github.com/thePython2016/loanPredictionApp.git
cd loanPredictionApp


### 2. Install dependencies

pip install -r requirements.txt


### 3. Run the app

streamlit run app.py


##  Sample Data

Use the provided sample_data.csv to test the app format.

| no_of_dependents | education    | self_employed | income_annum | loan_amount | loan_term | cibil_score | loanstatus |
| ---------------- | ------------ | ------------- | ------------ | ----------- | --------- | ----------- | ---------- |
| 2                | Graduate     | No            | 9600000      | 29900000    | 12        | 778         | Approved   |
| 0                | Not Graduate | Yes           | 4100000      | 12200000    | 8         | 417         | Rejected   |




This project is open source and available under the MIT License.
