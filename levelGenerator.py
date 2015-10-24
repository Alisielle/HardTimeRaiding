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
		return [lvl("GnollA",88,5,30,4,10),lvl("MurlocA",67,9,40,2,10),lvl("KoboldA",80,7,35,1.5,10)]
	if zone == "B":
		return [lvl("GnollB",176,10,60,8,20),lvl("MurlocB",134,18,80,4,20),lvl("KoboldB",160,14,70,3,20)]
	if zone =="C":
		return[lvl()]
	
		
		