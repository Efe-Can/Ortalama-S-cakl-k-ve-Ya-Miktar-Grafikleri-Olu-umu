import matplotlib.pyplot as plt 
import seaborn as sns

#Sıcaklık
sns.set(rc={'axes.facecolor':'#ffdbcf', 'figure.facecolor':'#ffffff'})
sıcaklık = [20,21,23,26,29,31,32,31,29,27,23,21]
noktalar = [0,1,2,3,4,5,6,7,8,9,10,11]
aralıklar = [-30,-20,-10,0,10,20,30,40]
plt.plot(noktalar,sıcaklık,'-o',label="Sıcaklık",color="#ff4400")
plt.yticks(aralıklar,aralıklar)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],
          ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'],
           rotation=45,fontsize=10)
plt.legend()
plt.xlabel('Aylar')
plt.ylabel('Sıcaklık Miktarı (C°)')
plt.title('Sıcaklık')
plt.show()

#Yağış
sns.set(rc={'axes.facecolor':'#d9f7ff', 'figure.facecolor':'#ffffff'})
degerler = [25,0,0,0,0,0,0,0,0,0,45,17.5]
aralıklar = [0,50,100,150,200,250,300,350]
plt.bar([0,1,2,3,4,5,6,7,8,9,10,11],degerler,
label="Yağış",color="#02b5e6")
plt.yticks(aralıklar,aralıklar)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11],
          ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'],
           rotation=45,fontsize=10)
plt.legend()
plt.xlabel('Aylar')
plt.ylabel('Yağış Miktarı (mm)')
plt.title('Yağış')
plt.show()