import pandas as pd
import numpy as np
d=pd.DataFrame({'date':pd.date_range(start='2023-09-07',periods=5,freq="D"),"temp":np.random.randint(18,30,5)})
d["f"]=d["temp"].shift(1)
print("shift:\n",d)
df=d.resample("m",on="date").mean()
print("\nResampling:\n",df)