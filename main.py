class Membership:
    def __init__(self, name, price, is_premium=False):
        self.name = name              # Nombre del plan de membresía (e.g., Basic, Premium, Family)
        self.base_price = price       # Costo base de la membresía
        self.is_premium = is_premium  # Indica si la membresía es premium o no
        self.features = []            # Lista de características adicionales seleccionadas
        self.available = True         # Indica si la membresía está disponible

    def add_feature(self, feature):
        """Agrega una característica adicional a la membresía si está disponible."""
        if feature.available:
            self.features.append(feature)
        else:
            print(f"The feature {feature.name} is currently unavailable.")

    def calculate_total_cost(self):
        """Calcula el costo total de la membresía incluyendo características adicionales y cualquier recargo por membresías premium."""
        features_cost = sum([feature.price for feature in self.features])
        total_cost = self.base_price + features_cost

        # Aplica un recargo de 15% si es una membresía premium
        if self.is_premium:
            total_cost *= 1.15  # Aplica un recargo del 15%

        return total_cost
 

class Features:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Shoppincart:

    def __init__(self, name, price):
        self.name = name
        self.price = price


def main():

    print("In development.")


if __name__ == "__main__":
    main()