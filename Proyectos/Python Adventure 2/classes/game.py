class Personaje:
	def __init__(self, nombre, vida, mana, ataque, defensa, habilidades, magia):
		self.nombre = nombre
		self.vida = vida
		self.mana = mana
		self.ataque = ataque
		self.defensa = defensa
		self.habilidades = habilidades
		self.magia = magia

	def damage(self):
		self.vida -= (self.ataque - self.defensa)
		return self.vida

	def damage_mundo(self, damage):
		self.vida -= damage
		return self.vida

	def cura_evento(self, comida):
		self.vida += comida
		return self.vida

class Ubicacion:
	def __init__(self, lugar, cordenada, descripcion):
		self.lugar = lugar
		self.cordenada = cordenada
		self.descripcion = descripcion

	def preguntar_desc(self):
		return self.descripcion
	
	def preguntar_lug(self):
		return self.lugar
	
	def preguntar_cor(self):
		return self.cordenada