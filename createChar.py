import classDefine,os,createSaveCharacter,fightGenerator

v = classDefine.tank("george",10)
# v.pseudo
# ,v.lvl,v.hpbase,v.dmgBase,v.armor
w = classDefine.tank("roberto",1)
# w.pseudo,w.lvl,w.hpbase,w.dmgBase,w.armor
print (v)
print (w)
# print repr(v)
# createSaveCharacter.save(v,w)
fightGenerator.encounter("A",w)


