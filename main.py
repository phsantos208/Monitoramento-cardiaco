# Sistema de Monitoramento Cardíaco

batimentos = []

print("=== Monitoramento Cardíaco ===")
print("Digite os batimentos de cada segundo:\n")

for i in range(60):
    bpm = int(input(f"Segundo {i + 1}: "))
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

print("\n=== Resultados ===")
print("Média de batimentos:", media)
print("Pico máximo:", maximo, "bpm")
print("Pico mínimo:", minimo, "bpm")
print("Valores fora da faixa segura:", fora_da_faixa)