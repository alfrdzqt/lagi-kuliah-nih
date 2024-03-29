#%%
def listsum_A(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum_A([1, 3, 5, 7, 9]))



#%%
def listsum_B(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum_B(numList[1:])

print(listsum_B([1, 3, 5, 7, 9]))

#%%

def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]
    
print(toStr(1453,16))

#%%
from pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
            n = n // base
        else:
            rStack.push(convertString[n % base])
            n = n // base
    res = ''
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res

print(toStr(1453,16))

#%%

import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

drawSpiral(myTurtle, 100)
myWin.exitonclick()

#%%

import turtle

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

    def main():
        t = turtle.Turtle()
        myWin = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color("green")
        tree(75,t)
        myWin.exitonclick()

    main()

#%%

import turtle

def drawTriangle(points,colour,myTurtle):
    myTurtle.fillcolor(colour)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[1],
                    getMid(points[0],points[1]),
                    getMid(points[1],points[2])],
                   degree-1,myTurtle)
        sierpinski([points[2],
                    getMid(points[2],points[1]),
                    getMid(points[0],points[2])],
                   degree-1,myTurtle)
        
def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-100,-50],[0,100],[100,-50]]
    sierpinski(myPoints,3,myTurtle)
    myWin.exitonclick()

main()

#%%

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from", fp, "to", tp)

moveTower(3,"A","B","C")