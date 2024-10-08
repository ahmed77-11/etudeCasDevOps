import numpy as np
# Accès à une ligne d'un tableau bidimensionnel
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0])
# Accès à une colonne d'un tableau bidimensionnel
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[:, 1])
# Calcul de la somme des éléments d'un tableau bidimensionnel
c = np.sum(b)
print(c)
# Calcul de la somme des éléments d'une colonne d'un tableau bidimensionnel
d = np.sum(b[:, 1])
print(d)
