def calcular_total(ventas):
    """Calcula el total de ventas dadas en una lista."""
    return sum(ventas)
if __name__ == "principal":
    ventas = [100, 250, 75, 300]
    total = calcular_total(ventas)

    print(f"Total de ventas del día: ${total}")
