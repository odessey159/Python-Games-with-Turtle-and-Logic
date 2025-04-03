import turtle,random
t=turtle.Turtle()
tstamp=turtle.Turtle()
tmargin=turtle.Turtle()
tfood=turtle.Turtle()
tsnake=turtle.Turtle()
tslogan=turtle.Turtle()
tstatus=turtle.Turtle()
tcontact=turtle.Turtle()
tttime=turtle.Turtle()
tmotion=turtle.Turtle()
turtle.tracer(False)
tstamp.hideturtle()
tstatus.hideturtle()
tttime.hideturtle()
tcontact.hideturtle()
tmotion.hideturtle()
tslogan.hideturtle()
tmargin.hideturtle()
tfood.hideturtle()
tsnake.hideturtle()
snakesize=20
hx=0
contactd=0
clickjudge=0
food=[]
stampid=[0]*10000
area = [[0] * 100 for i in range(100)]
stamparea = [[0] * 100 for i in range(100)]
tlen=1
ttime=0
hy=-30
direction=-1
ttime=0
id=10
t.up()
t.shape("square")
tstamp.shape("square")
food=[]
foodx=[0]*1000
foody=[0]*1000
monsterx=[0]*1000
monstery=[0]*1000
foodjudge=[0]*1000
monster=[]
turtle.setup(560,620)  # change the size of screen
t.fillcolor('red')  # turn the color of tile to yellow

