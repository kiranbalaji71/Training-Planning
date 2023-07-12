import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv('./csv file/ex-metrics.csv')
x = df.iloc[:,2:-1].values
y = df.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(x, y)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

print(metrics.classification_report(y_test, y_pred, zero_division=0))

print('Confusion matrix')
print(metrics.confusion_matrix(y_test,y_pred))

print('Cohen kappa score :',metrics.cohen_kappa_score(y_test,y_pred))

precision, recall, thresholds = metrics.precision_recall_curve(y_test, y_pred)
print('precision :',precision)
print('recall :', recall)
print('thresholds :', thresholds)
