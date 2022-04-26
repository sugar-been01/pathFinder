import turtle

def blocks(x,y,width):
    #draws block 
    turtle.speed(0)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.up()

def path(x,y,wid):
    #fills block
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.forward(wid)
    turtle.right(90)
    turtle.forward(wid)
    turtle.right(90)
    turtle.forward(wid)
    turtle.right(90)
    turtle.forward(wid)
    turtle.right(90)
    turtle.end_fill()

def startMaze(maze):
    #draws maze given a 2D array
    # list representing the maze
    turtle.up()
    turtle.hideturtle()
    x=1
    y=20
    wid=int(150/len(maze))
    blck={}
    X,Y=0,0

    for r in maze:
        x=1
        X=0
        for c in r:
            
            if c=="00":
                #draws a black block if the block is a wall
                turtle.fillcolor("black")
                turtle.begin_fill()
                blocks(x,y,wid)
                turtle.end_fill()

            elif c=="st":
                #draws a green block
                turtle.fillcolor("green")
                turtle.begin_fill()
                blocks(x,y,wid)
                turtle.end_fill()
                stC=Y,X

            elif c=="ed":
                #draws a red block
                blck[c]=(x,y)
                turtle.fillcolor("red")
                turtle.begin_fill()
                blocks(x,y,wid)
                turtle.end_fill() 

            else:
                #draws unfilled block
                blck[c]=(x,y)
                blocks(x,y,wid)
            x+=wid
            X+=1
        y+=wid
        Y+=1
    return blck,stC

def solution(maze,blck,stC):
    #finds all every path from start using bfs
    frontier=[]
    wid=int(150/len(maze))
    frontier.append(stC)
    current=stC
    vis=[]
    row=len(maze)
    col=len(maze[1])
    vis.append(current)
    solution={}
    turtle.fillcolor("gray")

    while len(frontier)>0:
        current=frontier[0]
        ind1=current[0]
        ind2=current[1]
        cp=maze[ind1][ind2]
        
        if current[0]-1>=0 and (current[0]-1,current[1]) not in vis:#check up
            pos=maze[ind1-1][ind2]

            if (pos!="00"):
                X,Y=blck[pos]
                path(X,Y,wid)
                frontier.append((current[0]-1,current[1]))
                vis.append((current[0]-1,current[1]))
                solution[pos]=cp

        if current[1]+1<col and (current[0],current[1]+1) not in vis:#check right
            pos=maze[ind1][ind2+1]

            if pos!="00":
                X,Y=blck[pos]
                path(X,Y,wid)
                frontier.append((current[0],current[1]+1))
                vis.append((current[0],current[1]+1))
                solution[pos]=cp

        if current[0]+1<row and (current[0]+1,current[1]) not in vis:#check down
            pos=maze[ind1+1][ind2]

            if pos!="00":
                X,Y=blck[pos]
                path(X,Y,wid)
                frontier.append((current[0]+1,current[1]))
                vis.append((current[0]+1,current[1]))
                solution[pos]=cp

        if current[1]-1>=0 and (current[0],current[1]-1) not in vis:#check left
            pos=maze[ind1][ind2-1]

            if pos!="00":
                X,Y=blck[pos]
                path(X,Y,wid)
                frontier.append((current[0],current[1]-1))
                vis.append((current[0],current[1]-1))
                solution[pos]=cp

        frontier.remove(current)
    return solution

def shortestPath(blck,solution,width):
    #uses the path method to fill out 
    #the shortest path from starting point to end
    turtle.fillcolor("red")
    X,Y=blck["ed"]
    path(X,Y,width)
    turtle.fillcolor("orange")
    found=(solution["ed"])
    X,Y=blck[found]
    path(X,Y,width)

    while found!="st":
        found=solution[found]

        if found!="st":
            X,Y=blck[found]
            path(X,Y,width)

def main():
    maze=[  
        ["00","st","02","00","04","00","45","00"],
        ["00","05","00","06","00","07","99","33"],
        ["00","08","09","95","10","11","00","55"],
        ["01","12","13","00","14","00","00","00"],
        ["00","15","27","00","16","17","68","89"],
        ["18","00","25","28","20","88","00","81"],
        ["00","90","67","00","44","77","00","ed"]]
    maze2=[
            ["s.","02","03","04","00","05","06","07","00","00","00","*-","@1","hj","eh","s-","l+","u]"],
            ["09","10","11","00","00","12","13","14","00","08","23","00","'+","00","jj","j-","q+","w]"],
            ["00","00","17","00","18","19","20","21","00","22","24","00","?/","00","ed","-p","ps","sd"],
            ["25","26","27","@b","00","28","00","00","00","32","33","00",":;","00","00","os","1+","@]"],
            ["34","00","00","35","36","37","38","39","40","41","42",">.","<>","00","kl","om","sm","ol"],
            ["43","00","44","00","45","46","47","48","00","00","*[","0~","0|","\|","00","00","mh","mf"],
            ["00","00","50","51","52","53","54","55","00","00","00","!+","><","00","00","dn","dm","sa"],
            ["00","56","57","58","59","60","61","00","00","00","00","u+","?.","=0","00","--","-+","-]"],
            ["62","63","64","65","66","67","68","00","69","bb","00","00","00","{0","#l","#-","#+","#]"],
            ["00","00","70","71","72","73","00","74","{-","00","00","00","00","_+","00","py","0o","9]"],
            ["00","00","00","75","76","77","78","79","00","00","00","++","||","}{","00","so","-$","#$"],
            ["00","00","#0","1#","00","00","mm","#9","00","00","00","[]","00","::","00","00","00","!l"],
            ["s;","00","$0",")(","(6","00","y6","7*","&1","00","00","__","//","''","0!","!!","-`","-~"],
            ["bs","00","1%","?(","+9","00","-8","7}","&}","=+","9k","(.","00","00","ii","kg","jk","mr"],
            ["de","#q","k%","j(","+l","st","-k","o}","9}","00","00","^b","00","00","1p","4f","5f","6s"]]
            
    screen = turtle.Screen()
    width, height = screen.window_width(), screen.window_height()
    screen.setworldcoordinates(0, 175, 185, 0)

    blcks,stC =startMaze(maze2)
    wid=int(150/len(maze2))
    paths=solution(maze2,blcks,stC)
    shortestPath(blcks,paths,wid)
    screen.exitonclick()

if __name__=="__main__":
    main()