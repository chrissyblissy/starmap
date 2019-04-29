import sys, pygame, random, globalvariables, math, missions

from globalvariables import ship

def random_position(val_max):
    return int((val_max-border)*random.random()+border)

###### change the difficulty up to 2 to make it more difficult ###### 
difficulty = 1

# dictionary of star co-ordinates
stars = {}
# screen resolution in pixels
x_res = 800
y_res = 600
# number of pixels to separate from edge
border = 10
# distance from the edge of screen that objects can be placed
x_max = x_res - border
y_max = y_res - border

star_split = 30
star_arrival_distance = 20
enemyship_arrival_distance = 35


black = 0, 0, 0
max_stars = 10
acceleration = 0.03
wait_time = 1




def main():
    #initialise pygame module and font
    pygame.init()
    

    
    #name and create logo for module
    logo = pygame.image.load("images/spaceshiplogo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("starmap")
    background = pygame.image.load("images/starfield800.png")
    background_rect = background.get_rect()

    spaceship_sprite = pygame.image.load("images/spaceshipstand.png")
    spaceship_boost = pygame.image.load("images/spaceshipboost.png")

    enemyship_sprite = pygame.image.load("images/enemyspaceship.png")
    
    star = pygame.image.load("images/star.png")
    #Create game window of size x_res and y_res

        

        
    screen = pygame.display.set_mode((x_res, y_res))
    create_stars(screen)
    playership = create_ship()
    enemyship = create_ship()

    if globalvariables.firstgame == True:
        main_menu(screen)

    while globalvariables.game_running == True:
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            globalvariables.game_running = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globalvariables.game_running = False
                
        # produces the background 
        
        screen.blit(background, background_rect)
        
               
        resources(screen)     
        draw_stars(screen, star)
        
        spaceshipmovementcheck(screen, spaceship_boost, spaceship_sprite, playership)
        enemy_ship(screen, enemyship, enemyship_sprite, playership)
        star_arrival(screen, playership)
        ship_arrival(screen, playership, enemyship)
        pygame.time.wait(wait_time)
        pygame.display.flip()
        screen.fill(black) 

def main_menu(screen):
    myfont = pygame.font.SysFont("Arial", 20)
    message_box = pygame.image.load("images/message.png")
    textsurface = myfont.render("Main Menu", False, (255, 255, 255))
    message_rect = message_box.get_rect(center=(x_max / 2, y_max / 2))
    mission_select = "ask"
    while mission_select == "ask":
        screen.blit(message_box, message_rect)
        screen.blit(textsurface, (x_max / 4, y_max / 2))
        pygame.display.flip()    
        
        
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                mission_select = "yes"
                #enemy_ship(screen, spaceship_boost, playership)
                break
            if pygame.key.get_pressed()[pygame.K_n]:
                mission_select = "no"
                break

        
def create_ship():
    # creates the player's ship using the class ship(playership.position_x, playership.position_y, bearing, playership.movement_x, playership.movement_y)
    return ship(random_position(x_max), random_position(y_max), 0, 0, 0)


#creates a dictionary of the stars and the values are (x,y) coordinates
def create_stars(screen):
    for i in range(max_stars):
        x = random_position(x_max)
        y = random_position(y_max - 50) + 50 # makes sure stars do not cover resource info
        j = 0
        while j < len(stars):           
            stars_array = stars[j]
            # ensures that the stars are spread out by at least star_split pixels
            if x < stars_array[0] + star_split and x > stars_array[0] - star_split:
                x = random_position(x_max)
                j = 0
            if y < stars_array[1] + star_split and y > stars_array[1] - star_split:    
                y = random_position(y_max - 50) + 50
                j = 0
            else:
                j += 1
        stars[i] = [x,y]
    print(stars)

#uses the stars{} dictionary to display the stars on the screen
def draw_stars(screen, star):
    for i in range(max_stars):
        star_rect = star.get_rect(center=(stars[i]))    
        screen.blit(star, star_rect)


# checks whether the ship is moving or not and calls the matching function
def spaceshipmovementcheck(screen, spaceship_boost, spaceship_sprite, playership):
    # if movement keys are pressed then it calls boost function else still function    
    if (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT]) and globalvariables.fuel > 0:
        spaceshipboost(screen, spaceship_boost, playership)
    else:
        spaceshipstill(screen, spaceship_sprite, playership)
                
