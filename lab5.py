import turtle

def svTree(length, depthSplit):
    '''creates a tree with certain length and depth/amounts of splits within tree'''
    turtle.color('Dark Sea Green')
    if depthSplit == 0:
        return
    turtle.forward(length)
    turtle.left(20)
    svTree(length/2, depthSplit-1)
    turtle.right(40)
    svTree(length/2, depthSplit-1)
    turtle.left(20)
    turtle.backward(length)


    