def tmove():
    global hx,hy,stampid,tlen,direction,ttime,id,contactd
    motion=''
    tstamp.up()
    tstamp.goto(hx,hy)
    if direction==0:  # determine the direction of the movement
        hx=hx+snakesize
        motion='Right'
    if direction==90:
        hy=hy+snakesize
        motion='Up'
    if direction==180:
        hx=hx-snakesize
        motion='Left'
    if direction==270: 
        hy=hy-snakesize
        motion='Down'
    if direction==-1: 
        motion='Pause'
        ttime=0
    tmotion.clear()
    tmotion.write(motion, align="center",font=('Arial',12))  # demonstrate the direction
    tcontact.clear()
    tcontact.write(contactd, align="center",font=('Arial',12))  # demonstrate the amount of contact
    t.up()
    turtle.tracer(True)
    tstamp.color('black')
    id+=1
    stampid[id]=int(tstamp.stamp())  # draw the body of the snake
    stamparea[hx//snakesize][hy//snakesize+1]=id  # record the sequence of stamp
    tstamp.clearstamp(stampid[id-tlen+1])
    t.goto(hx,hy)  # implement the movement of the head
    turtle.tracer(False)
    if area[hx//snakesize][hy//snakesize]>0:  # judge if the head run into the food
        tlen+=area[hx//snakesize][hy//snakesize]
        food[area[hx//snakesize][hy//snakesize]].clear()
        foodjudge[area[hx//snakesize][hy//snakesize]]=-1
        area[hx//snakesize][hy//snakesize]=0
    if area[hx//snakesize][hy//snakesize+1]==-1 or hx>250 or hx<-250 or hy>210 or hy<-270:  # judge if the head run into the monster or the border
        direction=0
        tslogan.color('red')
        tslogan.write('Game Over !!', align="center",font=('Arial',50))
        return
    if tlen==16:  # judge if all the food has been eaten
        direction=0
        tslogan.color('red')
        tslogan.write('Winner !!', align="center",font=('Arial',50))
        return
    mx=0
    my=0
    if ttime%6==0 and ttime!=0:  # implement the movement of the monster
        for i in range(4) : 
            mx=0
            my=0
            area[monsterx[i]][monstery[i]]=0
            while  True:
                if monsterx[i]*snakesize-10>hx :
                    mx=random.randint(max(-2,-12-monsterx[i]),0)
                if monsterx[i]*snakesize-10<hx :
                    mx=random.randint(0,min(2,12-monsterx[i]))
                if monstery[i]*snakesize-10>hy :
                    my=random.randint(max(-2,-13-monstery[i]),0)
                if monstery[i]*snakesize-10<hy :
                    my=random.randint(0,min(2,11-monstery[i]))
                if area[monsterx[i]+mx][int(monstery[i]+my)]!=-1 and not(mx+monsterx[i]*snakesize-10==hx and my+monstery[i]*snakesize-10==hy): break
            monster[i].goto((mx+monsterx[i])*snakesize,(my+ monstery[i]-0.5)*snakesize)    
            monsterx[i]=mx+monsterx[i]
            monstery[i]=my+monstery[i]
            area[monsterx[i]][monstery[i]]=-1
            if stamparea[monsterx[i]][monstery[i]]>id-tlen+1: contactd+=1
    if ttime%10==0 and ttime!=0:
        for i in range(1,6) :  # implement the movement of the food
            if foodjudge[i]!=-1:
                area[foodx[i]][int(foody[i])]=0
                mx=random.randint(max(-2,-12-foodx[i]),min(2,12-foodx[i]))
                my=random.randint(int(max(-2,-14-foody[i])),int(min(2,11-foody[i])))
                while area[foodx[i]+mx][int(foody[i]+my)]==-1:
                    mx=random.randint(max(-2,-12-foodx[i]),min(2,12-foodx[i]))
                    my=random.randint(int(max(-2,-14-foody[i])),int(min(2,10-foody[i])))
                drawnumber(i,foodx[i]+mx,foody[i]+my)
    if ttime%4==0:  # implement the movement of the head
        tttime.clear()
        tttime.write(ttime//4, align="center",font=('Arial',12))
    turtle.ontimer(tmove,250)
    ttime+=1

def drawnumber(i,x,y):  # draw the number of food
    food[i].clear()
    area[x][int(y)]=i
    foodx[i]=x
    foody[i]=y
    food[i].up()
    food[i].goto(x*snakesize,y*

snakesize)
    food[i].write(i, align="center",font=('Arial',10))    

def drawarea():  # the border 250 to 250, -280 to 220
    tmargin.up()
    tmargin.goto(-250,220)
    tmargin.down()
    tmargin.seth(0)
    for i in range(4):
        tmargin.forward(500)
        tmargin.right(90)
    tmargin.goto(-250,280)
    tmargin.goto(250,280)
    tmargin.goto(250,220)
    tmargin.up()

def clickhandler(x,y):  # judge if the mouse click,then began the game
    global clickjudge
    if clickjudge==0: 
        tslogan.clear()
        turtle.ontimer(tmove,300)
    clickjudge=1

def setdirection(d):
    global direction
    direction = d

def main():
    drawarea()
    area[0][0]=-1
    tstatus.up()
    tmotion.up()
    tttime.up()
    tcontact.up()
    tttime.goto(10,225)
    tcontact.goto(-100,225)
    tmotion.goto(160,225)
    tstatus.goto(0,225)
    tstatus.write('Contact:          time:          Motion:          ', align="center",font=('Arial',12))
    food.append(turtle.Turtle())
    food[0].hideturtle()
    for i in range(1,6): #initialize the cordinates of the food
        food.append(turtle.Turtle())
        food[i].up()
        food[i].hideturtle()
        drawnumber(i,random.randint(-12,12),random.randint(-14,10))
    for i in range(4): #initialize the cordinates of the monster
        monster.append(turtle.Turtle())
        monster[i].up()
        monster[i].shape('square')
        monster[i].color('purple')
        mx=random.randint(-12,12)
        my=random.randint(-13,11)
        while area[mx][my]!=0:
            mx=random.randint(-12,12)
            my=random.randint(-13,11)
        area[mx][my]=-1
        monsterx[i]=mx
        monstery[i]=my
        monster[i].goto(mx*snakesize,(my-0.5)*snakesize)
    turtle.Screen().onkey(lambda: setdirection(0),'d')
    turtle.Screen().onkey(lambda: setdirection(90), 'w')
    turtle.Screen().onkey(lambda: setdirection(180), 'a')
    turtle.Screen().onkey(lambda: setdirection(270), 's')
    turtle.Screen().listen()
    t.goto(hx,hy)
    area[0][0]=0
    tslogan.up()
    tslogan.goto(0,30)
    tslogan.write('Snake by Shen Yihao', align="center",font=('Arial',12))
    tslogan.goto(0,0)
    tslogan.write('Click anywhere to start! Have fun!', align="center",font=('Arial',12))
    turtle.Screen().update()
    turtle.Screen().onclick(clickhandler)  # start the game. Bind the click_handler function to a single mouse click event
    turtle.done()

main() 