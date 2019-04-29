import random, globalvariables
#from starmap import screen

#class missions():

      
def mission0():
    globalvariables.fuel += 100
    globalvariables.cash += 50
 #   mission_list.remove(mission0)
    return "You arrive at a large, rust-coloured planet with a large ring around it. The locals explain that the rocks in the rings were formed in a supernova and contain high amounts of platinum. Do you want to go for a dig? 0 "
def mission1():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 1 "
def mission2():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 2 "
def mission3():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 3 "
def mission4():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 4 "
def mission5():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 5 "
def mission6():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 6 "
def mission7():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 7 "
def mission8():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 8 "
def mission9():
    globalvariables.cash += 50
    globalvariables.fuel += 100
    return "You're at a star! 9 "

# no missions left to complete
def endmission():
    globalvariables.fuel += 10
    return "All missions complete!"

# a list of every mission
mission_list = [mission0, mission1, mission2, mission3, mission4, mission5, mission6, mission7, mission8, mission9]

