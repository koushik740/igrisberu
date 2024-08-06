import pandas as pd
from functools import reduce
data={'numbers':[1,2,3,4,5],'letters':['A','B','C','D','E']}
df=pd.DataFrame(data)
sq=df['numbers'].map(lambda x:x**2)
ev=list(filter(lambda x:x%2==0,df['numbers']))
po=reduce(lambda x,y:x*y,df['numbers'])
print("\n map for squarting:\n",sq)
print("\n reduce for product:\n",po)
print("\n filter for even:\n",ev)