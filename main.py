import pygame
import random
import time
#every game need to have a game window

#before creating pygame we need to initialize pygame and create window
pygame.init()


width=800
height=600
#display module pygame library set_mode function
#width and height in the form of coordinates
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

w=(255,255,255)
b=(0,0,0)
r=(255,0,0)
g=(0,255,0)
#window disappears so use
over=False
#listens for an event
x1=width/2
y1=height/2
snake_body=[]
#if we keep x1,y1 only then we would not be able to increase the size of snake so maintain a list of values

change_x=0
change_y=0

foodx=round(random.randrange(0,width-10)/10)*10.0
foody=round(random.randrange(0,height-10)/10)*10.0

length=1
score=0


#to control the movement rate of snake we need to use clock pygame also comes with clock 
clk=pygame.time.Clock()




while not over:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            over=True
        #movement of snake
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                change_x=-10
                change_y=0
            elif i.key==pygame.K_RIGHT:
                change_x=10
                change_y=0
            elif i.key==pygame.K_UP:
                change_x=0
                change_y=-10
            elif i.key==pygame.K_DOWN:
                change_x=0
                change_y=10
    x1=x1+change_x
    y1=y1+change_y
    #checking boundary conditions when hitting boundaries quit the game

    if x1>=width or x1<0 or y1>=height or y1<0:
        window.fill(b)
        font=pygame.font.SysFont(None,90)
        font1=pygame.font.SysFont(None,50)
        font2=pygame.font.SysFont(None,30)
        text=font.render("You Lost the Game",True,w)
        text2=font2.render("Snake hit the boundary",True,w)
        text1=font1.render("Your Score : "+str(score),True,w)
        window.blit(text,(100,100))
        window.blit(text2,(250,170))
        window.blit(text1,(250,200))
        pygame.display.update()
        time.sleep(2)
        over=True
    #remove the old square and add new one
    window.fill(b)
    snake_head=[]
    snake_head.append(x1)
    snake_head.append(y1)

    snake_body.append(snake_head)

    if len(snake_body)>length:
        del snake_body[0]

    #snake hitting itself
    for i in snake_body[:-1]:
        if i==snake_head:
            window.fill(b)
            font=pygame.font.SysFont(None,90)
            font2=pygame.font.SysFont(None,30)
            font1=pygame.font.SysFont(None,50)
            text=font.render("You Lost the Game",True,w)
            text2=font2.render("Snake hit it's head",True,w)
            text1=font1.render("Your Score : "+str(score),True,w)
            window.blit(text,(100,100))
            window.blit(text2,(250,170))
            window.blit(text1,(250,200))
            pygame.display.update()
            time.sleep(2)
            over=True

    #displaying score to do that we fix the font
    font=pygame.font.SysFont(None,50)
    text=font.render("Score : "+str(score),True,w)
    window.blit(text,(10,10))


    #eating food
    if x1==foodx and y1==foody:
        foodx=round(random.randrange(0,width-10)/10)*10.0
        foody=round(random.randrange(0,height-10)/10)*10.0
        length=length+1
        score=score+1
        
    #adding food item
    #keep ar random position
    pygame.draw.rect(window,r,[foodx,foody,10,10])


    #creating a snake
    #small square box
    #on which place need to draw ,color ,rectangle value-->x left,y top,width,height400
    #pygame.draw.rect(window,w,[x1,y1,10,10])
    #update window
    o=len(snake_body)
    y=0
    for i in snake_body:
        if y==o-1:
            pygame.draw.rect(window,g,[i[0],i[1],10,10])
            y=y+1
        else:
            pygame.draw.rect(window,w,[i[0],i[1],10,10])
            y=y+1

    pygame.display.update()
    clk.tick(10)
