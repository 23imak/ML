from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors


#[height,weight,show_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

#3 more classfiers
clf1 = svm.SVC()
clf2 = GaussianNB()
clf3 = neighbors.KNeighborsClassifier()

clf1 = clf1.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)

#Test Data
X_test=[[198,92,48],[184,84,44],[183,83,44],[166,47,36],[170,60,38],[172,64,39],[182,80,42],[180,80,43]]
Y_test=['male','male','male','female','female','female','male','male']

Y_prediction1 = clf1.predict(X_test)
Y_prediction2 = clf2.predict(X_test)
Y_prediction3 = clf3.predict(X_test)

prediction = clf.predict([[190,70,43]])

print ("Predicted Value by Naive Bayes is : ", Y_prediction2)
print ("Prediction by SVM is : " , accuracy_score(Y_test,Y_prediction1))
print ("Prediction by Naive Bayes is : ", accuracy_score(Y_test,Y_prediction2))
print ("Prediciton by K Neighbors : ", accuracy_score(Y_test,Y_prediction3))




