class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.estoque = dict()
        for ingrediente in self.MINIMUM_INVENTORY:
            self.estoque[ingrediente] = self.MINIMUM_INVENTORY[ingrediente]

    def add_new_order(self, customer, order, day):
        pratos_disponiveis = self.get_available_dishes()
        if order not in pratos_disponiveis:
            return False
        for ingrediente in self.INGREDIENTS[order]:
            self.estoque[ingrediente] -= 1

    def get_quantities_to_buy(self):
        result = dict()
        for ingrediente in self.MINIMUM_INVENTORY:
            result[ingrediente] = (
                self.MINIMUM_INVENTORY[ingrediente] - self.estoque[ingrediente]
            )

        return result

    def get_available_dishes(self):
        pratos_disponiveis = set()
        produtos_disponiveis = {
            ingrediente
            for ingrediente, quantidade in self.estoque.items()
            if quantidade > 0
        }

        for prato, ingredientes in self.INGREDIENTS.items():
            if set(ingredientes) <= produtos_disponiveis:
                pratos_disponiveis.add(prato)

        return pratos_disponiveis
