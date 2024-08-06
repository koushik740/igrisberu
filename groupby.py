import pandas as p
t={'course':["py","jv","dbms","mma","mmu"],'fee':[300,600,32,59,86],'complexity':[100,56,32,10,67]}
d=p.DataFrame(t)
print(d)
c=d.groupby('course').agg({'fee':'min'})
print("\n",c)