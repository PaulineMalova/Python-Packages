class Mpesa_Account:

	def __init__(self,name,phone_number,balance):
		self.name = name
		self.phone_number = phone_number
		self.balance = balance

	def deposit(self,amount):
		self.balance = self.balance + amount
		print ("Dear {}, you have successfuly deposited Ksh{} into your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		
	def withdraw(self,amount):
		if self.balance>amount:
			self.balance = self.balance - amount
			print ("Dear {}, you have successfully withdrawn Ksh{} from your account {}. Your new M-pesa balance is Ksh{}.".format(self.name,amount,self.phone_number,self.balance))
		else:
			print ("Sorry {}, you have insufficient funds to facilitate your withdrawal. Your current balance is Ksh{}.".format(self.name,self.balance))

	def check_balance(self):
		print ("Dear {}, your M-pesa balance is Ksh{}".format(self.name,self.balance))

