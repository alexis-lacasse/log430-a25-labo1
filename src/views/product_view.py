from controllers.product_controller import ProductController
from models.product import Product

class ProductView:
	@staticmethod
	def show_options():
		controller = ProductController()
		while True:
			print("\n1. Montrer la liste d'items\n2. Ajouter un item\n3. Quitter")
			choice = input("Choisissez une option: ")

			if choice == '1':
				products = controller.list_products()
				ProductView.show_items(products)
			elif choice == '2':
				name, brand, price = ProductView.get_inputs()
				product = Product(None, name, brand, price)
				controller.create_product(product)
				print("Produit ajouté!")
			elif choice == '3':
				controller.shutdown()
				break
			else:
				print("Cette option n'existe pas.")

	@staticmethod
	def show_items(products):
		print("\n".join(f"{p.id}: {p.name} {p.brand} ({p.price})" for p in products))

	@staticmethod
	def get_inputs():
		name = input("Nom du produit : ").strip()
		brand = input("Marque du produit : ").strip()
		price = input("Prix du produit : ").strip()
		return name, brand, price

