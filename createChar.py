import lvlUpCharacter,classDefine,os,createSaveCharacter,fightGenerator

v = classDefine.tank("george",10)
# v.pseudo
# ,v.lvl,v.hpbase,v.dmgBase,v.armor
w = classDefine.tank("roberto",1)
# w.pseudo,w.lvl,w.hpbase,w.dmgBase,w.armor
# print (v)
print (w)
print (repr(w))
# print repr(v)
# createSaveCharacter.save(v,w)
fightGenerator.encounter("A",w)
print (repr(w))
# lvlUpCharacter.lvlUp(v)
fightGenerator.encounter("B",w)

print (repr(w))
