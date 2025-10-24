import csv
from datetime import datetime

def leer_ventas(archivo_csv):
    """Lee las ventas desde un archivo CSV."""
    ventas = []
    with open(archivo_csv, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            ventas.append({
                'producto': fila['producto'],
                'cantidad': int(fila['cantidad']),
                'precio_unitario': float(fila['precio_unitario'])
            })
    return ventas

def calcular_total(ventas):
    """Calcula el total de ventas y detecta anomalías."""
    total = sum(v['cantidad'] * v['precio_unitario'] for v in ventas)
    alertas = [v for v in ventas if v['cantidad'] > 100]
    return total, alertas

def generar_reporte(total, alertas):
    """Genera un archivo de texto con el resumen diario."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    with open(f"reporte_{fecha}.txt", "w", encoding="utf-8") as f:
        f.write(f"Reporte de ventas - {fecha}\n")
        f.write(f"Total vendido: ${total:.2f}\n")
        if alertas:
            f.write("\nProductos con ventas inusuales:\n")
            for a in alertas:
                f.write(f"- {a['producto']} ({a['cantidad']} unidades)\n")
        else:
            f.write("\nSin errores.\n")

if __name__ == "__main__":
    ventas = leer_ventas("ventas.csv")
    total, alertas = calcular_total(ventas)
    generar_reporte(total, alertas)
    print("Reporte generado correctamente.")

