import pytest
from src.calculadora_imc import calcular_imc, classificar_imc

def test_calculo_imc_correto():
    assert calcular_imc(70, 1.75) == pytest.approx(22.86, 0.01)

def test_classificacao_abaixo_peso():
    assert classificar_imc(17.5) == "Abaixo do peso"

def test_classificacao_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.0) == "Sobrepeso"

def test_classificacao_obesidade():
    assert classificar_imc(31.0) == "Obesidade"

def test_valores_invalidos():
    with pytest.raises(ValueError):
        calcular_imc(-70, 1.75)

    with pytest.raises(ValueError):
        calcular_imc(70, 0)
