"""
Calculadora de propinas - Salida por terminal
"""
precio = float(input("Ingresa el precio de la cuenta: $"))

lista_de_porcentaje = [5, 10, 15, 20]

print(f"\n{'Porcentaje %':<15}{'Propina $':<15}{'Total $':<15}")
print("-" * 45)

for porcentaje in lista_de_porcentaje:
    propina = precio * (porcentaje / 100)
    total = precio + propina
    print(f"{str(porcentaje) + '%':<15}{propina:<15.2f}{total:<15.2f}")