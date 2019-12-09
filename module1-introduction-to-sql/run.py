import sql_api as sqla

rpg = sqla.Database('rpg_db.sqlite3')

print(f'How many total Characters are there? {len(rpg.get_all("charactercreator_character"))}!\n')  #Q1

print('How many of each specific subclass?\n')                                                      #Q2

print(f'    Cleric: {len(rpg.get_all("charactercreator_cleric"))}')
print(f'    Fighter: {len(rpg.get_all("charactercreator_fighter"))}')
print(f'    Mage: {len(rpg.get_all("charactercreator_mage"))}')
print(f'    Thief: {len(rpg.get_all("charactercreator_thief"))}')
print(f'    Necromancer: {len(rpg.get_all("charactercreator_necromancer"))}\n\n')

itemcount = len(rpg.get_all("armory_item"))
print(f'How many total items? {itemcount}\n\n')                                                     #Q3

weaponcount = len(rpg.get_all("armory_weapon"))
print('How many of the Items are weapons? How many are not?\n')                                     #Q4
print(f'    Are: {weaponcount}')
print(f'    Aren\'t: {itemcount - weaponcount}\n\n')

print('How many Items does each character have? (first 20):\n' +                                    #Q5
     f'{[len(inv) for inv in rpg.get_all("charactercreator_character_inventory")[:20]]}\n\n')


