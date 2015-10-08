import random,levelGenerator

def encounter(zone,*characters):
	iteration  = 20
	listEnemy = levelGenerator.genZone(zone)
	enemy = listEnemy[random.randint(0,len(listEnemy))]
	fight(enemy,characters,iteration)
	
def fight(enemy,characters,iteration):
	aggro=[]
	for a in range(len(characters)):aggro.append(0) 
	while iteration > 0:
		c = 0
		for b in characters:
			dommage = b.dmg - enemy.armor
			aggro[c]+=dommage*b.aggroPerDmg
			print "{} inflige {} points de degats".format(b.pseudo,dommage)
			
		d = max(aggro)
		e = [f for f,g in enumerate(aggro) if g==d]
		h = charaters[e]
		# Calcul des dégats
		print "{} inflige {} points de degats".format(h.nom,dommage)
		c+=1
	
	


# zoneA = levelGenerator.genZoneA()