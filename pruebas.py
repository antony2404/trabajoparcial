from trabajoparcial import calcular_total

def test_calcular_total():
    ventas = [
        {"producto": "A", "cantidad": 10, "precio_unitario": 2.0},
        {"producto": "B", "cantidad": 5, "precio_unitario": 3.0},
    ]
    total, alertas = calcular_total(ventas)
    assert total == 35.0
    assert alertas == []