def spaceshipstill(screen, spaceship_sprite, playership):
    # prepares the spaceship to be displayed to the screen
    playership.position_x += playership.movement_x
    playership.position_y += playership.movement_y

    playership.calc_bearing()
    playership.calc_border(border, y_max, x_max)
    
    spaceship_sprite = pygame.transform.rotate(spaceship_sprite, playership.bearing)
    spaceship_rect = spaceship_sprite.get_rect(center=(playership.position_x,playership.position_y))
    screen.blit(spaceship_sprite, spaceship_rect)

#creates the spaceship, rotates the image and
#moves it in the direction pressed by the player
def spaceshipboost(screen, spaceship_boost, playership):

    
    
    fuel_y = playership.movement_y
    fuel_x = playership.movement_x
              
    #checks which keys have been pressed
    if pygame.key.get_pressed()[pygame.K_UP] and pygame.key.get_pressed()[pygame.K_LEFT]:
        #rotates the spaceship picture by a set angle
        playership.bearing = 45 
        
        #moves the spaceship in the direction pressed
        playership.movement_y -= acceleration
        playership.movement_x -= acceleration
            
    elif pygame.key.get_pressed()[pygame.K_LEFT] and pygame.key.get_pressed()[pygame.K_DOWN]:
        playership.bearing = 135
        playership.movement_y += acceleration
        playership.movement_x -= acceleration
            
    elif pygame.key.get_pressed()[pygame.K_DOWN] and pygame.key.get_pressed()[pygame.K_RIGHT]:
        playership.bearing = 225
        playership.movement_y += acceleration
        playership.movement_x += acceleration
            
    elif pygame.key.get_pressed()[pygame.K_RIGHT] and pygame.key.get_pressed()[pygame.K_UP]:
        playership.bearing = 315
        playership.movement_y -= acceleration
        playership.movement_x += acceleration
            
    elif pygame.key.get_pressed()[pygame.K_UP]:
        playership.bearing = 0
        playership.movement_y -= acceleration
           
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        playership.bearing = 180
        playership.movement_y += acceleration
                   
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        playership.bearing = 270
        playership.movement_x += acceleration
                  
    elif pygame.key.get_pressed()[pygame.K_LEFT]:
        playership.bearing = 90
        playership.movement_x -= acceleration

    if fuel_y != playership.movement_y:
        globalvariables.fuel -= 1
    if fuel_x != playership.movement_x:
        globalvariables.fuel -= 1

    # checks if the spaceship is too close to the edge of the screen
    if playership.position_y < border:
        playership.position_y += y_max     
    if playership.position_y > y_max:
        playership.position_y -= y_max 
    if playership.position_x < border:
        playership.position_x += x_max
    if playership.position_x > x_max:
        playership.position_x -= x_max


        

    
    spaceship_boost = pygame.transform.rotate(spaceship_boost, playership.bearing)

    playership.position_x += playership.movement_x
    playership.position_y += playership.movement_y
    # prepares the spaceship to be displayed to the screen
    spaceship_rect = spaceship_boost.get_rect(center=(playership.position_x,playership.position_y))
    screen.blit(spaceship_boost, spaceship_rect)
    

def resources(screen):
    resourcefont = pygame.font.SysFont("Arial", 20)
    textsurface = resourcefont.render("Cash = " + str(globalvariables.cash) + "  Fuel = " + str(globalvariables.fuel), False, (255, 255, 255))
    
    screen.blit(textsurface, (10, 10))
     
def star_arrival(screen, playership):
    i = 0
    
    while i < len(stars):
        # checks if the spaceship is within arrival_distance of a star
        if playership.position_x < stars[i][0] + star_arrival_distance and playership.position_x > stars[i][0] - star_arrival_distance and playership.position_y < stars[i][1] + star_arrival_distance and playership.position_y > stars[i][1] - star_arrival_distance and i != globalvariables.last_mission:
            if abs(playership.movement_x) + abs(playership.movement_y) > 3:
                gameover(screen, "You crashed into a star and died. Press Enter to restart or Esc to quit.")
                break
            textbox(screen, i)
        else:
            i += 1

