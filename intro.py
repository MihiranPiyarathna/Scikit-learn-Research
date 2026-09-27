# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(random_state=0) # supervised
# X = [[ 1,  2,  3],  # 2 samples, 3 features
#      [11, 12, 13]]
# y = [0, 1]  # gt classes (labels) assigned to each sample
# clf.fit(X, y)
# out = clf.predict([[4, 5, 6], [14, 15, 16]])  # predict classes of new data
# print(out)

from sklearn.preprocessing import StandardScaler
X = [[0, 15],
     [1, -10]]
# scale data according to computed scaling values
out = StandardScaler().fit(X).transform(X)
print(out)