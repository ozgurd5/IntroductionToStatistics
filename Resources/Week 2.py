

Uygulama 2.1 

X: 80 40 40 50 30 40 60 30 100 60
"""

x=[80, 40, 40, 50, 30, 40, 60, 30, 100, 60]

"""Soru 1: Değerlerin toplamını hesaplatınız """

print(sum(x))

"""Soru 2: Küçükten büyüğe sıralayınız

Python'da nesne yönelimli bir yaklaşım benimsenmiştir. Dizi nesnesi sıralama işlevine sahiptir. ' \
      'bir nesnenin işlevlerine değişkenin isminden sonra nokta koyarak ulaşabiliriz. Yani bir diziyi sıralamak istiyorsak dizi_adi.' \
      'sort() fonksiyonunu çağırabiliriz. Burada sort işlevi bir değer döndürmez ancak çağırıldığı diziyi sıralar.
"""

y=sorted(x)
print(y)
x.sort()
print(x)

"""Soru 3: Bu seride her sayı kaç kez
tekrarlanmıştır, bulunuz.

Bir listede her bir sayının kaç kere tekrarlandığının gösterilmesine histogram diyoruz Colab da histogram hesaplamak için bir kütüphane yüklememiz gerekiyor.

Python da kütüphaneler import komutu ile yüklenir. Satırın sonuna as komutuyla kütüphanenin kod içinde kullanılma ismi değiştirilebilir yada kısaltılabilir.
"""

import matplotlib.pyplot as plt

"""Bu örnekte matplotlib.pyplot kütüphanesi plt olarak adlandırılmıştır. Bu şekilde her seferinde kütüphanenin tam ismi yerine plt yazmak yeterli olacaktır."""

plt.hist(x,range(0,101)) 

plt.show()

"""Eğer grafik çizmek yerine değerleri kullanmak istiyorsak o zaman numpy kütüphanesinden yararlanabiliriz. Burada bir döngü kurmamız gerekecektir
Pythonda for döngüsü bir değişkenin verilen dizideki değerleri sırasıyla alması ve istenen işlemi yapması olarak tanımlanır.
Yani *for i in liste* i değişkenine liste dizisindeki her bir değeri sırayla atar ve her değer için bir tab içerde yazılmış tüm işlemleri gerçekleştirir.
C dilindeki gibi i değişkeninin 0 dan dizinin sonuna kadar indisleri sırasıyla almasını istediğimizde range komutunu kullanırız.  """

print(*range(10))

"""Şimdi tabloyu oluşturalım."""

import numpy as np
degerler=[30,40,50,60,80,100,101]# aralıklar bir önceki değerden verilen değere kadar sayılır yani counts[0] x dizisinde [30,40) aralığındaki 
# değer sayısı bu yüzden kaç tane 100 olduğunun sayılabilmesi için 110 değer eklendi
counts, bin_edges = np.histogram(x,bins=degerler)
print("%3s : %3s"%("x","f"))
print("%3s : %3s"%(3*"-",3*"-"))
for i in range(len(counts)):
  if(counts[i]!=0):
    print("%3d : %3d"%(degerler[i],counts[i]))

"""Python pretty table adında verileri tablo olarak yazdırabileceğimiz bir kütüphaneye de sahiptir.
Örnekte from anahtar kelimesi bir kütüphaneden sadece belirli fonksiyonları kullanmak istediğimizde şu kütüphaneden bu fonksiyonu al demeke için kulanılır.
Yani aşağıda ilk satırdaki kod prettytable kütüphanesinden PrettyTable fonksiyonunu al demektir."""

from prettytable import PrettyTable
tablo = PrettyTable(["X", "F"])
for i in range(len(counts)):
  if(counts[i]!=0):
    tablo.add_row([degerler[i], counts[i]])
print(tablo)

"""Gruplanmış veri örneği"""

from random import randint
liste=[randint(0,9) for i in range(100)]
print(liste)

"""frekans tablosu"""

degerler=range(11)
counts, bin_edges = np.histogram(liste,bins=degerler)
tablo = PrettyTable(["gruplar", "F"])
for i in range(len(counts)):
  if(counts[i]!=0):
    tablo.add_row([str(2*i)+"-"+str(2*i+1), counts[i]])
tablo.add_row(["------","----"])
tablo.add_row(["Toplam",sum(counts)])
print(tablo)

"""5 gruba ayrılmış frekans tablosunun oluşturulması"""

aralik= int((max(liste)-min(liste))/5+0.9)
degerler=[min(liste)+aralik*i for i in range(6)]
counts, bin_edges = np.histogram(liste,bins=degerler)
tablo = PrettyTable(["gruplar", "F"])
for i in range(len(counts)):
  if(counts[i]!=0):
    tablo.add_row([str(2*i)+"-"+str(2*i+1), counts[i]])
tablo.add_row(["------","----"])
tablo.add_row(["Toplam",sum(counts)])
print(tablo)

"""4 gruba ayrılmış hali"""

grup=4
aralik= int((max(liste)-min(liste))/grup+0.9)
degerler=[aralik*i for i in range(grup+1)]
counts, bin_edges = np.histogram(liste,bins=degerler)
tablo = PrettyTable(["gruplar", "F"])
for i in range(len(counts)):
  if(counts[i]!=0):
    tablo.add_row([str(aralik*i)+"-"+str(aralik*(i+1)-1), counts[i]])
tablo.add_row(["------","----"])
tablo.add_row(["Toplam",sum(counts)])
print(tablo)

"""Uygulama 2.2"""

notlar=[1,2,3,3,4,4,4,5,6,6,7,8,9,9,10]
degerler=range(min(notlar),max(notlar)+2)
counts, bin_edges = np.histogram(notlar,bins=degerler)
tablo = PrettyTable(["gruplar", "F"])
for i in range(len(counts)):
  if(counts[i]!=0):
    tablo.add_row([degerler[i], counts[i]])
tablo.add_row(["------","----"])
tablo.add_row(["Toplam",sum(counts)])
print(tablo)

grup=5
aralik= int((max(notlar)-min(notlar))/grup+0.9)
degerler=[min(notlar)+aralik*i for i in range(grup+1)]
counts, bin_edges = np.histogram(notlar,bins=degerler)
tablo = PrettyTable(["gruplar", "F"])
for i in range(len(counts)):
  if(counts[i]!=0):
    tablo.add_row([str(aralik*i)+"-"+str(aralik*(i+1)-1), counts[i]])
tablo.add_row(["------","----"])
tablo.add_row(["Toplam",sum(counts)])
print(tablo)