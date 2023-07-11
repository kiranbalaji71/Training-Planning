import numpy as np
from sklearn import metrics
from nltk.translate.bleu_score import sentence_bleu
from nltk.metrics import edit_distance

B = 'bird'
C = 'cat'
D = 'dog'

x_test = [B,B,B,B,B,B, C,C,C,C,C,C, D,D,D,D,D,D]
x_pred = [B,B,B,B,C,D, C,C,C,D,D,B, B,B,C,C,C,C]

print("confusion matrix")
print(metrics.confusion_matrix(x_test, x_pred))
print(metrics.classification_report(x_test, x_pred))

y_test = np.array([1,0,0,1,1,1])
y_pred = np.array([0,0,1,1,1,0])

print('Precision :', metrics.precision_score(y_test,y_pred))
print('Recall :', metrics.recall_score(y_test,y_pred))
print('f1_score :', metrics.f1_score(y_test,y_pred))

y_pred_prob = np.array([0.7,0.5,0.2,0.4,0.3,0.6]) 

print('ROC_AUC :', metrics.roc_auc_score(y_test,y_pred_prob))
print('PRC :',metrics.average_precision_score(y_test,y_pred_prob))


reference = [['A','love','cats']]
candidate = ['I','like','dogs']
print('BLEU Score :', sentence_bleu(reference,candidate))

gtvalue = 'this is a cat'
probvalue = 'this is a dog'
print('Character error :', edit_distance(gtvalue,probvalue)/len(gtvalue))

gtword = gtvalue.split()
probword = probvalue.split()
print('Word error :', edit_distance(gtword,probword)/len(gtword))