class ValidationProcessing:
	def __init__(self, args):
		for k,v in args.items():
			setattr(self, k, v)

	def is_positive(self):
		if self.number > 0:
			return True
		else:
			return False