def textbox(screen, star_number):
    myfont = pygame.font.SysFont("Arial", 20)
    message_box = pygame.image.load("images/message.png")
    textsurface = myfont.render(missions.mission_list[star_number](), False, (255, 255, 255))
    message_rect = message_box.get_rect(center=(x_max / 2, y_max / 2))
    mission_select = "ask"
    while mission_select == "ask":
        screen.blit(message_box, message_rect)
        screen.blit(textsurface, (x_max / 4, y_max / 2))
        pygame.display.flip()    
        
        
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                mission_select = "yes"
                #enemy_ship(screen, spaceship_boost, playership)
                break
            if pygame.key.get_pressed()[pygame.K_n]:
                mission_select = "no"
                break


    globalvariables.last_mission = star_number
 #   print("Last mission was :  ", globalvariables.last_mission)

def gameover(screen, message):
    myfont = pygame.font.SysFont("Arial", 20)
    message_box = pygame.image.load("images/message.png")
    textsurface = myfont.render(message, False, (255, 255, 255))
    message_rect = message_box.get_rect(center=(x_max / 2, y_max / 2))
    mission_select = "ask"
    while mission_select == "ask":
        screen.blit(message_box, message_rect)
        screen.blit(textsurface, (x_max / 4, y_max / 2)) 
        pygame.display.flip()    
        
        
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                mission_select = "yes"
                restart()
                break
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                mission_select = "no"
                globalvariables.game_running = False
                break

def restart():
    globalvariables.cash = globalvariables.newgamecash
    globalvariables.fuel = globalvariables.newgamefuel
    globalvariables.game_running = True
    globalvariables.last_mission = 11
    globalvariables.firstgame = False
    main()

def enemy_ship(screen, enemyship, enemyship_sprite, playership):
    max_speed = 50 # gives the maximum speed the enemyship can reach
    adjustment = 0.7 * difficulty  # changes how quickly the enemyship can change direction
    if enemyship.total_movement() < max_speed * 2:
        if enemyship.position_y < playership.position_y:
            if abs(enemyship.movement_y) > abs(playership.position_y - enemyship.position_y):
                enemyship.movement_y -= adjustment
            else:
                enemyship.movement_y += adjustment
        if enemyship.position_y > playership.position_y:
            if abs(enemyship.movement_y) > abs(playership.position_y - enemyship.position_y):
                enemyship.movement_y += adjustment
            else:
                enemyship.movement_y -= adjustment
        if enemyship.position_x < playership.position_x:
            if abs(enemyship.movement_x) > abs(playership.position_x - enemyship.position_x):
                enemyship.movement_x -= adjustment
            else:
                enemyship.movement_x += adjustment    
        if enemyship.position_x > playership.position_x:
            if abs(enemyship.movement_x) > abs(playership.position_x - enemyship.position_x):
                enemyship.movement_x += adjustment
            else:
                enemyship.movement_x -= adjustment
    else:
        if enemyship.movement_x >= max_speed:
            enemyship.movement_x -= adjustment * 2
        elif enemyship.movement_x <= - max_speed:
            enemyship.movement_x += adjustment * 2
        if enemyship.movement_y >= max_speed:
            enemyship.movement_y -= adjustment * 2
        elif enemyship.movement_y <= - max_speed:
            enemyship.movement_y += adjustment * 2

    enemyship.calc_bearing()
    enemyship.calc_border(border, y_max, x_max)
    
    enemyship.position_x += enemyship.movement_x / 20
    enemyship.position_y += enemyship.movement_y / 20
    
    enemyship_sprite = pygame.transform.rotate(enemyship_sprite, enemyship.bearing)
    spaceship_rect = enemyship_sprite.get_rect(center=(enemyship.position_x,enemyship.position_y))
    screen.blit(enemyship_sprite, spaceship_rect)
    
def ship_arrival(screen, playership, enemyship):

    # checks if playership has crashed into enemyship
    if playership.position_x < enemyship.position_x + enemyship_arrival_distance and playership.position_x > enemyship.position_x - enemyship_arrival_distance and playership.position_y < enemyship.position_y + enemyship_arrival_distance and playership.position_y > enemyship.position_y - enemyship_arrival_distance:
        gameover(screen, "The enemy ship crashed into you and exploded. Press Enter to restart or Esc to quit.")

        
def mission0():

    while True:
        
        break
        
    globalvariables.cash += 50
    
 #   mission_list.remove(mission0)
    return "You arrive at a large, rust-coloured planet with a large ring around it. The locals explain that the rocks in the rings were formed in a supernova and contain high amounts of platinum. Do you want to go for a dig? 0 "




# no missions left to complete
def endmission():
    globalvariables.fuel += 10
    return "All missions complete!"


main()
pygame.quit()
