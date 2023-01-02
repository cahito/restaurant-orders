class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.pedido = list()

    def __len__(self):
        return len(self.pedido)

    def add_new_order(self, customer, order, day):
        self.pedido.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        prato = dict()
        for pedido in self.pedido:
            if pedido[0] == customer:
                if pedido[1] not in prato:
                    prato[pedido[1]] = 1
                else:
                    prato[pedido[1]] += 1
        favorito = max(prato, key=prato.get)

        return favorito

    def get_never_ordered_per_customer(self, customer):
        pratos_existentes = set()
        pratos_pedidos = set()
        for pedido in self.pedido:
            pratos_existentes.add(pedido[1])
            if pedido[0] == customer:
                pratos_pedidos.add(pedido[1])

        return pratos_existentes - pratos_pedidos

    def get_days_never_visited_per_customer(self, customer):
        dias_atendimento = set()
        dias_com_cliente = set()
        for pedido in self.pedido:
            dias_atendimento.add(pedido[2])
            if pedido[0] == customer:
                dias_com_cliente.add(pedido[2])

        return dias_atendimento - dias_com_cliente

    def get_busiest_day(self):
        dias_com_clientes = dict()
        for pedido in self.pedido:
            if pedido[2] not in dias_com_clientes:
                dias_com_clientes[pedido[2]] = 1
            else:
                dias_com_clientes[pedido[2]] += 1
        dia_cheio = max(dias_com_clientes, key=dias_com_clientes.get)

        return dia_cheio

    def get_least_busy_day(self):
        dias_com_clientes = dict()
        for pedido in self.pedido:
            if pedido[2] not in dias_com_clientes:
                dias_com_clientes[pedido[2]] = 1
            else:
                dias_com_clientes[pedido[2]] += 1
        dia_vazio = min(dias_com_clientes, key=dias_com_clientes.get)

        return dia_vazio
