class tank:
	
	"""hpBase = 100
	hpPerLvl = 20
	dmgBase = 10
	dmgPerLvl = 1
	hpsBase = 0
	hpsPerLvl = 0
	armorBase = 20
	armorPerLvl = 5
	avoidance = 0.2
	aggroPerDmg = 3"""
	
	def __init__(self,pseudo,lvl):
		self.pseudo = pseudo
		self.lvl = lvl
		self.hp = 100+20*lvl
		self.dmg = 10+lvl*1
		self.hps = 0
		self.armor = 20+lvl*5
		self.avoidance = 0.2
		self.aggroPerDmg = 3
		self.classe = "tank"
		
	def __repr__(self):
		return "\"Tank\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\"".format(self.pseudo,self.lvl,self.hp,self.dmg,self.hps,self.armor,self.avoidance,self.aggroPerDmg)
		
	def __str__(self):
		return "Charactere Tank: Pseudo({}),lvl ({})".format(self.pseudo,self.lvl)
		

class cac:
	
	"""hpBase = 80
	hpPerLvl = 10
	dmgBase = 30
	dmgPerLvl = 3
	hpsBase = 0
	hpsPerLvl = 0
	armorBase = 10
	armorPerLvl = 3
	avoidance = 0.25
	aggroPerDmg = 0.8"""
	
	def __init__(self,pseudo,lvl):
		self.pseudo = pseudo
		self.lvl = lvl
		self.hp = 80+10*lvl
		self.dmg = 30+lvl*3
		self.hps = 0
		self.armor = 10+lvl*3
		self.avoidance = 0.25
		self.aggroPerDmg = 0.8
		self.classe = cac
		
	def __repr__(self):
		return "\"Cac\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\"".format(self.pseudo,self.lvl,self.hp,self.dmg,self.hps,self.armor,self.avoidance,self.aggroPerDmg)
		
	def __str__(self):
		return "Charactere Cac: Pseudo({}),lvl ({})".format(self.pseudo,self.lvl)

		
class dist:
	
	"""hpBase = 60
	hpPerLvl = 5
	dmgBase = 25
	dmgPerLvl = 2.5
	hpsBase = 0
	hpsPerLvl = 0
	armorBase = 7
	armorPerLvl = 2
	avoidance = 0.2
	aggroPerDmg = 0.7"""
	
	def __init__(self,pseudo,lvl):
		self.pseudo = pseudo
		self.lvl = lvl
		self.hp = 60+5*lvl
		self.dmg = 25+lvl*2.5
		self.hps = 0
		self.armor = 7+lvl*2
		self.avoidance = 0.2
		self.aggroPerDmg = 0.7
		self.classe = dist
		
	def __repr__(self):
		return "\"Dist\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\"".format(self.pseudo,self.lvl,self.hp,self.dmg,self.hps,self.armor,self.avoidance,self.aggroPerDmg)
		
	def __str__(self):
		return "Charactere Dist: Pseudo({}),lvl ({})".format(self.pseudo,self.lvl)
	
class heal:
	
	"""hpBase = 50
	hpPerLvl = 5
	dmgBase = 0
	dmgPerLvl = 0
	hpsBase = 50
	hpsPerLvl = 2.75
	armorBase = 5
	armorPerLvl = 1
	avoidance = 0.1
	aggroPerDmg = 0.5"""
	
	def __init__(self,pseudo,lvl):
		self.pseudo = pseudo
		self.lvl = lvl
		self.hp = 50+5*lvl
		self.dmg = 0
		self.hps = 50+lvl*2.75
		self.armor = 5+lvl*1
		self.avoidance = 0.1
		self.aggroPerDmg = 0.5
		self.classe = heal
		
	def __repr__(self):
		return "\"Heal\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\";\"{}\"".format(self.pseudo,self.lvl,self.hp,self.dmg,self.hps,self.armor,self.avoidance,self.aggroPerDmg)
		
	def __str__(self):
		return "Charactere Heal: Pseudo({}),lvl ({})".format(self.pseudo,self.lvl)
	
