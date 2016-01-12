#! /usr/bin/python3

#This is the inventory problem at the end of chapter 5
#By Kyle Ziegler

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ " " + k)

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i] += 1
    return (inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
