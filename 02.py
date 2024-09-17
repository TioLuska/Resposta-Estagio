def contar_as(texto):

  texto_minusculo = texto.lower()

  contagem = texto_minusculo.count('a')

  return contagem

texto = input("Digite uma frase: ")
resultado = contar_as(texto)
print(f"A letra 'a' aparece {resultado} vezes na frase.")