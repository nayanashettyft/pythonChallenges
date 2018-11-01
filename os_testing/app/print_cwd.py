import os

class PrintCWD:
	def __init__(self):
		pass

	def work_on(self):
		path = os.getcwd()
		print(f'Working on {path}')
		return path

	def work_on_env(self):
		path = os.path.join(os.getcwd(), os.environ['MY_VAR'])
		print(f'Working on {path}')
		return path

def main():
	printcwd = PrintCWD()
	printcwd.work_on()

#  This is main
if __name__ == "__main__":
    main()