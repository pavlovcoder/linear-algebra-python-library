from sklearn.model_selection import train_test_split
# [...]
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2)

t0 = time()
< your clf.fit() line of code >
print "training time:", round(time()-t0, 3), "s"