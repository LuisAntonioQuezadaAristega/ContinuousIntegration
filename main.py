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
 

class AdditionalFeatures:

    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available

    def toggle_availability(self):
        """Alterna la disponibilidad de la característica."""
        self.available = not self.available
        status = "available" if self.available else "unavailable"
        print(f"Feature '{self.name}' is now {status}.")

    def display_info(self):
        """Muestra información sobre la característica adicional."""
        availability = "Available" if self.available else "Unavailable"
        print(f"Feature: {self.name} | Price: ${self.price} | Status: {availability}")


class ShoppingCart:
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
        # Recalcular el costo total 
        self.total_price = sum([membership.calculate_total_cost() for membership in self.memberships])
        
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
    # Crear ejemplos de membresías
    basic_membership = Membership("Basic", 50)
    premium_membership = Membership("Premium", 100, is_premium=True)
    family_membership = Membership("Family", 80)

    # Crear características adicionales
    personal_training = AdditionalFeatures("Personal Training", 20)
    group_classes = AdditionalFeatures("Group Classes", 15)

    # Crear un carrito de compras
    cart = ShoppingCart()

    # Simular interacción del usuario
    while True:
        print("\n--- Gym Membership Shop ---")
        print("1. View available memberships")
        print("2. Add membership to cart")
        print("3. Add additional features to a membership")
        print("4. View available additional features")
        print("5. Toggle availability of a feature")
        print("6. View cart")
        print("7. Clear cart")
        print("8. Checkout and apply discounts")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAvailable Memberships:")
            print("1. Basic - $50")
            print("2. Premium - $100 (15% surcharge for premium features)")
            print("3. Family - $80")
        elif choice == "2":
            membership_choice = input("\nEnter the number of the membership to add (1-Basic, 2-Premium, 3-Family): ")
            if membership_choice == "1":
                cart.add_membership(basic_membership)
            elif membership_choice == "2":
                cart.add_membership(premium_membership)
            elif membership_choice == "3":
                cart.add_membership(family_membership)
            else:
                print("Invalid choice.")
        elif choice == "3":
            if cart.memberships:
                feature_choice = input("\nAdd features to which membership? (Enter 1, 2, ...): ")
                if feature_choice.isdigit() and 1 <= int(feature_choice) <= len(cart.memberships):
                    selected_membership = cart.memberships[int(feature_choice) - 1]
                    feature_to_add = input("\nEnter the feature to add (1-Personal Training, 2-Group Classes): ")
                    if feature_to_add == "1":
                        selected_membership.add_feature(personal_training)
                    elif feature_to_add == "2":
                        selected_membership.add_feature(group_classes)
                    else:
                        print("Invalid feature choice.")
                else:
                    print("Invalid membership selection.")
            else:
                print("No memberships in the cart.")
        elif choice == "4":
            print("\nAvailable Additional Features:")
            personal_training.display_info()
            group_classes.display_info()
        elif choice == "5":
            toggle_choice = input("\nEnter the feature to toggle availability (1-Personal Training, 2-Group Classes): ")
            if toggle_choice == "1":
                personal_training.toggle_availability()
            elif toggle_choice == "2":
                group_classes.toggle_availability()
            else:
                print("Invalid choice.")
        elif choice == "6":
            cart.display_cart()
        elif choice == "7":
            cart.clear_cart()
        elif choice == "8":
            cart.calculate_discount()
            cart.display_cart()
        elif choice == "9":
            print("Exiting the shop. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

