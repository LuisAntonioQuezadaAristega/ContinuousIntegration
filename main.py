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
    def __init__(self):
        self.memberships = []  # Lista de membresías seleccionadas
        self.total_price = 0

    def add_membership(self, membership):
        """Agrega una membresía al carrito y actualiza el costo total."""
        if membership.available:
            self.memberships.append(membership)
            self.total_price += membership.calculate_total_cost()
            print(f"{membership.name} added to the cart. Total price: ${self.total_price:.2f}")
        else:
            print(f"Membership {membership.name} is currently unavailable.")

    def calculate_discount(self):
        """Aplica descuentos especiales si hay 2 o más membresías idénticas en el carrito."""
        if len(self.memberships) >= 2:
            total_discount = 0.10 * self.total_price
            self.total_price -= total_discount
            print(f"A group discount of 10% has been applied. New total: ${self.total_price:.2f}")

        if self.total_price > 400:
            self.total_price -= 50
            print("Special offer: $50 discount applied.")
        elif self.total_price > 200:
            self.total_price -= 20
            print("Special offer: $20 discount applied.")

    def display_cart(self):
        """Muestra el contenido del carrito y el costo total."""
        if not self.memberships:
            print("The cart is empty.")
            return

        print("\nShopping Cart:")
        for i, membership in enumerate(self.memberships, start=1):
            print(f"{i}. {membership.name} - ${membership.calculate_total_cost():.2f}")
        
        print(f"Total Price: ${self.total_price:.2f}")

    def clear_cart(self):
        """Vacía el carrito de compras."""
        self.memberships = []
        self.total_price = 0
        print("Cart has been cleared.")




def main():

    print("In development.")


if __name__ == "__main__":
    main()