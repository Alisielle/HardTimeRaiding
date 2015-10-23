import random,levelGenerator,lvlUpCharacter,time

def encounter(zone,*characters):

	iteration  = 20
	while iteration > 0:
		listEnemy = levelGenerator.genZone(zone)
		enemy = listEnemy[random.randint(0,len(listEnemy))-1]
		characters,iteration = fight(enemy,characters,iteration)
		time.sleep(5)
	
def fight(enemy,characters,iteration):
	
	aggro=[]
	vie=[]
	aliveChar = len(characters)
	enemyhp = enemy.hp
	
	for a in characters:vie.append(a.hp)
	for a in range(len(characters)):aggro.append(0) 
	while iteration > 0:
		c = 0
		for b in characters:
			if vie[c] > 0:
				dommage = b.dmg - enemy.armor
				aggro[c]+=dommage*b.aggroPerDmg
				enemyhp -= dommage
				print ("{} inflige {} points de degats à {}({} hp restant)".format(b.pseudo,dommage,enemy.nom,enemyhp))
			c+=1
		if enemyhp <= 0: break	
		d = max(aggro)
		e = [f for f,g in enumerate(aggro) if g==d]
		h = characters[e[0]]
		# Calcul des dégats
		dommage = enemy.pen
		if enemy.dmg > h.armor : dommage += enemy.dmg - h.armor
		vie[e[0]]-=  dommage
		if vie[e[0]] <= 0:
			aggro[e[0]]=0
			aliveChar -= 1
		print ("{} inflige {} points de degats à {} ({} hp restant)".format(enemy.nom,dommage,h.pseudo,vie[e[0]]))
		print("\n")
		if aliveChar == 0:
			break
		iteration -= 1
		time.sleep(1)
	
	if iteration == 0:
		print("\n\n-----------------------\nFin de la soirée de raid !\n-----------------------\n\n\n")
		return characters,iteration
	elif aliveChar:
		print("\n\n-----------------------\nVous avez Triomphé de {}! Vous recevez un objet de niveau {}\n-----------------------\n\n\n".format(enemy.nom,enemy.loot))
		lvl = []
		for a in characters:lvl.append(a.lvl)
		d = min(lvl)
		if d < enemy.loot:lvlUpCharacter.lvlUp(characters[[f for f,g in enumerate(lvl) if g==d][0]])
		return characters,iteration
	else:
		print("\n\n-----------------------\nVous avez été vaincu par {}! Revenez avec plus de stuff\n-----------------------\n\n\n".format(enemy.nom))
		return characters,iteration