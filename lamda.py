import pandas as pd
from functools import reduce
data={'number':[1,2,3,4,5],'letters':['a','b','c','d','e']}
df=pd.DataFrame(data)
sq=df['number'].map(lambda x:x**2)
ev=list(filter(lambda x:x%2==0,df['number']))
po=reduce(lambda x,y:x*y,df['number'])
print('DataFrame:',df)
print("\nmap for squaring:\n",sq)
print("reduce for product:\n",po)
print("\nfilter for even numbers:\n",ev)