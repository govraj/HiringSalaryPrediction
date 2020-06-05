# HiringSalaryPrediction
This is machine learning web application which predict hiring salary on the basis of three crieteria experience score, test_score, interview_score. This is linear regression based model.

# Requirement to run
1. python 3.7
2. Spyder or any IDE
3. Flask (mini-webframwork for web app)
4. sklearn (to train model)
5. pickle(to save model)

# About Code files
1. style/css:- contain style.css for website design
2. template/index.html is web form in which we pass value
3. model.py:- read hiring.csv with pandas and get feature from datafram and predict salary with sklearn.linear_model() and dump the model locally as .pkl file.
4. model.pkl:- it is traind model which will use by web app to predict salary
5. app.py:- it is flask web app code file in which we read model.pkl and show prediction.
6. hiring.csv:- it is csv file with raw data which we used for train the model.

columns: experiece,test_score,interview_score,salary
