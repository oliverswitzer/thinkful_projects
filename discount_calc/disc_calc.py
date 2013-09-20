class DiscountCalculator(object):
	def calculate(self, total, discount_amount, discount_type):
		if discount_type == 'percent':
			discount_percent = float(discount_amount) / 100
			discount = float(total)*discount_percent
		elif discount_type == 'absolute':
			discount = discount_amount
		else:
			raise ValueError("Invalid discount amount")
		return discount
