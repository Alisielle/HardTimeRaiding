import random,levelGenerator,lvlUpCharacter,time

def encounter(zone,*characters):

	iteration  = 40
	vie=[]
	for a in characters:vie.append(a.hp)
	while iteration > 0:
		listEnemy = levelGenerator.genZone(zone)
		enemy = listEnemy[random.randint(0,len(listEnemy))-1]
		characters,iteration,vie = fight(enemy,characters,iteration,vie)
		time.sleep(5)
	
def fight(enemy,characters,iteration,vie):
	
	aggro=[]
	
	aliveChar = len(characters)-vie.count(0)
	enemyhp = enemy.hp
	

	for a in range(len(characters)):aggro.append(0) 
	while iteration > 0:
		iteration -= 1
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
		if random.randint(1,10)/10 > h.avoidance:
			dommage = enemy.pen
			if enemy.dmg > h.armor : dommage += enemy.dmg - h.armor
			vie[e[0]]-=  dommage
			if vie[e[0]] <= 0:
				vie[e[0]]=0
				aggro[e[0]]=0
				aliveChar -= 1
			print ("{} inflige {} points de degats à {} ({} hp restant)".format(enemy.nom,dommage,h.pseudo,vie[e[0]]))
			print("\n")
			if aliveChar == 0:
				break
		else:
			print("{} equive l'attaque de {}\n".format(h.pseudo,enemy.nom))
		
		time.sleep(0.5)
	
	if iteration == 0:
		print("\n\n-----------------------\nFin de la soirée de raid !\n-----------------------\n\n\n")
		return characters,iteration,vie
	elif aliveChar:
		rint("\n\n-----------------------\nVous avez Triomphé de {}! \n".format(enemy.nom,e.pseudo))
		lvl = []
		for a in characters:lvl.append(a.lvl)
		d = min(lvl)
		e = characters[[f for f,g in enumerate(lvl) if g==d][0]]
		if d < enemy.loot:
			if d+10>enemy.loot:	lvlUpCharacter.lvlUp(e)
			else:
				for i in range(0,int(enemy.loot/10-d/10)):lvlUpCharacter.lvlUp(e)
			print("{} recoit un objet de niveau {}\n-----------------------\n\n\n".format(enemy.loot))
		return characters,iteration,vie
	else:
		print("\n\n-----------------------\nVous avez été vaincu par {}! \nRevenez avec plus de stuff\n-----------------------\n\n\n".format(enemy.nom))
		return characters,0,vie