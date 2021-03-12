# Shopping Bucket
class Customer:
	def __init__(self, budget):
		self.budget=budget
		self.cart_total = 0
		self.cart = dict() # empty dictionary
	def add_item(self, product, quantity, price):
		# Validate if capable to buy
		if price < self.get_balance():
			# Check if product already in cart
			if product in self.cart.keys():
				# remove previous price , we will append new later
				self.cart_total -= self.cart[product]['price']
			# we are using dictionary implementaion, so it will update if exist or add
			self.cart[product] = {'price': price, 'quantity': quantity}
			# increase the cart_total
			self.cart_total += price
			# Print Balance
			print(f"Amount left : {self.get_balance()}")
		else:
			print(f"Can't Buy the product ###(because budget left is {self.get_balance()})")
	def get_balance(self):
		return self.budget - self.cart_total
	def budget_suggestion(self):
		max_product_price = 0
		max_product = ''
		for product, details in self.cart.items():
			if ( details['price'] <= self.get_balance() ) and (details['price'] >= max_product_price):
				max_product_price = details['price']
				max_product = product
		# If found any product with leftover budget				
		if max_product != '':
			print(f"Amount left can buy you {max_product}")
	def show_cart(self):
		if len(self.cart.keys()) > 0:
			print('GROCERY LIST is:')
			print("Product name \tQuantity \tPrice")
			for product, details in self.cart.items():
				print("{:12} \t {:7} \t{: >5}".format(product, details['quantity'], details['price']))
		else:
			print("Your cart is empty ;(")
# Question Loop
def interface():
	print("User GO with following question")
	# Ask Budget
	budget = int(input("Enter your budget : "))
	customer = Customer(budget)
	# Prepare questions
	questions = [
		'1.Add an item',
		'2.Exit'
	]
	user_choice = 3
	while(user_choice!=2) : # 2 denotes exit
		# print avail choices
		[print(question) for question in questions]
		#
		user_choice = int(input("Enter your choice : "))
		print('\n')
		# on add item
		if user_choice == 1:
			product = input("Enter product : ")
			quantity = input("Enter quantity : ")
			price = int(input("Enter Price : "))
			# Add to cart
			print('\n')
			customer.add_item(product, quantity, price)
			print('\n')
		# Exit is while termination
	customer.budget_suggestion()
	print('\n')
	customer.show_cart()

if __name__ =='__main__':
	interface()
