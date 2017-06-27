'''

Name: Pong
Author: Gordon Stirling

Tutorial 1: An introduction to pygame - The Basics
In this tutorial we will just be getting pygame up and running.  
Our goal is a small template that produces a blank window that 
doesn’t hang that we can close with the window X or by pressing 
escape.  Additionally we want to put our frames per second in 
the title bar, just for good measure.

'''

# import modules and check pygame has loaded successfully.
try:
    import pygame, sys
    from pygame.locals import *

except ImportError as err:
    ''' Implement some simple error handling in case pygame hasn't loaded. '''
    print ("%s Failed to load module: %s" % (__file__, err))
    sys.exit(1)

class Game(object):
    ''' Our game object! This is a fairly simple object that handles the 
    initialisation of pygame and sets up our game to run. '''


    def __init__(self):
        ''' Called when the Game object is initialised.  
        Initialises pygame and sets up our pygame window 
        and other pygame tools that we will need for more 
        complicated tutorials '''

        # load and set up pygame
        pygame.init()

        # create our surface (window)
        self.WINSURF = pygame.display.set_mode((800, 600))

        # clock for ticking
        self.clock = pygame.time.Clock()

        # set the window title
        pygame.display.set_caption("Pygame Tutorial 1 - Basics")

        # tell pygame to only pay attention to certain events
        # we want to know if the user hits the X on the window, and we
        # want keys so we can close the window with the esc key
        pygame.event.set_allowed([QUIT, KEYDOWN])


    def run(self):
        ''' Runs the game.  Contains the game loop that computes and renders 
        each frame '''

        print ("Starting Event Loop")

        is_running = True

        # run until something tells us to stop
        while is_running:

            # tick pygame clock
            # you can limit the FPS by passing the desired frames per second to tick()
            self.clock.tick(60)

            # handle pygame events - if user closes the game, stop running
            is_running = self.handleEvents()

            # update the title bar with our frames per second
            pygame.display.set_caption('Pygame Tutorial 1 - Basic | FPS: ' + str( int(self.clock.get_fps()) ))

            # render the screen, even though we don't have anything going on right now
            pygame.display.flip()

        print ("Quitting.  Thanks for playing")
        
        pygame.quit()
        sys.exit()


    def handleEvents(self):
        ''' Poll for pygame events and behave accordingle.  Return false to stop
        the event loop and end the game '''

        # poll for pygame events
        for event in pygame.event.get():
            if event.type == QUIT:
                return False

            # handle user input
            elif event.type == KEYDOWN:
                # if the user presses escape, quit the event loop
                if event.key == K_ESCAPE:
                    return False

        return True

# create a game and run it
if __name__ == '__main__':
    game = Game()
    game.run()