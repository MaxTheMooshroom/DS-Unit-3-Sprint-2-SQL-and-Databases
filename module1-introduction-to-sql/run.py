import sql_api as sqla

rpg = sqla.Database('rpg_db.sqlite3')

print('\n\nHow many total Characters are there?',                                                   #Q1
      str(len(rpg.get_all("charactercreator_character"))) + '!\n\n')

#---------------------------------------------------------------

print('How many of each specific subclass?')                                                        #Q2

print(f'    Cleric: {len(rpg.get_all("charactercreator_cleric"))}')
print(f'    Fighter: {len(rpg.get_all("charactercreator_fighter"))}')
print(f'    Mage: {len(rpg.get_all("charactercreator_mage"))}')
print(f'    Thief: {len(rpg.get_all("charactercreator_thief"))}')
print(f'    Necromancer: {len(rpg.get_all("charactercreator_necromancer"))}\n\n')

#---------------------------------------------------------------

itemcount = len(rpg.get_all("armory_item"))
print(f'How many total items? {itemcount}\n\n')                                                     #Q3

#---------------------------------------------------------------

weaponcount = len(rpg.get_all("armory_weapon"))
print('How many of the Items are weapons? How many are not?')                                       #Q4
print(f'    Are: {weaponcount}')
print(f'    Aren\'t: {itemcount - weaponcount}\n\n')

#---------------------------------------------------------------

ids = [inv[0] for inv in rpg.get_all("charactercreator_character")]
names = [inv[1] for inv in rpg.get_all("charactercreator_character")]
invcounts = []

for id in ids[:20]:
    result = rpg.fetchall(f'SELECT * FROM charactercreator_character_inventory as inv WHERE inv.character_id = {id}')
    invcounts.append(len(result))

print('How many Items does each character have? (first 20):')                                       #Q5
for i in range(0, 20):
    print(f'    {names[i]}: {invcounts[i]}')

print('\n')

#---------------------------------------------------------------

weapon_ids = [iids[0] for iids in rpg.get_all("armory_weapon")]

print('How many Weapons does each character have? (first 20):')                                     #Q6

for i, id in enumerate(ids[:20]):
    result = rpg.fetchall(f'SELECT item_id FROM charactercreator_character_inventory as inv WHERE inv.character_id = {id}')
    
    weapon_count = 0

    for item_id in result:
        if item_id[0] in weapon_ids:
            weapon_count += 1

    print(f'    {names[i]}: {weapon_count} weapons!')
print('\n')

#---------------------------------------------------------------

invcounts = []
for id in ids:
    result = rpg.fetchall(f'SELECT * FROM charactercreator_character_inventory as inv WHERE inv.character_id = {id}')
    invcounts.append(len(result))

print(f'On average, how many Items does each Character have: {sum(invcounts) / len(invcounts)}\n\n')#Q7  

#---------------------------------------------------------------

weaponcounts = []

for i, id in enumerate(ids[:20]):
    result = rpg.fetchall(f'SELECT item_id FROM charactercreator_character_inventory as inv WHERE inv.character_id = {id}')
    
    weapon_count = 0

    for item_id in result:
        if item_id[0] in weapon_ids:
            weapon_count += 1
    weaponcounts.append(weapon_count)

print(f'On average, how many Weapons does each character have?:',                                   #Q8
      sum(weaponcounts) / len(weaponcounts))




#---------------------------------------------------------------
"""
    Section 2
"""

buddy = sqla.Database('Buddy.db')

#---------------------------------------------------------------

print('Count how many rows you have:', len(buddy.get_all('users')), '\n\n')

#---------------------------------------------------------------

names = []

results = buddy.fetchall(f'SELECT * FROM users')

for i, result in enumerate(results):
    if result[5] > 100 and result[7] > 100:
        names.append(result[0])

print('How many users who reviewed at least 100 Nature in the category ' + 
     f'also reviewed at least 100 in the Shopping category: {len(names)}\n\n')

#---------------------------------------------------------------

container = []

for i in range(2,8):
    col = [pos[i] for pos in results]
    container.append(sum(col) / len(col))

print('What are the average number of reviews for each category?\n' +
     f'    Sports: {container[0]}\n    Religious: {container[1]}\n' +
     f'    Nature: {container[2]}\n    Theatre: {container[3]}\n' + 
     f'    Shopping: {container[4]}\n    Picnic: {container[5]}\n\n')

