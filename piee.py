import matplotlib.pyplot as plt
cars=['BMW','Audi',"Ford","Tesla","Jaguar"]
data=[34,14,22,10,15]
e=[0.1,0,0,0,0]
c=('grey','green','pink','#8B0000','blue')
plt.pie(data,labels=cars,colors=c,explode=e,autopct='%11.2f%%',shadow=True)
plt.show()