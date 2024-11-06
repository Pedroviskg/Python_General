import numpy as np
import matplotlib.pyplot as plt

# Condições de contorno:
#u(x,3) = 1
#u(x,0) = 0
#u(0,y) = 0
#U(4,y) = 0

# Condições de contorno:
#u(x,3) = 1
#u(x,0) = 0
#u(0,y) = 0
#U(4,y) = 0

tam_y = 3
tam_x = 4

T = np.zeros([41,41])
linha  = np.shape(T)[0]
coluna = np.shape(T)[1]

T[-1, :] = 1  # Linha superior (y = 3) tem valor 1
T[:, 0] = 0   # Coluna esquerda (x = 0) tem valor 0
T[:, -1] = 0  # Coluna direita (x = 4) tem valor 0

erro = 10
tol  = 1e-3
X_old = np.ones([linha,coluna])

while tol < erro:
  X = np.copy(T)
  for i in range(1, linha-1):
    for j in range(1, coluna-1):
      T[i][j] = (T[i+1][j] + T[i-1][j] + T[i][j+1] + T[i][j-1])/4
  erro = np.linalg.norm(X_old - X)/np.linalg.norm(X)
  X_old = X

coord_x = np.linspace(0, tam_x, linha)
coord_y = np.linspace(0, tam_y, coluna)

# Visualização do resultado
plt.contourf(coord_x, coord_y, T, levels=50, cmap="coolwarm")
plt.colorbar(label='u(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução eq. calor')
plt.show()

tam_x = 4
tam_y = 4

U = np.zeros([5,5])
U[-1, :] = 100   # Linha inferior (y = tam_y) com valor 100
U[0, :] = -100   # Linha superior (y = 0) com valor -100
U[:, 0] = 0      # Coluna esquerda (x = 0) com valor 0
U[:, -1] = 0
linha  = np.shape(U)[0]
coluna = np.shape(U)[1]

erro = 10
tol  = 1e-3
X_old = np.ones([linha,coluna])

while tol < erro:
  X = np.copy(U)
  for i in range(1, linha-1):
    for j in range(1, coluna-1):
      U[i][j] = (U[i+1][j] + U[i-1][j] + U[i][j+1] + U[i][j-1])/4
  erro = np.linalg.norm(X_old - X)/np.linalg.norm(X)
  X_old = X

coord_x = np.linspace(0, tam_x, linha)
coord_y = np.linspace(0, tam_y, coluna)

# Visualização do resultado
plt.contourf(coord_x, coord_y, U, levels=50, cmap="coolwarm")
plt.colorbar(label='u(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução eq. potencial')
plt.show()

import numpy as np

A = np.array([[10, 0, 0, 100, 0, 0],
              [10, -100, 0, 0, 100, 0],
              [0, 0, 100, -100, 100, 0],
              [1, 1, 0, 0, 0, -1],
              [1, 0, 0, -1, -1, 0],
              [0, -1, 1, 0, -1, 0]], dtype = float)


b = np.array([10, 0, 0,0,0,0], dtype =float)
b_ajustado = b.reshape(-1,1)
n = len(b)
Ab = np.concatenate((A,b_ajustado), 1)


for j in range(n):
  # Encontrado os pivos
  pivo = A[j][j]
  linha_pivo = j
  for k in range(j+1, n):
    if abs(A[k][j]) > abs(A[linha_pivo][j]):
      pivo = A[k][j]
      linha_pivo = k

  # Mudando a linha do pivo com a linha atual
  if linha_pivo != j:
    Ab[[j, linha_pivo]] = Ab[[linha_pivo, j]]

  for i in range(j+1, n):
        multiplicador = Ab[i][j] / Ab[j][j]
        Ab[i] = Ab[i] - multiplicador * Ab[j]

x = np.zeros(n)

for i in range(n - 1, -1, -1):
  s = Ab[i][n]
  for j in range(i+1, n):
    s -= Ab[i][j] * x[j]

  x[i] = s/Ab[i][i]
for i in range(len(x)):
  print("Solução x_", i, ": ", x[i])

A = np.array([[8, 1, -1],
             [1, -7, 2],
             [2, 1, 9]])

b = np.array([8, -4, 12])

max = 100
x1 = 0
x2 = 0
x3 = 0
tol = 1e-6

for interacoes in range(max):
  x1_new = 10 + 4*x2 + 2*x3
  x2_new = (4*x1_new - 8*x2 - (1/40) * np.log(1 + x2*1e9) + 2*x3)/8
  x3_new = 4 + 2*x1_new + 2*x2_new


  x1 = x1_new
  x2 = x2_new
  x3 = x3_new

  if abs(x1_new - x1) < tol and abs(x2_new - x2) < tol and abs(x3_new - x3) < tol:
    break


print(x1, "  ", x2, "  ", x3)

