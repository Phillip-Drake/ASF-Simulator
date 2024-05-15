from tkinter import *
from tkinter import ttk

num_tiles = 66
root = Tk()
frm = Canvas(root)
frm.rowconfigure((0,1),weight=2,minsize=20)
v = Scrollbar(frm)
  
        # attach Scrollbar to root window on 
        # the side

frm.grid()
#btn = ttk.Button(frm, text="Click to Rotate", command = root.destroy).grid(column=1,row=1)
#north = ttk.Label(frm, text="1").grid(column = 1, row = 0)



#win = GraphWin(width = 1000, height = 1000)
#win.setCoords(0,0,1000,1000)
#
#When pivot is called, you then call the global pivot function, with the initial position, and the 
#
#

class Tile:


    def find_pivot(self):
        if(str(self.north)[-1] == '*' and str(self.east)[-1] == '*'):
            return 1
        elif(str(self.east)[-1] == '*' and str(self.south)[-1] == '*'):
            return 2
        elif(str(self.south)[-1] == '*' and str(self.west)[-1] == '*'):
            return 3
        else:
            return 4

    def __init__(self, num):
        self.pivot = num % 2 == 0
        self.num = num * 4+1
            
        self.north = self.num
        self.east = self.num+1
        self.south = self.num+2
        self.west = self.num+3

        

        self.xCoord = num*3+2+num+1000
        self.yCoord = 1002
        
        self.northx = num*3+2+num+1000
        self.northy = 1001

        self.eastx = num*3+3+num+1000
        self.easty = 1002
 
        self.southx = num*3+2+num+1000
        self.southy = 1003
        self.westx = num*3+1+num+1000
        self.westy = 1002
        self.northLabel = ttk.Label(frm, text=self.north)
        self.northLabel.grid(column=self.northx, row=self.northy)
        self.eastLabel = ttk.Label(frm, text=self.east)
        self.eastLabel.grid(column=self.eastx, row=self.easty)
        self.southLabel = ttk.Label(frm, text=self.south)
        self.southLabel.grid(column=self.southx, row=self.southy)
        self.westLabel = ttk.Label(frm, text = self.west)
        self.westLabel.grid(column=self.westx, row = self.westy)
        self.butn = ttk.Button(frm, text = "Click to Rotate")
        self.butn.configure(command=lambda: rotateOn((self.num-1)/4))
        self.butn.grid(column=self.xCoord,row=self.yCoord)
        if(self.pivot):
            self.pivotLabel = ttk.Label(frm, text = 'X')
            print(self.southx)
            self.pivoty = self.southy + 1
            self.pivotx = self.eastx + 1
            self.pivotLabel.grid(row=self.pivoty, column=self.pivotx)
            self.next_dir = 'clockwise'
        else:
            self.pivotLabel = ttk.Label(frm, text = 'X')
            self.pivoty = self.northy-1
            self.pivotx = self.eastx + 1
            self.pivotLabel.grid(row=self.pivoty, column=self.pivotx)
            self.next_dir = 'counter_clockwise'
        
    def translate(self, x_delta, y_delta):
        self.northx = self.northx + x_delta
        self.northy = self.northy + y_delta
        self.northLabel.grid(column = self.northx, row = self.northy)
        self.eastx = self.eastx + x_delta
        self.easty = self.easty + y_delta
        self.eastLabel.grid(column = self.eastx, row = self.easty)
        self.southx = self.southx + x_delta
        self.southy = self.southy + y_delta
        self.southLabel.grid(column = self.southx, row = self.southy)
        self.westx = self.westx + x_delta
        self.westy = self.westy + y_delta
        self.westLabel.grid(column = self.westx, row = self.westy)
        self.xCoord = self.xCoord + x_delta
        self.yCoord = self.yCoord + y_delta
        self.butn.grid(column = self.xCoord, row = self.yCoord)
    
    def move_to(self, x, y):
        self.northx = -self.northy
        self.northy = self.northx 
        self.northLabel.grid(column = self.northx, row = self.northy)
        self.eastx = x+1
        self.easty = y+1
        self.eastLabel.grid(column = self.eastx, row = self.easty)
        self.southx = x
        self.southy = y+3
        self.southLabel.grid(column = self.southx, row = self.southy)
        self.westx = x-1
        self.westy = y+1
        self.westLabel.grid(column = self.westx, row = self.westy)
        self.xCoord = x
        self.yCoord = y+1
        self.butn.grid(column = self.xCoord, row = self.yCoord)

    def rotate(self, direction):

        if(direction == 'clockwise'):
            temp = self.north
            self.north = self.west
            self.west = self.south
            self.south = self.east
            self.east = temp
        else:
            temp = self.north
            self.north = self.east
            self.east = self.south
            self.south = self.west
            self.west = temp
        self.northLabel.configure(text = self.north)
        self.eastLabel.configure(text=self.east)
        self.southLabel.configure(text=self.south)
        self.westLabel.configure(text=self.west)

    def rotate_coords(self, direction, pivot_x, pivot_y):
        if(direction == 'clockwise'):
            xCoordDiff = self.xCoord - pivot_x
            yCoordDiff = self.yCoord - pivot_y
            
            print(f'initX: {self.xCoord}, initY: {self.yCoord}')
            print(f'xDiff: {xCoordDiff}, yDiff: {yCoordDiff}')

            temp = xCoordDiff
            xCoordDiff = yCoordDiff * -1
            yCoordDiff = temp
            
            print(f'resultX: {pivot_x+xCoordDiff}, resultY: {pivot_y+yCoordDiff}')
            
            pivotxDiff = self.pivotx - pivot_x
            pivotyDiff = self.pivoty - pivot_y

            temp = pivotxDiff
            pivotxDiff = pivotyDiff * -1
            pivotyDiff = temp
            self.pivotx = pivot_x + pivotxDiff
            self.pivoty = pivot_y + pivotyDiff
            self.pivotLabel.grid(column = self.pivotx, row = self.pivoty)

            self.xCoord = pivot_x + xCoordDiff
            self.yCoord = pivot_y + yCoordDiff
            self.northx = self.xCoord
            self.northy = self.yCoord - 1
            self.northLabel.grid(column = self.northx, row = self.northy)
            self.eastx = self.xCoord + 1
            self.easty = self.yCoord
            self.eastLabel.grid(column = self.eastx, row = self.easty)
            self.southx = self.xCoord
            self.southy = self.yCoord + 1 
            self.southLabel.grid(column = self.southx, row = self.southy)
            self.westx = self.xCoord - 1
            self.westy = self.yCoord
            self.westLabel.grid(column = self.westx, row = self.westy)
            self.butn.grid(column = self.xCoord, row = self.yCoord)
        else:
            xCoordDiff = self.xCoord - pivot_x
            yCoordDiff = self.yCoord - pivot_y
            
            print(f'initX: {self.xCoord}, initY: {self.yCoord}')
            print(f'xDiff: {xCoordDiff}, yDiff: {yCoordDiff}')

            temp = xCoordDiff
            xCoordDiff = yCoordDiff
            yCoordDiff = temp * -1
            
            print(f'resultX: {pivot_x+xCoordDiff}, resultY: {pivot_y+yCoordDiff}')
            
            pivotxDiff = self.pivotx - pivot_x
            pivotyDiff = self.pivoty - pivot_y

            temp = pivotxDiff
            pivotxDiff = pivotyDiff
            pivotyDiff = temp * -1
            self.pivotx = pivot_x + pivotxDiff
            self.pivoty = pivot_y + pivotyDiff
            self.pivotLabel.grid(column = self.pivotx, row = self.pivoty)

            self.xCoord = pivot_x + xCoordDiff
            self.yCoord = pivot_y + yCoordDiff
            self.northx = self.xCoord
            self.northy = self.yCoord - 1
            self.northLabel.grid(column = self.northx, row = self.northy)
            self.eastx = self.xCoord + 1
            self.easty = self.yCoord
            self.eastLabel.grid(column = self.eastx, row = self.easty)
            self.southx = self.xCoord
            self.southy = self.yCoord + 1 
            self.southLabel.grid(column = self.southx, row = self.southy)
            self.westx = self.xCoord - 1
            self.westy = self.yCoord
            self.westLabel.grid(column = self.westx, row = self.westy)
            self.butn.grid(column = self.xCoord, row = self.yCoord)
            frm.scale(ALL, 8200,1200,0.1,0.1)

            

def rotateOn(tile_num):
    tile_num = int(tile_num)
    for i in range(tile_num+1, num_tiles):
        tiles[i].rotate(tiles[tile_num].next_dir)
        tiles[i].rotate_coords(tiles[tile_num].next_dir, tiles[tile_num].pivotx, tiles[tile_num].pivoty)
            
            
            #if(tiles[tile_num].eastx == tiles[tile_num+1].westx-1):
            #    tiles[tile_num+1].translate(0,3)
            #    for i in range(tile_num + 2, num_tiles):
            #        tiles[i].move_to(tiles[i-1].southx, tiles[i-1].southy+1)



tiles = []
for i in range(0, num_tiles):
    tiles.append(Tile(i))



root.mainloop()


    

#def draw(object):
#    object.tileObject.draw(win)
#    pass
#
#test1 = Tile(1)
#test2 = Tile(2)
#test3 = Tile(3)
#
#draw(test1)
#draw(test2)
#draw(test3)
#
#    
#win.getMouse()
#
#
#
#
#