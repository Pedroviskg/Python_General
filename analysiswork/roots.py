import numpy as np
import matplotlib.pyplot as plt

#QUESTÃO 1

# Funções para o método de Newton: a função da questão e sua derivada analítica

def funcao_b(b, l):
  return np.cos(b*l)*np.cosh(b*l) + 1

def funcao_b_linha(b, l):
  return -l*np.sin(b*l)*np.cosh(b*l) + l*np.cos(b*l)*np.sinh(b*l)

# Calcula o intervalo em que haja uma raíz. Intervalo de B entre 0 e 10.

def intervalo(l):

  intervalos = np.linspace(1, 10, 20)
  arr        = np.array([])
  achou      = 0
  dx         = 0.5

  for i in intervalos:
    if funcao_b(i,l)*funcao_b(i + dx, l) < 0:
      arr = np.append(arr, [[i, i + dx]])
      achou += 1
    if achou != 0:
      arr = arr.reshape(-1, 2)
  return arr

# Usando o intervalo, os valores iniciais serão as médias aritméticas de cada intervalo.

def media(array, tamanho):
  med = np.array([])
  for i in range(0, tamanho):
    k = (array[i][0] + array[i][1])/2
    med = np.append(med, k)
  return med

# Função do método de Newton.

def newton(funcao, d_funcao, l, x0 = 0):
  while True:
    x_1 = x0 - funcao(x0, l)/d_funcao(x0, l)
    if abs(x0 - x_1) <= 1e-10:
      return (x_1)
    else:
      x0 = x_1

# Obtém a raiz e as agrega em um array numpy

def obter_raiz(valores_iniciais):
  x = np.array([])
  for i in valores_iniciais:
    x = np.append(x, newton(funcao_b, funcao_b_linha, l, i))
  return x

#A) e B)

l   = 1
b   = np.linspace(0, 8, 101)
f_b = funcao_b(b, l)

plt.plot(b, f_b, label = 'f(B)', color = 'red', ls = 'dashed')
plt.title('Frequência natural de uma barra uniforme')
plt.xlabel('B')
plt.ylabel('f(B)')
plt.legend()
plt.grid(True)
plt.show()


#C)

intervalo_raizes = intervalo(l)
print(intervalo_raizes)

#D)

valores_iniciais = media(intervalo_raizes, len(intervalo_raizes))
print("Valores iniciais", valores_iniciais)

raizes = obter_raiz(valores_iniciais)
print("Raízes", raizes)
