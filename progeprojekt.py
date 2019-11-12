import pygame
pygame.init()
 
size = (800, 800)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Seiklus Donaldiga")
 
# tsükklis kuni kinni pannakse
done = False
 
#kui kiiresti pilt uuendatakse?
clock = pygame.time.Clock()
background_image = pygame.image.load("square-starfield.jpg").convert()
pygame.mixer.music.load("senorita.mp3")
pygame.mixer.music.play() 
# terve mängu tsükkel
while not done:
    # programm ise
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
#mängu loogika siia:
    screen.blit(background_image, [0,0])
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()