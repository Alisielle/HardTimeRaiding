import classDefine

def lvlUp(character):
	if character.classe=="tank":lvlUpTank(character)
	elif character.classe=="cac":lvlUpCac(character)
	elif character.classe=="dist":lvlUpDist(character)
	elif character.classe=="heal":lvlUpHeal(character)

def lvlUpTank(character):
	character.lvl += 1
	character.hp += 20
	character.dmg += 1
	character.armor += 5
	
def lvlUpCac(character):
	character.lvl += 1
	character.hp += 10
	character.dmg += 3
	character.armor += 3
	
def lvlUpDist(character):
	character.lvl += 1
	character.hp += 5
	character.dmg += 2.5
	character.armor += 2
	
def lvlUpHeal(character):
	character.lvl += 1
	character.hp += 5
	character.hps += 2.75
	character.armor += 1