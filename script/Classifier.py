from sklearn import tree

clf = tree.DecisionTreeClassifier()

# [No Of Hours Remaining For Exam, Study Hour]
X = [[24, 10], [100, 30], [200, 50], [20, 5],
     [48, 15], [24, 7],
     [50, 11], [5, 1], [24, 2], [24, 3],[100, 5],[48, 4],[200, 20],[100, 10],[50,7],[60, 8],[10, 1],[10,4],[20,7],[30,7]]

Y = ['pass', 'pass', 'pass', 'pass', 'pass', 'pass', 'pass','pass','fail', 'fail','fail','fail','fail','fail','fail','fail','fail','pass','pass','pass']


#train the model/fit

clf = clf.fit(X, Y)

x=[[50,15]]

#Predict the Example

prediction = clf.predict(x)

print(prediction)

print(x)
