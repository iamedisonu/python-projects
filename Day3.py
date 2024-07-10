print("Welcome to Treasure Island.\nyour mission is to find the treasure ")

m=str(input("you are at a cross road where do you want to go? left or right? "))

if m=="left":
    
    n=str(input("you come to a lake. there is an island in the middle of the lake. type \"swim\" to swim accross or \"wait\" to wait "))
    if n== "wait":
        print("which door?") #Here adding more description could be good to make game fun. Concept gainned
        p=str(input("Red or Blue: "))
        if p=="Red":
            print("Burned by fire.\nGame over.")
        elif p== "Yellow":
            print("You Win")
        elif p=="Blue":
            print("Eaten by beasts.\n Game Over.")
        else:
            print("Game Over.")
    else:
        print("attacked by trout. \nGame Over.")
        
    
else:
    print("Fall into a hole Game over")
    
