class Skills:
    def __init__(self, nombre, descripcion, costo, damage):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.damage = damage
    
    def damage_skill(self):
        return self.damage