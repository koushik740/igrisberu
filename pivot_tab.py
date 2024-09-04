import pandas as pd
import matplotlib.pyplot as plt
data = {
    "First_name": ["Aryan", "Rohan", "Riya", "Yash", "Siddhant"],
    "Last_name": ["Singh", "Agarwal", "Shah", "Bhatia", "Khanna"],
    "Type": ["Full-Time", "Intern", "Full-Time", "Part-Time", "Full-Time"],
    "Department": ["Administration", "Technical", "Administration", "Technical", "Management"],
    "YoE": [2,3,5,7,6],
    "Salary": [1000, 5000,10000,20000,10000]
}
df=pd.DataFrame(data)
print(df)
av=df.pivot_table(index=['Department','Type'],values='Salary',aggfunc='mean')
print("Average Salary of each Dept:\n",av)
sm=df.pivot_table(index='Type',values='Salary',aggfunc=['sum','mean','count'])
sm.columns=("Total Salary",'Mean Salary','No of employees')
print("Sum and Mean:\n",sm)
St=df.pivot_table(values= 'Salary', index='Type', aggfunc='std')
print("\nStandard Deviation:\n", St)
plt.figure(figsize=(8, 6))
plt.plot(df["YoE"], df["Salary"], marker='p',linestyle='-', color='blue', label='Salary')
plt.xlabel("Years of Experience (YoE)")
plt.ylabel("Salary")
plt.title("Salary based on Years of Experience(YoE)")
plt.legend()
plt.grid(True)
plt.show()