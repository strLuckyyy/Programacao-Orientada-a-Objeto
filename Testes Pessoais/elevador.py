import os
import math

class Test:
	def __init__(self, altura: float, largura: float, profundidade: float):
		self.altura_elevador = altura
		self.largura_elevador = largura
		self.profundidade_elevador = profundidade
		
		self.largura_porta_elevador = largura
		
		self.altura_movel = altura
		self.largura_movel = largura
		self.grossura_movel = profundidade
		
	
	def tamanho_movel(self, movel):
			list3d = []
			
			list3d.append(movel.altura_movel)
			list3d.append(movel.largura_movel)
			list3d.append(movel.grossura_movel)
			
			return list3d
			
	
	def tamanho_elevador(self, elevador, porta):
			i = []
			
			i.append(elevador.altura_elevador)
			i.append(elevador.largura_elevador) 
			i.append(elevador.profundidade_elevador)
			i.append(porta.largura_porta_elevador)
			
			return i	
								
	def trignometria_elevador(self, elev, list_elev):
			porta_diagonal = math.sqrt(list_elev[3] ** 2 + list_elev[0] ** 2)
			
			diagonal_lateral_elev = math.sqrt(list_elev[0] ** 2 + list_elev[1] ** 2)
			
			diagonal_profunda_elev = math.sqrt(list_elev[0] ** 2 + list_elev[2] ** 2)
			
			print(
			f'A diagonal da porta do elevador mede {porta_diagonal}\n',
			f'A diagonal do elevador, com base na largura, mede {diagonal_lateral_elev}',
			f'A diagonal do elevador, com base na profundidade, mede {diagonal_profunda_elev}'
			)
			
			
		
	
def decidir_passagem(movel, porta, ambiente):
	pass
	
	
def main():
	os.system('cls')
	
	vidro = Test(270, 160, 5)
	v1 = vidro.tamanho_movel(vidro)
	
	elevador = Test(250, 145, 228)
	porta = Test(250, 120, 0)
	
	e1 = elevador.tamanho_elevador(elevador, porta)
	elevador.trignometria_elevador(elevador, e1)
	
	
if __name__ == '__main__':
	main()
	