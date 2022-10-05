import numpy as np
import pandas as pd

num=pd.read_excel("digitos 50.xlsx", header=None)
arr=num.to_numpy()

sum=0
rf=''
for i in range(49,-1,-1):
    for e in range(100):
        y=arr[e,0]
        x=y[i]
        x=int(x)
        sum=sum+x
    r=str(sum)
    if i==0:
        rf=r+rf
    else:
        rf=r[-1]+rf
    sum=str(sum)
    sum=sum[:-1]
    if sum!='':
        sum=int(sum)
    else:
        sum=0
print (rf)

print('Respuesta:',rf[:10])