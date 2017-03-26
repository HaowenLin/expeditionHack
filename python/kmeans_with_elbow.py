from sklearn import cluster
from sklearn import linear_model
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

'''
X = [[0,1,2,3],[0,2,2,3],[0,1,4,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3],[10,1,2,3],[10,1,2,3],[10,1,2,3]]



k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X)
print(k_means.labels_[:])
print(k_means.cluster_centers_)
#print(k_means.fit_transform(X))
'''

# Predict Total Consumption of 2017-2018

#YY = [[2000,7850000],[2001,8220000],[2002,8550000],[2003,9225000],[2004,9325000],[2005,9700000],[2006,9025000],[2007,9150000],[2008,10750000],[2009,10900000],[2010,11900000],[2011,10200000],[2012,11300000],[2013,11700000],[2014,13250000]]
XX = [[2001],[2002],[2003],[2004],[2005],[2006],[2007],[2008],[2009],[2010],[2011],[2012],[2013],[2014],[2015],[2016]]
YY =  [[7850000],[8220000],[8550000],[9225000],[9325000],[9700000],[9025000],[9150000],[10750000],[10900000],[11900000],[10200000],[11300000],[11700000],[13250000],[13000000]]
reg = linear_model.LinearRegression()
reg.fit(XX,YY)
print(reg.predict(2017))

XXX = [[2001],[2002],[2003],[2004],[2005],[2006],[2007],[2008],[2009],[2010],[2011],[2012],[2013],[2014],[2015],[2016]]
YYY = [[4471000],[5028000],[7767000],[8300000],[4145000],[8862000],[2346000],[5122000],[10141000],[7442000],[8336000],[5079000],[9657000],[6800000],[11500000],[3807000]]
reg = linear_model.LinearRegression()
reg.fit(XXX,YYY)
print(reg.predict(2017))

'''
svr_rbf = SVR(kernel='poly', C=1e3, degree=2)
pred = y_rbf = svr_rbf.fit(XXX, YYY).predict(2017)
print pred
#print(reg.predict(2017))
lw = 2
plt.scatter(XXX, YYY, color='darkorange', label='data')

plt.plot(XXX,YYY, color='c', lw=lw, label='Linear model')
plt.savefig('hi')
'''