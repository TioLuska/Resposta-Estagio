def sequencia_impares(n):
  """Retorna o próximo número ímpar na sequência."""
  return n + 2

def sequencia_potencias_de_dois(n):
  """Retorna a próxima potência de dois na sequência."""
  return n * 2

def sequencia_quadrados_perfeitos(n):
  """Retorna o próximo quadrado perfeito na sequência."""
  return (int(n**0.5) + 1)**2

def sequencia_quadrados_pares(n):
  """Retorna o próximo quadrado de um número par na sequência."""
  raiz = int(n**0.5)
  return (raiz + 2)**2

def sequencia_fibonacci(n1, n2):
  """Retorna o próximo número da sequência de Fibonacci."""
  return n1 + n2

# Chamadas às funções para obter os próximos elementos
print(sequencia_impares(7))  # Saída: 9
print(sequencia_potencias_de_dois(64))  # Saída: 128
print(sequencia_quadrados_perfeitos(36))  # Saída: 49
print(sequencia_quadrados_pares(64))  # Saída: 100
print(sequencia_fibonacci(5, 8))  # Saída: 13   