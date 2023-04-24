
"""ders4.ipynb
Basit seriler için ortalama hesabı elemanların toplamının eleman sayısına bölünmesi ile bulunur. Pythonda bir dizinin boyutu len() fonksiyonu ile bulunabilir.
"""

x=[95,88,73,67,59,46,35,26,23]
s=0
for x_i in x:
  s += x_i
ort=s/len(x)
print("Ortalama : %d/%d = %f"%(s,len(x),ort))

"""Gruplanmış seriler için aritmetik ortalama her bir değerin frekansı ile çarpılarak toplandığı ve toplam frekansa bölündüğü ortalama hesabıdır."""

Grup=[51,66,72,82,94]
f=[1,3,4,5,7]
s=0
for i in range(len(Grup)):
  s += f[i]*Grup[i]
ort = s/sum(f)
print("Ortalama : %d/%d = %f"%(s,sum(f),ort))

x=[1.8, 2.0, 3.4, 3.9, 5.3, 9.1, 10.8]
f=[1,1,2,1,3,1,1]
s=0
for i in range(len(x)):
  s += f[i]*x[i]
ort = s/sum(f)
print("Ortalama : %d/%d = %f"%(s,sum(f),ort))

"""Sınıflanmış serilerde aritmetik ortalama sınıf orta noktaları kullanılır."""

from prettytable import PrettyTable
sinirlar=[30, 36, 42, 48, 54, 60, 66]
f=[2,6,10,7,4,1]
tablo = PrettyTable(["Siniflar", "f_i", "m_i", "m_i f_i"])
s=0
for i in range(len(sinirlar)-1):
  m_i = sinirlar[i]+(sinirlar[i+1]-sinirlar[i])/2
  s += m_i*f[i]
  tablo.add_row([str(sinirlar[i])+" - "+str(sinirlar[i+1])+" den az",f[i], m_i, m_i*f[i] ])
print(tablo)
ort = s/sum(f)
print("Ortalama : %d/%d = %f"%(s,sum(f),ort))

"""Ağırlıklı aritmetik ortalama, frekanslar yerine ağırlıklar kullanılarak hesaplanan ortalamadır."""

dersler=["Isitatistik", "Matematik", "Iktisat", "Isletme"]
notlar=[70,60,50,80]
kredi=[3,4,3,2]
tablo = PrettyTable(["Dersler", "Notlar", "Kredi", "t_i x_i"])
s=0
for i in range(len(dersler)):
  s+=notlar[i]*kredi[i]
  tablo.add_row([dersler[i],notlar[i],kredi[i],notlar[i]*kredi[i]])
tablo.add_row(["Toplam",sum(notlar),sum(kredi),s])
ort=s/sum(kredi)
print("Ortalama : %d/%d = %f"%(s,sum(kredi),ort))

"""Harmonik ortalama"""

x=[10,6,4,5]
s=0
for x_i in x:
  s += 1.0/x_i
print("1/H = %f /%d "%(s,len(x)))
print("H = %d/%f = %f"%(len(x),s,len(x)/s))

"""Alternatif olarak istatistik paketinden direk hmean fonksiyonu kullanılabilir."""

from scipy.stats.mstats import hmean
print(hmean(x))

"""Geometrik ortalama log işlemi kullanılır. Pythonda standart log işlemi e tabanında çalışır. """

from math import log,exp
m=[1.5, 2.5, 1, 3, 2]
s=0
for m_i in m:
  s+=log(m_i)
print("log G = %f / %d"%(s,len(m)))
print("G = e^%f = %f"%(s/len(m),exp(s/len(m))))

"""Alternatif olarak istatistik paketinden direk gmean fonksiyonu kullanılabilir."""

from scipy.stats.mstats import gmean

print(gmean(m))

"""Mod hesabı"""

from scipy.stats import mode
x=[60, 72, 82, 72, 61, 81, 72]
print("%d degeri %d kere tekrarlanmistir."%(mode(x).mode[0],mode(x).count[0]))

import statistics
x=[60, 72, 82, 72, 61, 81, 72]
statistics.mode(x)

"""Medyan hesabı"""

from numpy import median
x=[30,42,56,61,68,79,82,88,90,98]
print("Medyan degeri %.1f."%(median(x)))
print("Medyan degeri %.1f."%(median(x[:-1])))