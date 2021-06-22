def funcion_decoradora(funcion):
	@property
	def wrapper():
		print("Este es el último mensaje...")
		funcion
		print("Este es el primer mensaje ;)")
		i=input("que onda")
	return wrapper

def zumbido():
	print("Buzzzzzz")

zumbido = funcion_decoradora(zumbido())