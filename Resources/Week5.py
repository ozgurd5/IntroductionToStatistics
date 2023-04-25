# -*- coding: utf-8 -*-
"""ders5.ipynb

Kartiller
"""

l=[19,20,21,22,23,23,23,24,25,26]

"""Sıralı veriyi 4 eşit parçaya ayıran değerler. """

from numpy import percentile, mean, median, absolute, std, sqrt

print(l[:-1])

q1=percentile(l,25,method='weibull')
q2=percentile(l,50,method='weibull')
q3=percentile(l,75,method='weibull')
print(q1,q2,q3)

q1=percentile(l[:-1],25,method='weibull')
q2=percentile(l[:-1],50,method='weibull')
q3=percentile(l[:-1],75,method='weibull')
print(q1,q2,q3)

"""Ortalama Mutlak Sapma"""

from numpy import mean, absolute, std, sqrt
x=[30,41,53,61,68,79,82,88,90,98]
OMS=mean(absolute(x - mean(x)))
print(OMS)

m=[33,39,45,51,57,63]
f=[2,6,10,7,4,1]
xbar=sum([m[i]*f[i] for i in range(len(m))])/sum(f)
sum([abs(m[i]-xbar)*f[i] for i in range(len(m))])/sum(f)

s=std(x) # kitle için!
print(s,mean(x),sum([(x[i]-mean(x))**2 for i in range(len(x))])/9.0,sqrt(504.222))