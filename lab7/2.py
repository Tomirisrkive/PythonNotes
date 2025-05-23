import pygame 
pygame.init()
pygame.mixer.init()

width = 1000
height = 1000
color_white = (255,255,255)
screen = pygame.display.set_mode((width,height))

songs = [
    "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/audio/Drake_One_Dance.mp3",
    "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/audio/Duke_Dumont_Ocean_Drive.mp3",
    "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/audio/Eminem_Lose_Yourself.mp3",
    "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/audio/Rihanna_Diamonds.mp3",
    "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/audio/Timbaland_Apologize.mp3",
    "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab7/audio/WILLOW_Wait_a_Minute!.mp3"
]


# function for next song 
def next_song():
    global songs
    songs = songs[1:] + [songs[0]] # putting current song to the back of the list
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

# function for previous song
def previous_song():
    global songs
    songs = [songs[-1]] + songs[:-1] # putting the last-played song to the front of list
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

paused = False 

def stopping():
    global paused
    paused = not paused
    if paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

clock = pygame.time.Clock()
FPS = 60

song_end = pygame.USEREVENT + 1 
pygame.mixer.music.set_endevent(song_end)

pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            if event.key == pygame.K_LEFT:
                previous_song()
            if event.key == pygame.K_SPACE:
                stopping()
        if event.type == song_end:
            next_song()
        screen.fill(color_white)
    pygame.display.flip()
    clock.tick(FPS)