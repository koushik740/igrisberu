import pandas as pd
f={'course':["py","java","dbms","sql","r"],'fee':[500,100,56,76,600],'complexity':[90,45,32,56,100]}
d=pd.DataFrame(f)
print(d)
print("\n",d.pivot(columns="course",values="complexity"))
print("\n",d.melt())