import shelve 


class Bank:
	def __init__(self):
		print("Welcome to the BANK")
		self.account_holder = []
		db = shelve.open('database')
		for i in list(db.keys()):
			self.account_holder.append(i)
		db.close()

	def createAccount(self, name, address, balance):
		if name not in self.account_holder:
			self.account_holder.append(name)
			db = shelve.open('database')
			db[name] = [address, balance]
			db.close()
			print("Your account is created!")
		else:
			print("You already have an account!")
	
	def showAccount(self, name):
		if name in self.account_holder:
			db = shelve.open('database')
			print(list(db[name]))
			db.close()
		else:
			print("You need to create an account first!")

	def printdatabase(self):
		db = shelve.open('database')
		print(list(db.keys()))
		print(list(db.values()))
		db.close()


bank = Bank()

while True:
	print("Enter 1 for making account.")
	print("Enter 2 for showing account.")
	print("Enter 3 for printing database.")
	print("Enter 'quit' for exiting the program.")
	print()
	action = input('What do you want to do? ')
	print()
	if action == 'quit':
		print("Exiting")
		print()
		break
	elif action == '1':
		print("Enter your personal details.")
		name = input("Enter your name: ")
		add = input("Enter your address: ")
		balance = int(input("Enter you balance: "))
		bank.createAccount(name, add, balance)
		print()
		print()
	elif action == '2':
		name = input("Enter your name: ")
		bank.showAccount(name)
		print()
		print()
	elif action == '3':
		bank.printdatabase()
		print()
		print()
	else:
		print("Invalid input, try again!")
		print()
		print()
