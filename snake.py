import pygame, sys, time
pygame.init()

size = (700,700)
ventana = pygame.display.set_mode(size)
pygame.display.set_caption("SNAKE by Rickrolleado")
reloj = pygame.time.Clock()

color_ventana = (0,20,0)
verde_cuadricula = (0,40,0)
verde = (0,255,0)
rojo = (255,0,0)

class CUADRICULA:
	def __init__(self, color, size, lado):
		self.color = color
		self.tamaño_vent = size
		self.lado_casilla = lado
		self.casillasx = int(self.tamaño_vent[0]/self.lado_casilla)
		self.casillasy = int(self.tamaño_vent[1]/self.lado_casilla)

	def crear_cuadricula(self):
		regla = [0,0]
		for columnas in list(range(self.casillasx)):
			pygame.draw.line(ventana,self.color,regla,[regla[0],self.tamaño_vent[1]])
			regla[0]+=self.lado_casilla

		regla = [0,0]
		for filas in list(range(self.casillasy)):
			pygame.draw.line(ventana,self.color,regla,[self.tamaño_vent[0],regla[1]])
			regla[1]+=self.lado_casilla

class SNAKE:
	def __init__(self, color, largo, lado, posx, posy):
		self.color = color
		self.largo_cola = largo
		self.dimension = lado
		self.velx = lado
		self.vely = 0
		self.posx = self.dimension * posx
		self.posy = self.dimension * posy

	def crear_snake(self):

		for parte in range(self.largo_cola):
			pygame.draw.rect(ventana, self.color, [self.posx, self.posy, self.dimension, self.dimension])
		 

	def movimiento(self):
		key = pygame.key.get_pressed()
		
		if key[pygame.K_RIGHT] and self.velx == 0:
			self.velx = 0
			self.vely = 0
			self.velx += self.dimension 
		if key[pygame.K_LEFT] and self.velx == 0:
			self.velx = 0
			self.vely = 0
			self.velx -= self.dimension 
		if key[pygame.K_UP] and self.vely == 0:
			self.velx = 0
			self.vely = 0
			self.vely -= self.dimension 
		if key[pygame.K_DOWN] and self.vely == 0:
			self.velx = 0
			self.vely = 0
			self.vely += self.dimension

		self.posx += self.velx
		self.posy += self.vely


cuadricula = CUADRICULA(verde_cuadricula,size,35)
snake = SNAKE(verde, 2, cuadricula.lado_casilla, 9, 9)


while True:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()

	ventana.fill(color_ventana)
	cuadricula.crear_cuadricula()
	snake.crear_snake()
	snake.movimiento()



	pygame.display.flip()
	reloj.tick(5)