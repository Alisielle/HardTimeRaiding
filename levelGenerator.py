class lvl:
	
	def __init__(self,nom,hp,pen,dmg,armor,loot):
		self.nom = nom
		self.hp = hp
		self.pen = pen
		self.dmg = dmg
		self.armor = armor
		self.loot = loot
		
def genZone(zone):
		
	if zone == "A":
		return [lvl("GnollA",72,2,5,8,10),lvl("MurlocA",54,6,14,4,10),lvl("KoboldA",39,5,12,3,10)]
	if zone == "B":
		return [lvl("GnollB",142,4,10,16,20),lvl("MurlocB",108,12,28,8,20),lvl("KoboldB",78,10,24,6,20)]
	
		
		