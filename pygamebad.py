import random, pygame

width = 800
height = 600
grey = (211,211,211)
white = (255,255,255)
black = (0,0,0)
green = (100,255,100)
starting_mice = 10

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Mice')
clock = pygame.time.Clock()

class Mouse:
    def __init__(self, color):
        self.color = color
        self.x = random.randrange(0,width)
        self.y = random.randrange(0,height)
        self.size = random.randrange(7,15)
        
    def wiggle(self):
        self.move_x = random.randrange(-1,2)
        self.move_y = random.randrange(-1,2)
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0:
            self.x = 0
            
        elif self.x > width:
            self.x = width
            
        if self.y < 0:
            self.y = 0
            
        elif self.y > height:
            self.x = height
            
    def grow(self):
        gr = 1
        self.size += gr
        rd = random.randint(1,3)
        if rd == 3:
            self.size -= gr
        
def draw_environment(moose):
    game_display.fill(black)
    for mice_dict in moose:
        for mice_id in moose:
            mice = moose[mice_id]
            pygame.draw.circle(game_display, mice.color, [mice.x, mice.y], mice.size)
            mice.wiggle()
            tree = random.randint(1,15)
            if tree == 3:
                mice.grow()
                
            else:
                pass
            
    pygame.display.update()
    
    
def main():
    mice = dict(enumerate([Mouse(grey) for i in range(starting_mice)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        draw_environment(mice)
        clock.tick(30)
        
if __name__ == '__main__':
    main()