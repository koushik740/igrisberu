import matplotlib.pyplot as p
prices=[12,30,22,37,48,5,18]
sales=[34,58,20,37,40,10,5]
p.scatter(prices,sales,color='red',s=60,marker='p',alpha=1)
p.title('Dataset')
p.xlabel('sales')
p.ylabel('price')
p.show()