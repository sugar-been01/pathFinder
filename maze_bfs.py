import turtle
 
def path(x,y,wid):
    #fills block
    turtle.goto(x,y)
    turtle.shape("square")
    turtle.stamp()

def startMaze(maze):
    #draws maze given a 2D array
    # list representing the maze
    turtle.up()
    turtle.hideturtle()
    x=1
    y=20
    blck={}
    X,Y=0,0

    for r in maze:
        x=1
        X=0
        for c in r:
            
            if c=="00":
                #draws a black block if the block is a wall
                turtle.goto(x,y)
                turtle.color("white")
                turtle.shape("square")
                turtle.stamp()
                
                blck[c]=(x,y)
            elif c=="st":
                #draws a green block
                blck[c]=(x,y)
                turtle.goto(x,y)
                turtle.color("green")
                turtle.shape("square")
                turtle.stamp()
                
                stC=Y,X

            elif c=="ed":
                #draws a red block
                blck[c]=(x,y)
                turtle.goto(x,y)
                turtle.color("red")
                turtle.shape("square")
                turtle.stamp()
                

            else:
                #draws unfilled block
                turtle.goto(x,y)
                turtle.shape("square")
                blck[c]=(x,y)
                
            x+=5
            X+=1
        y+=5
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
            ["00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",'00',"00","00","00"],
            ["00","st","11","00","00","12","13","14","00","08","23","00","'+","00","jj","j-","q+","w]","a1","b1","d1","1c","1f","1h","1i",'[sa',"'sa",";sa","00"],
            ["00","00","17","00","18","19","20","21","00","22","24","00","?/","00","ed","-p","ps","sd","a2","b2","00","00","00","h2","i2",'0sad',"023","123","00"],
            ["00","26","27","@b","00","28","00","00","00","32","33","00",":;","00","sax","os","1+","@]","a3","b3","00","c4","00","h3","i3",'0asdc0',"0210","00sd","00"],
            ["00","00","00","35","a72","37","38","39","40","41","42",">.","<>","00","kl","om","00","ol","a4","b4","00","c3","00","h4","i4",'sadv,',"savd0","0qwe","00"],
            ["00","00","44","00","45","46","47","48","00","00","*[","0~","0|","\|","AX","00","mh","sx","a","b5","d5","c5","f5","h5","i5",'xzcb',"xcz0","d./","00"],
            ["00","00","50","51","52","53","54","55","00","00","00","!+","><","00","00","dn","dm","sa","6a","b6","d6","c6","f6","00","00",'sa',"/sa0","0axd","00"],
            ["00","56","57","58","59","60","61","00","00","00","00","u+","?.","=0","00","--","-+","-]","00","00","00","c7","7f","7h","7i",'23f',"|:d","s}a","00"],
            ["00","63","64","65","66","67","68","00","69","bb","00","00","00","{0","#l","#-","#+","#]","a8","00","00","c8","f8","h8","8i",'sac0',"0as0","034:","00"],
            ["00","00","70","71","72","73","00","74","{-","00","00","00","00","_+","00","py","0o","9]","9a","00","00","00","00","pl","i9",'00',"a12","sda0","00"],
            ["00","00","00","75","76","77","78","79","00","00","00","++","||","}{","00","so","-$","#$","10a",",b",",d",",c","00","h0","00",'00',"00","s]ds","00"],
            ["00","nn","#0","1#","00","00","mm","#9","00","00","00","[]","00","::","00","00","00","!l","00","00","00","c0","<0","h0","i0",'0[]',"00","0fvx","00"],
            ["00","0.0","$0",")(","(6","00","y6","7*","&1","00","00","__","//","''","0!","!!","-`","-~","asa-","b-as","d0-","00","00","h's;","ika",'0-_',"+12","saj","00"],
            ["00","00","1%","?(","+9","00","-8","7}","&}","=+","9k","(.","00","00","ii","kg","jk","mr","a's","b'a}","00","00","00","h|","]i|",'00',"s[0","+sa]","00"],
            ["00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00",'00',"00","00","00"]]
            
    screen = turtle.Screen()
    turtle.bgcolor("black")
    width, height = screen.window_width(), screen.window_height()
    screen.setworldcoordinates(0, 150, 150, 0)

    blcks,stC =startMaze(maze2)
    wid=int(150/len(maze2))
    paths=solution(maze2,blcks,stC)
    shortestPath(blcks,paths,wid)
    screen.exitonclick()

if __name__=="__main__":
    main()
