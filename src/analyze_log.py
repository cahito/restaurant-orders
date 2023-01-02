import csv


def analise_mkt_prato(data, person):
    prato = dict()
    for pedido in data:
        if pedido[0] == person:
            if pedido[1] not in prato:
                prato[pedido[1]] = 1
            else:
                prato[pedido[1]] += 1
    favorito = max(prato, key=prato.get)

    return favorito


def analise_mkt_vezes(data, person, meal):
    vezes = 0
    for pedido in data:
        if pedido[0] == person:
            if pedido[1] == meal:
                vezes += 1

    return vezes


def analise_mkt_nunca_prato(data, person):
    pratos_existentes = set()
    pratos_pedidos = set()
    for pedido in data:
        pratos_existentes.add(pedido[1])
        if pedido[0] == person:
            pratos_pedidos.add(pedido[1])

    return pratos_existentes - pratos_pedidos


def analise_mkt_nunca_dia(data, person):
    dias_atendimento = set()
    dias_com_cliente = set()
    for pedido in data:
        dias_atendimento.add(pedido[2])
        if pedido[0] == person:
            dias_com_cliente.add(pedido[2])

    return dias_atendimento - dias_com_cliente


def write_results(results):
    try:
        with open("data/mkt_campaign.txt", "a") as file:
            file.write(results)
    except ValueError:
        raise ValueError


def analyze_log(path_to_file: str):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file, "r") as file:
            temp = csv.reader(file, delimiter=",")
            dados = list(temp)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    prato_mais_pedido = analise_mkt_prato(dados, "maria")
    quantas_vezes_pediu = analise_mkt_vezes(dados, "arnaldo", "hamburguer")
    pratos_nunca_pedidos = analise_mkt_nunca_prato(dados, "joao")
    dias_que_nunca_veio = analise_mkt_nunca_dia(dados, "joao")
    result = f"""{prato_mais_pedido}
{quantas_vezes_pediu}
{pratos_nunca_pedidos}
{dias_que_nunca_veio}"""

    write_results(result)
