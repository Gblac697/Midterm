
#Player's vaule
class chara_trait:
    def __init__ (self, health, arm):
        self.health = health
        self.arm = arm
        self.inventory = []
        
    #actions for player to use
    def throw(self, rope, boat):
     print("you throw the rope on the boat")
     if rope in self.inventory and self.arm >3:
         print("You got the boat")
         self.inventory.append(boat)
     elif rope.speed < 3:
        print("You can not reach the boat")
     else:
         print("you failed to throw")
         
    def route(self, map):
        if map in self.inventory:
            print("You have found da Way!")
        else:
            print("You are lost")
            pass
    
    def sail(self,boat):
        if boat in self.inventory:
            print("You sail home. You WIN!")
        else:
            print("You cannot")
            pass
 
player_one = chara_trait(100,10)

#items and their vaules
class items_used:
    def __init__(self, stregth, weight, speed, ):
        self.stregth = stregth
        self.weight = weight
        self.speed = speed 

map = items_used(1,1,10,)
rope = items_used(2,2,5)
boat = items_used(20,10,12)
#start the game
def player_spawn(player_one):

    print("You are lost in forest.")
    print("you see three paths ahead")
    print("North is the Mountain, West to the Lake, East to the Valley.")

    choice = input("Onward. (North/West/East): ").lower()
    
    if choice == "north":
        mountain()
    elif choice == "west":
        lake()
    elif choice == "east":
        valley()
    else:
        print("You failed that")
        return player_spawn(player_one)
  #Forest return area     
def forest():
    print("You are back in the forest")
    print("Nothing has changed")

    choice = input("Onward. (North/West/East): ").lower()
    
    if choice == "north":
        mountain()
    elif choice == "west":
        lake()
    elif choice == "east":
        valley()
    else:
        print("You failed that")
        return forest()
#area example Maybe change to class.
def mountain():
    print("You arrive at the Mountain")
    print("You see a House and some rock")
    print("Along with two road to the lake and valley")
    if rope in player_one.inventory:
     pass
    else:
     print("You see a rope hang tree")
    
    choice = input("Now what? (Head Back/Enter House/ Climb the Rocks/ Go to lake/ Go to valley): ").lower()

    if choice == "go to valley":
        print("To the Valley")
        valley()
    elif choice == "go to lake":
        print("To the Lake")
        lake()
    elif choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "enter house":
        house()
    elif choice == "climb the rocks":
        print("rock time")
        print('You climb to a cliff edge. You meet God and become wise.')
        print('Now you do not need to escape. Game Over!')
    elif choice == "pick up rope" or "grab rope":
        print ("You try to grab the rope")
        if rope in player_one.inventory:
            print("You have that")
            return mountain()
        elif rope not in player_one.inventory: 
             print("you grab rope.")
             player_one.inventory.append(rope)
             return mountain()
        else:
            pass
    else:
        print("You know you are wrong")
        return mountain() #loop if input is inncorrect
    
def house():
    print("You enter the house")
    if map in player_one.inventory:
     pass
    else:
     print("You see a map")
     pass
    choice = input("Now what? (Head back)").lower()

    if choice == "head back":
        print("You go back")
        mountain()
    elif choice == "grab map" or "pick up map":
        player_one.inventory.append(map)
        print("You grab the map")
        return house()
    else:
        print("You know you are wrong")
        return house()
        
#lake location
def lake():
    print('You arrive at the Lake.')
    print("You see a road to the Mountain.")
    if boat in player_one.inventory:
        pass
    else:
     print("You see a boat floating.")
    
    choice = input("(Head Back/go to road):").lower()
    if choice == "throw rope":
        player_one.throw(rope,boat)
        pass
    else:
        pass


    if choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "go to road":
        print("You walk up the road.")
        mountain()
    elif choice == "sail home":
        player_one.sail(boat)
        finish_line()
    else:
        print("You know you are wrong.")
        return lake()
    
   
 #Valley area   
def valley():
    print("You arrive to the Valley.")
    print("It is a sea of green grass")
    if map in  player_one.inventory:
        print("The map shows da way")
        pass
    else:
        pass

    choice = input("(head back/Take Road to mountain/Go to the Green Sea):").lower()
    if choice == "head back":
        print("You go back to Forest")
        forest()
    elif choice == "take road to mounatain":
        mountain()
    elif choice == "go da way":
        print("You found da way")
        finish_line()
    elif choice == "go to the green sea":
        print("You walk into the sea lost forever. GAME OVER")
    else:
        print("You know You are wrong")
        return valley()
    
def finish_line():
     print("You are the Master of Game.")
     stop()
#game start
def stop():
    print({})
    
if __name__ == "__main__":
    player_one = chara_trait(100,10)
    player_spawn(player_one)
   