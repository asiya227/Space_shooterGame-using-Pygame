import sys

import pygame
import button
import pygame
from pygame import mixer
pygame.init()

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

def Option():

  #game variables
  game_paused = False
  menu_state = "main"

  #define fonts
  font = pygame.font.SysFont("arialblack", 40)

  #define colours
  TEXT_COL = (255, 255, 255)

  #load button images
  #resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
  options_img = pygame.image.load("images/button_options.png").convert_alpha()
  quit_img = pygame.image.load("start_btn.png").convert_alpha()
  quit_img=pygame.transform.scale(quit_img, (250, 82))
  video_img = pygame.image.load('new game.png').convert_alpha()
  video_img = pygame.transform.scale(video_img, (250, 92))
  audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
  audio_img = pygame.transform.scale(audio_img, (350, 52))
  keys_img = pygame.image.load('help.png').convert_alpha()
  keys_img = pygame.transform.scale(keys_img, (310, 50))
  back_img = pygame.image.load('images/button_back.png').convert_alpha()
  back_img = pygame.transform.scale(back_img, (190, 52))
  inst = pygame.image.load('instruction 1.png').convert_alpha()
  inst = pygame.transform.scale(inst, (800, 420))

  #create button instances
  #resume_button = button.Button(304, 125, resume_img, 1)
  options_button = button.Button(297, 250, options_img, 1)
  quit_button = button.Button(299, 350, quit_img, 1)
  video_button = button.Button(240, 75, video_img, 1)
  audio_button = button.Button(205, 200, audio_img, 1)
  keys_button = button.Button(226, 325, keys_img, 1)
  back_button = button.Button(290, 450, back_img, 1)
  inst_button= button.Button(0,0,inst,1)

  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



  #game loop
  run = True
  while run:

    screen.fill((52, 78, 91))

    #check if game is paused
    if game_paused == True:
      #check menu state
      if menu_state == "main":
        #draw pause screen buttons
       # if resume_button.draw(screen):
        #  game_paused = False
        if back_button.draw(screen):
          pygame.quit()
          sys.exit()
        if options_button.draw(screen):
          menu_state = "options"
        if quit_button.draw(screen):
          run = False

      #check if the options menu is open
      if menu_state == "options":
        #draw the different options buttons
        if video_button.draw(screen):
          run=False
        if audio_button.draw(screen):
          pygame.mixer.music.stop()
          mixer.music.load('Clown.mp3')
          mixer.music.play(-1)
         # if event.type==pygame.K_2:
          #  mixer.music.load('Monkeys-Spinning-Monkeys.mp3')
           # mixer.music.play(-1)
          print("Audio Settings")
        if keys_button.draw(screen):
          menu_state="help"
        if back_button.draw(screen):
          menu_state = "main"
      if menu_state=="help":
        inst_button.draw(screen)
        if back_button.draw(screen):
          menu_state = "main"

        #print("help")
    else:
      draw_text("Press s key to start", font, TEXT_COL, 160, 250)

    #event handler
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
          game_paused = True
      if event.type == pygame.QUIT:
        run = False

    #screen.blit(inst, 200, 400)
    pygame.display.update()

Option()
pygame.quit()