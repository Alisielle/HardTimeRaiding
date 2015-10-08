class lvl:
	
	def __init__(self,nom,hp,pen,dmg,armor):
		self.nom = nom
		self.hp = hp
		self.pen = pen
		self.dmg = dmg
		self.armor = armor
		
def genZone(zone):
		
	if zone == "A":
		return [lvl("A1",72,2,5,8),lvl("A2",54,6,14,4),lvl("A3",39,5,12,3)]
	
		
		