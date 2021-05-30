class Magic:
    def __init__(self, nombre, descripcion, costo, damage):
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.damage = damage

    def damage_magic(self):
        return self.damage