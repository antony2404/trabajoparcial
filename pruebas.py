from principal import calcular_total

def test_calcular_total():
    assert calcular_total([100, 200, 300]) == 600
    assert calcular_total([]) == 0

    assert calcular_total([50]) == 50
