
# CLASE NODO
class Nodo:
	def __init__ (self, valor):
		self.info = valor
		self.sig = None
	
# CLASE LISTA
class Lista:
	
	# CONSTRUCTOR
	def __init__ (self):
		self.__primero = None
		self.__ultimo = None
		self.__actual = None
		self.__n = 0
		self.__pos = 0

    # Metodo para insertar al inicio de la lista
	def insertar_inicio (self, valor):
		nodo = Nodo (valor)
		
		nodo.sig = self.__primero
		self.__primero = nodo
		self.__actual = nodo
		if (self.__ultimo == None):
			self.__ultimo = nodo
		
		self.__n = self.__n+1
		self.__pos = 0
		
	# Metodo para insertar al final de la lista
	def insertar_ultimo (self, valor):
		nodo = Nodo(valor)
		
		if (self.__ultimo == None):
			self.__primero = nodo
		else:
			self.__ultimo.sig = nodo

		self.__ultimo = nodo
		self.__actual = nodo
		self.__n = self.__n + 1
		self.__pos = self.__n - 1
		
	# Metodo para insertar adelanta de la posicion actual de la lista
	def insertar_actual (self, valor):

		if(self.__n == 0):
			self.insertar_inicio (valor)
			return
			
		if(self.__actual == self.__ultimo):
			self.insertar_ultimo (valor)
			return
			
		nodo = Nodo(valor)
		nodo.sig = self.__actual.sig

		self.__actual.sig = nodo
		self.__actual = nodo
		
		self.__n = self.__n + 1
		self.__pos = self.__pos + 1
		
		
	# Metodo que busca si un valor existe en la lista 
	def busca_valor (self, valor):
		
		nodo  = self.__primero
		p = 0
		while (nodo != None) :
			if (nodo.info == valor):
				return p 
			
			nodo = nodo.sig
			p = p + 1
			
		return -1
		
	# Metodo para eliminar el primer elemento de la lista
	def elimina_primero(self):
		
		if (self.__primero == None):
			return

		nodo = self.__primero
		self.__primero = nodo.sig
		del nodo 
		
		self.__n = self.__n - 1
		if (self.__n == 0):
			self.__ultimo = None

		if (self.__pos == 0):
			self.__actual = self.__primero
		else:
			self.__pos = self.__pos - 1
			
	# Metodo para vaciar la lista 
	def vacia_lista(self):
		
		num = self.__n
		for i in range(num):
			self.elimina_primero()
				

	# Metodo para ubicar en actual en la posicion "pos" (enviada por parametro)
	def pos_actual(self, pos):
		pass
		
		
	# Metodo para mostrar los elementos de la lista 
	def mostrar (self):
		
		nodo = self.__primero
		for i in range (self.__n):
			if (i == self.__pos):
				print "(",nodo.info,")", 
			else: 
				print nodo.info, 
			nodo=nodo.sig	
			
		print 
	#metodo que suma la numeros enteros en una lista	
	def sumar (self):
		nodo=self.__primero
		suma=0
		for i in range (self.__n):
			
			if (type(nodo.info)== int):
				suma=suma+nodo.info
			nodo=nodo.sig
		return suma 

	#metodo para eliminar la mitad de la lista
	def eliminar_mitad(self):
		nodo=self.__primero
		if (nodo == None):
				return
		cont=0
		mitad = self.__n / 2
		while(cont<mitad):
			cont=cont+1
			self.elimina_primero()
			nodo=nodo.sig

	#si dos listas son iguales 
	def listas_iguales(self,lista):
		if (self.__n != lista.consultar_n() ):
				return False
		nodo1 = self.__primero
		nodo2 = lista.__primero
		cont = 0
		while (nodo1 != None and nodo2 != None):
			if (nodo1.info != nodo2.info):
				return False
			nodo1 = nodo1.sig
			nodo2 = nodo2.sig
		return True
	
# PRINCIPAL 

# Crea la lista de elementos
l = Lista()

# Inserta elementos en la lista 
l.insertar_actual(5);
l.insertar_actual(10);
l.insertar_actual(15);
l.insertar_actual(20);
l.insertar_inicio(25);
l.insertar_actual(30);
l.insertar_ultimo(35);
l.mostrar()
print l.sumar();
l.eliminar_mitad();
l.mostrar(); # Muestra los elementos de la lista
