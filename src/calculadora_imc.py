# Código Principal

def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula o IMC com base no peso (kg) e altura (m).
    Retorna o valor do IMC com duas casas decimais.
    """
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser valores positivos.")
    imc = peso / (altura ** 2)
    return round(imc, 2)


def classificar_imc(imc: float) -> str:
    """
    Retorna a classificação do IMC de acordo com a OMS.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"