from datetime import datetime

def obter_quintas(mes: int, ano: int, dias=[3]):
    dias_encontrados = []
    for dia in range(1, 32):
        try:
            data = datetime(ano, mes, dia)
            if data.weekday() in dias:
                dias_encontrados.append(dia)
        except ValueError:
            break
    return dias_encontrados


def obter_sextas(mes: int, ano: int, dias=[4]):
    dias_encontrados = []
    for dia in range(1, 32):
        try:
            data = datetime(ano, mes, dia)
            if data.weekday() in dias:
                dias_encontrados.append(dia)
        except ValueError:
            break
    return dias_encontrados


