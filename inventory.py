## Fantasy Game Inventory
# Name: Display inventory
# Description: Data structure to model player's inventory
# Input: inventory must be a dictionary, dragonLoot must be list

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += inventory[k]
    print('Total number of items = ' + str(item_total))

def addToInventory(inventory, addedItems):
    for i in range(0,len(addedItems)):
        if addedItems[i] not in inventory:
            inventory.setdefault(addedItems[i],1)
        else:
            inventory[addedItems[i]] += 1
    return inventory
            
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','dagger']
inventory = {'gold coin': 42, 'rope': 1}
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)
        
    
