import csv
from datetime import datetime

def leer_ventas(archivo_csv):
    """Lee las ventas desde un archivo CSV """
    ventas = []
    with open(archivo_csv, newline='', encoding='utf-8-sig') as csvfile:
        lector = csv.DictReader(csvfile)

        for fila in lector:
            producto = fila.get('producto') or fila.get('Producto') or fila.get('descripcion') or fila.get('nombre')
            cantidad = fila.get('cantidad') or fila.get('Cantidad') or fila.get('unidades')
            precio = fila.get('precio_unitario') or fila.get('Precio_unitario') or fila.get('precio') or fila.get('Precio')

            if producto and cantidad and precio:
                ventas.append({
                    'producto': producto.strip(),
                    'cantidad': int(cantidad),
                    'precio_unitario': float(precio)
                })
            else:
                print(f"⚠️ Fila con datos incompletos: {fila}")
    return ventas

def calcular_total(ventas):
    """Calcula el total de ventas y detecta anomalías."""
    total = sum(ventas['cantidad'] * ventas['precio_unitario'] for ventas in ventas)
    alertas = [ventas for ventas in ventas if ventas['cantidad'] > 100]
    return total, alertas

def generar_reporte(total, alertas):
    """Genera un archivo de texto con el resumen diario."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    with open(f"reporte_{fecha}.txt", "w", encoding="utf-8") as f:
        f.write(f"📅 Reporte de ventas - {fecha}\n")
        f.write(f"Total vendido: ${total:.2f}\n")
        if alertas:
            f.write("\n⚠️ Productos con ventas inusuales:\n")
            for a in alertas:
                f.write(f"- {a['producto']} ({a['cantidad']} unidades)\n")
        else:
            f.write("\nSin errores.\n")

if __name__ == "__main__":
    ventas = leer_ventas("ventas.csv")
    total, alertas = calcular_total(ventas)
    generar_reporte(total, alertas)
    print("✅ Reporte generado correctamente.")


