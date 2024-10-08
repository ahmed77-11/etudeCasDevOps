import numpy as np

data=np.loadtxt('../data.csv', delimiter=',', dtype='object', skiprows=1)
print(data)


c2=data[:,2].astype(float)
print(c2)

moyenne=np.mean(c2)
varaiance=np.var(c2)
ecart_type=np.std(c2)



print(f'moyenne={moyenne},varaiance={varaiance},ecart_type={ecart_type}')


c3=data[:,3].astype(float)
c4=data[:,4].astype(float)

produit_matriciel=np.dot(c2,c3)
print("produit_matriciel=",produit_matriciel)

cumlative_sum=np.cumsum(c3)
print("cumlative_sum=",cumlative_sum)


