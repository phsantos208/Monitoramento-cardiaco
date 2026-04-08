# Sistema de Monitoramento Cardíaco

batimentos = []

print("=== Monitoramento Cardíaco ===")
print("Digite os batimentos de cada segundo:")
print("")

# 1. Coletar os batimentos
for i in range(60):
    bpm = int(input("Segundo " + str(i + 1) + ": "))
    batimentos.append(bpm)

# 2. Calcular a média
total = 0
for bpm in batimentos:
    total = total + bpm
media = total / 60

# 3. Pico máximo
maximo = batimentos[0]
for bpm in batimentos:
    if bpm > maximo:
        maximo = bpm

# 4. Pico mínimo
minimo = batimentos[0]
for bpm in batimentos:
    if bpm < minimo:
        minimo = bpm

# 5. Contar valores fora da faixa segura
fora_da_faixa = 0
for bpm in batimentos:
    if bpm < 60 or bpm > 100:
        fora_da_faixa = fora_da_faixa + 1

# 6. Mostrar resultados
print("")
print("=== Resultados ===")
print("Media de batimentos: " + str(media))
print("Pico maximo: " + str(maximo) + " bpm")
print("Pico minimo: " + str(minimo) + " bpm")
print("Valores fora da faixa segura: " + str(fora_da_faixa))
