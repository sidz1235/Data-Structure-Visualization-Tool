from cmd import Cmd
from clrprint import clrprint, clrinput
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
import os
import re
import turtle as t
import random
import tkinter
import time
import sys
import ast

init_dir = os.getcwd()
methodList={"array":["set","get","insert","append" ,"delete","pop","search","reverse","count","sort"],
            "stack":["push","pop","peek","size","is_empty","is_full"],
            "queue":["enqueue","dequeue","peek","size","is_empty","is_full"],
            "binarytree":["insert","search","delete","count","level_order","pre_order","post_order","in_order"],
            "linkedlist":["insert","delete","count","search","remove","reverse"],
            "binarysearchtree":["insert","search","delete","count","level_order","pre_order","post_order","in_order"]}

maxCapacity={"array":12,"stack":6,"queue":12,"binarytree":3,"binarysearchtree":3,"linkedlist":7} #File Name
initialise = {"array":"append","stack":"push","queue":"enqueue","linkedlist":"insert","binarytree":"insert","binarysearchtree":"insert"}


def write(msg):
    global ins_turtle, cur_message
    msg_stack.append(msg)
    ins_turtle.clear()
    ins_turtle.write(str(msg), align = "center", font = ("Arial", 20, "bold"))
def undo():
    global ins_turtle, cur_message
    ins_turtle.clear()
    msg_stack.pop()
    msg = msg_stack.pop()
    write(msg)
    ins_turtle.write(str(msg), align = "center", font = ("Arial", 20, "bold"))

class DS_Turtle:
    def __init__(self, x=0, y=0):
        self.turtle = t.Turtle()
        self.pen = t.Turtle()
        self.turtle.up()
        self.pen.up()
        self.pen.ht()
        self.turtle.shape("ds.gif")
        self.move(x, y)
    def move(self, x, y):
        self.turtle.setposition(x, y)
        self.pen.setposition(x, y-11)
    def write(self, msg):
        self.pen.write(msg, align = "center", font = ("Arial", 15, "bold"))
    def clr(self):
        self.pen.clear()
        self.turtle.ht()
    def hide(self):
        self.pen.ht()
        self.turtle.ht()
        
ds_turtles = []

def init_ds(obj):
    global ds_turtles
    ds_turtles = [DS_Turtle() for i in range(len(obj))]
    for i in range(len(obj)):
        ds_turtles[i].move(ds_turtle.xcor(), ds_turtle.ycor()-75*(i+1))
        ds_turtles[i].write(obj[i][:10])
def del_ds():
    global ds_turtles
    for i in range(len(ds_turtles)):
        ds_turtles[0].clr()
        del ds_turtles[0]

def init_screen():
    global main_turtle, ins_turtle, next_turtle, ds_turtle, main_turtle_left, pointer_turtle, msg_stack
    win.delay(0)
    main_turtle.up()
    ins_turtle.up()
    next_turtle.up()
    ds_turtle.up()
    main_turtle_left.up()
    pointer_turtle.up()
    main_turtle_left.ht()
    main_turtle.ht()
    ins_turtle.ht()
    ds_turtle.ht()
    pointer_turtle.ht()

    main_turtle.setposition(-156.5, 61.5)
    ins_turtle.setposition(-156.5, -280)
    ds_turtle.setposition(454, 290)
    main_turtle_left.setposition(-400, 61.5)
    next_turtle.setposition(454, -265)
    next_turtle.shape("next_ds.gif")
    write("Welcome!")
    msg_stack = ["Welcome!"]

#init_ds(objects)

#Init DS Turtles
#def init_ds(size):
"""ds_turtles = [DS_Turtle() for i in range(6)]
for i in range(6):
    ds_turtles[i].move(ds_turtle.xcor(), ds_turtle.ycor()-75*(i+1))
    ds_turtles[i].write("Hello")"""

class Array_Turtle:
    def __init__(self, x=0, y=0, data = "NULL"):
        self.data = data
        self.turtle = t.Turtle()
        self.turtle.turtlesize(40)
        self.pen = t.Turtle()
        self.turtle.up()
        self.pen.up()
        self.pen.ht()
        self.turtle.shape("arr"+str(random.randint(1, 9))+".gif")
        self.move(x, y)
        self.turtle.onclick(fun = self.get_data)
        self.pen.onclick(fun = self.get_data)
    def move(self, x, y):
        self.turtle.setposition(x, y)
        self.pen.setposition(x, y-11)
    def write(self, msg):
        self.pen.write(msg, align = "center", font = ("Arial", 15, "bold"))
    def clr(self):
        self.pen.clear()
        self.turtle.ht()
    def hide(self):
        self.pen.ht()
        self.turtle.ht()
    def set_data(self, data):
        self.data = data
    def change_color(self):
        self.turtle.shape("arr"+str(random.randint(1, 9))+".gif")
    def get_data(self, x, y):
        self.turtle.onclick(fun = None)
        self.pen.onclick(fun = None)
        write(self.data)
        time.sleep(3)
        undo()
        self.turtle.onclick(fun = self.get_data)
        self.pen.onclick(fun = self.get_data)

class Array:
    def __init__(self, size = 12):
        global main_turtle
        self.array_turtles = [Array_Turtle() for i in range(size)]
        self.array_shapes = ["arr-1.gif" for i in range(size)]
        self.array = ["NULL" for i in range(size)]
        self.size = size
        self.append_index = 0
        self.update()
        write("Created Array Of Size "+str(size))
        time.sleep(3)
    def __del__(self):
        global pointer_turtle
        pointer_turtle.clear()
        while(len(self.array_turtles)>0):
            self.array_turtles[0].clr()
            del self.array_turtles[0]
    def pointer_update(self, var):
        global main_turtle, pointer_turtle
        pointer_turtle.clear()
        init_y = main_turtle.ycor()-80
        #print(list(sorted(var.keys())))
        for i in list(sorted(var.keys())):
            pointer_turtle.setposition(main_turtle.xcor(), init_y)
            pointer_turtle.write(str(i)+" : "+str(var[i]), align = "center", font = ("Arial", 20, "bold"))
            init_y -= 30
    def update(self):
        if(len(self.array)>self.size):
            write("Array Limit Exceeded")
            time.sleep(3)
            undo()
            return -1
        else:
            (count_right, count_left) = (99, -33)
            n = self.size//2
            for i in range(n, -1, -1):
                self.array_turtles[i].pen.clear()
                self.array_turtles[i].move(main_turtle.xcor()-count_left, main_turtle.ycor())
                self.array_turtles[i].write(str(self.array[i])[:4])
                self.array_turtles[i].set_data(self.array[i])
                self.array_turtles[i].turtle.shape(self.array_shapes[i])
                count_left += 66
            right_index = n+1
            while(right_index<self.size):
                self.array_turtles[right_index].pen.clear()
                self.array_turtles[right_index].move(main_turtle.xcor()+count_right, main_turtle.ycor())
                self.array_turtles[right_index].write(str(self.array[right_index])[:4])
                self.array_turtles[right_index].set_data(self.array[right_index])
                self.array_turtles[right_index].turtle.shape(self.array_shapes[right_index])
                right_index += 1
                count_right += 66
    def set(self, index, x):
        if(index>self.append_index):
            write("Array Length Exceeded")
            time.sleep(3)
            undo()
            return -1
        self.array[index] = x
        self.array_shapes[index] = "arr"+str(random.randint(1, 9))+".gif"
        self.update()
        write("Set Index "+str(index)+" To "+str(x))
        time.sleep(3)
    def get(self, index):
        if(index>=self.append_index):
            write("Array Length Exceeded")
            time.sleep(3)
            undo()
            return -1
        write("Index "+str(index)+" Contains "+str(self.array[index]))
        time.sleep(3)
    def insert(self, index = -1, x = "NULL"):
        if(index == -1):
            index = self.append_index
        if(self.append_index>=self.size):
            write("Array Length Exceeded")
            time.sleep(3)
            undo()
            return -1
        self.append_index += 1
        for i in range(self.append_index-1, index, -1):
            self.array_shapes[i] = self.array_shapes[i-1]
            self.array[i] = self.array[i-1]
        self.array[index] = x
        self.array_shapes[index] = "arr"+str(random.randint(1, 9))+".gif"
        self.update()
        write("Inserted "+str(x)+" At Index "+str(index))
        time.sleep(3)
    def append(self, x = "NULL"):
        self.insert(self.append_index, x)
    def delete(self, index = -1):
        if(index == -1):
            index = self.append_index
        if(index>=self.append_index):
            write("Array Length Exceeded")
            time.sleep(3)
            undo()
            return -1
        self.append_index -= 1
        data = self.array[index]
        for i in range(index, self.append_index):
            self.array_shapes[i] = self.array_shapes[i+1]
            self.array[i] = self.array[i+1]
        self.array[self.append_index] = "NULL"
        self.array_shapes[self.append_index] = "arr-1.gif"
        self.update()
        write("Deleted "+str(data)+" At Index "+str(index))
        time.sleep(3)
    def pop(self):
        self.delete(self.append_index-1)
    def search(self, x):
        global pointer_turtle
        var = {"i":0}
        for i in range(self.append_index):
            self.pointer_update(var)
            if(self.array[i] == x):
                self.array_turtles[i].turtle.shape("arrgreen.gif")
                write("Found "+str(x)+" At Index "+str(i))
                time.sleep(3)
                pointer_turtle.clear()
                return i
            else:
                self.array_turtles[i].turtle.shape("arrred.gif")
                write("Did Not Find "+str(x)+" At Index "+str(i))
                time.sleep(2)
            var["i"] += 1
        else:
            write("Did Not Find "+str(x)+" In Array")
            time.sleep(3)
        self.update()
        pointer_turtle.clear()
        return -1
    def reverse(self):
        global pointer_turtle
        self.update()
        var = {"start":0, "end":(self.append_index-1)}
        end = (self.append_index-1)
        for start in range(self.append_index):
            self.pointer_update(var)
            if(start>end):
                self.update()
                write("Array Reversed")
                time.sleep(2)
                pointer_turtle.clear()
                return 1
            (self.array[start], self.array[end]) = (self.array[end], self.array[start])
            (self.array_shapes[start], self.array_shapes[end]) = (self.array_shapes[end], self.array_shapes[start])
            self.array_turtles[start].turtle.shape("arrgold.gif")
            self.array_turtles[end].turtle.shape("arrgold.gif")
            write("Swapping Indices "+str(start)+" And "+str(end))
            time.sleep(5)
            self.update()
            start += 1
            end -= 1
            var["start"] = start
            var["end"] = end
    def count(self):
        global pointer_turtle
        var = {"count":0}
        for i in range(self.append_index):
            self.pointer_update(var)
            self.array_turtles[i].turtle.shape("arrgold.gif")
            var["count"] += 1
            write("Incrementing Count")
            self.pointer_update(var)
            time.sleep(3)
        write("There Are "+str(var["count"])+" Element(s) in Array")
        time.sleep(3)
        self.update()
        pointer_turtle.clear()
        return var["count"]
    def sort(self):
        global pointer_turtle
        self.update()
        var = {"i":0, "j":0}
        for i in range(self.append_index):
            for k in range(i+1):
                self.array_turtles[k].turtle.shape("arrgold.gif")
            self.array_turtles[i].turtle.shape("arrgold.gif")
            write("Selecting Element At Index "+str(i))
            time.sleep(4)
            for j in range(i+1, self.append_index):
                for k in range(i+1):
                    self.array_turtles[k].turtle.shape("arrgold.gif")
                var["i"] = i
                var["j"] = j
                self.pointer_update(var)
                if(self.array[i]>self.array[j]):
                    (self.array[i], self.array[j]) = (self.array[j], self.array[i])
                    (self.array_shapes[i], self.array_shapes[j]) = (self.array_shapes[j], self.array_shapes[i])
                    write("Swapping Elements As Element At "+str(i)+" is Greater Than Element At "+str(j))
                    time.sleep(4)
                    self.array_turtles[i].turtle.shape("arrgold.gif")
                self.update()
        self.update()
        write("Array Sorted")
        pointer_turtle.clear()
        time.sleep(3)
                
#Init Array Turtles
"""array_turtles = [Array_Turtle() for i in range(12)]
count_right = 99
count_left = -33
n = 12//2
for i in range(n, -1, -1):
    array_turtles[i].move(main_turtle.xcor()-count_left, main_turtle.ycor())
    array_turtles[i].write(str(i))
    array_turtles[i].set_data(i)
    count_left += 66
right_index = n+1
while(right_index<12):
    array_turtles[right_index].move(main_turtle.xcor()+count_right, main_turtle.ycor())
    array_turtles[right_index].write(str(right_index))
    array_turtles[right_index].set_data(right_index)
    right_index += 1
    count_right += 66"""

"""arr = Array(7)
arr.append(10)
arr.append(80)
arr.append(30)
arr.append(90)
#arr.append(40)
#arr.append(50)
#arr.insert(0, 70)
#arr.reverse()
#arr.sort()
#arr.count()
win.clearscreen()"""

class Stack_Turtle:
    def __init__(self, x=0, y=0, data = "NULL"):
        self.data = data
        self.turtle = t.Turtle()
        self.turtle.turtlesize(40)
        self.pen = t.Turtle()
        self.turtle.up()
        self.pen.up()
        self.pen.ht()
        self.turtle.shape("stack-1.gif")
        self.move(x, y)
        self.turtle.onclick(fun = self.get_data)
        self.pen.onclick(fun = self.get_data)
    def move(self, x, y):
        self.turtle.setposition(x, y)
        self.pen.setposition(x, y-11)
    def write(self, msg):
        self.pen.write(msg, align = "center", font = ("Arial", 15, "bold"))
    def clr(self):
        self.pen.clear()
        self.turtle.ht()
    def hide(self):
        self.pen.ht()
        self.turtle.ht()
    def set_data(self, data):
        self.data = data
    def get_data(self, x, y):
        self.turtle.onclick(fun = None)
        self.pen.onclick(fun = None)
        write(self.data)
        time.sleep(3)
        undo()
        self.turtle.onclick(fun = self.get_data)
        self.pen.onclick(fun = self.get_data)

class Stack:
    def __init__(self, size = 6):
        global main_turtle
        self.stack_turtles = [Stack_Turtle() for i in range(size)]
        self.stack_container = t.Turtle()
        self.stack_container.shape("stackcontainer.gif")
        self.stack_container.up()
        self.stack_container.setposition(main_turtle.xcor(), main_turtle.ycor()+30)
        self.stack_shapes = ["stack-1.gif" for i in range(size)]
        self.stack = ["NULL" for i in range(size)]
        self.capacity = size
        self.var = {"top":-1}
        self.update()
        write("Created Stack Of Size "+str(size))
        time.sleep(3)
    def __del__(self):
        global pointer_turtle
        pointer_turtle.clear()
        self.stack_container.clear()
        self.stack_container.ht()
        for i in range(len(self.stack_turtles)):
            self.stack_turtles[0].clr()
            del self.stack_turtles[0]
    def update(self):
        global main_turtle
        pos = -150
        for i in range(self.capacity):
            self.stack_turtles[i].pen.clear()
            self.stack_turtles[i].move(main_turtle.xcor(), pos+66*(i+1))
            self.stack_turtles[i].write(str(self.stack[i])[:12])
            self.stack_turtles[i].set_data(self.stack[i])
            self.stack_turtles[i].turtle.shape(self.stack_shapes[i])
        self.pointer_update(self.var)
    def pointer_update(self, var):
        global main_turtle, pointer_turtle
        pointer_turtle.clear()
        init_x = self.stack_turtles[0].turtle.xcor()+250
        init_y = self.stack_turtles[0].turtle.ycor()-17
        pointer_turtle.setposition(init_x, init_y+66*self.var["top"])
        pointer_turtle.write(str("top")+" : "+str(var["top"]), align = "center", font = ("Arial", 20, "bold"))
    def push(self, x):
        if(self.var["top"] == self.capacity-1):
            write("Stack is Full")
            time.sleep(3)
            return -1
        self.var["top"] += 1
        self.stack_shapes[self.var["top"]] = "stack"+str(random.randint(1, 9))+".gif"
        self.stack[self.var["top"]] = x
        self.update()
        self.stack_turtles[self.var["top"]].turtle.shape("stackgold.gif")
        write("Pushed "+str(x)+" Onto Stack")
        time.sleep(3)
        self.update()
    def pop(self):
        if(self.var["top"] == -1):
            write("Stack is Empty")
            time.sleep(3)
            return -1
        data = self.stack[self.var["top"]]
        self.stack_turtles[self.var["top"]].turtle.shape("stackgold.gif")
        write("Popping "+str(data)+" From Stack")
        time.sleep(3)
        self.stack_shapes[self.var["top"]] = "stack-1.gif"
        self.stack[self.var["top"]] = "NULL"
        self.var["top"] -= 1
        self.update()
        return data
    def peek(self):
        if(self.var["top"] == -1):
            write("Stack is Empty")
            time.sleep(3)
            return -1
        write("Data At Top is "+str(self.stack[self.var["top"]]))
        self.stack_turtles[self.var["top"]].turtle.shape("stackgold.gif")
        time.sleep(3)
        self.update()
        return self.stack[self.var["top"]]
    def size(self):
        write("There Are "+str(self.var["top"]+1)+" Element(s) In The Stack")
        time.sleep(3)
        return self.var["top"]+1
    def is_empty(self):
        if(self.var["top"] == -1):
            write("Stack is Empty")
            time.sleep(3)
        else:
            write("Stack is Not Empty")
            time.sleep(3)
    def is_full(self):
        if(self.var["top"] == self.capacity-1):
            write("Stack is Full")
            time.sleep(3)
        else:
            write("Stack is Not Full")
            time.sleep(3)
        

#Init Stack Turtles
"""stack_turtles = [Stack_Turtle() for i in range(6)]
pos = -150
for i in range(6):
    stack_turtles[i].move(main_turtle.xcor(), pos+66*(i+1))
    stack_turtles[i].write(str(i))
    stack_turtles[i].set_data(i)"""

"""s = Stack(3)
s.is_empty()
s.push("Hey")
s.push("Hello")
s.push("Lol")
s.push("Troll")
s.push("Bobbbbb")
s.push("Bobbbbb")
s.push("Bobbbbb")
s.push("Bobbbbb")
s.is_full()"""

class Queue:
    def __init__(self, size = 12):
        global main_turtle
        self.queue_turtles = [Array_Turtle() for i in range(size)]
        self.queue_shapes = ["arr-1.gif" for i in range(size)]
        self.queue = ["NULL" for i in range(size)]
        self.capacity = size
        self.var = {"front":-1, "rear":-1}
        self.update()
        write("Created Queue Of Size "+str(size))
        time.sleep(3)
    def __del__(self):
        global pointer_turtle
        pointer_turtle.clear()
        for i in range(len(self.queue_turtles)):
            self.queue_turtles[0].clr()
            del self.queue_turtles[0]
    def pointer_update(self, var):
        global main_turtle, pointer_turtle
        pointer_turtle.clear()
        init_y = main_turtle.ycor()-80
        for i in list(sorted(var.keys())):
            pointer_turtle.setposition(main_turtle.xcor(), init_y)
            pointer_turtle.write(str(i)+" : "+str(var[i]), align = "center", font = ("Arial", 20, "bold"))
            init_y -= 30
    def update(self):
        self.pointer_update(self.var)
        if(len(self.queue)>self.capacity):
            write("Queue Limit Exceeded")
            time.sleep(3)
            undo()
            return -1
        else:
            (count_right, count_left) = (99, -33)
            n = self.capacity//2
            for i in range(n, -1, -1):
                self.queue_turtles[i].pen.clear()
                self.queue_turtles[i].move(main_turtle.xcor()-count_left, main_turtle.ycor())
                self.queue_turtles[i].write(str(self.queue[i])[:4])
                self.queue_turtles[i].set_data(self.queue[i])
                self.queue_turtles[i].turtle.shape(self.queue_shapes[i])
                count_left += 66
            right_index = n+1
            while(right_index<self.capacity):
                self.queue_turtles[right_index].pen.clear()
                self.queue_turtles[right_index].move(main_turtle.xcor()+count_right, main_turtle.ycor())
                self.queue_turtles[right_index].write(str(self.queue[right_index])[:4])
                self.queue_turtles[right_index].set_data(self.queue[right_index])
                self.queue_turtles[right_index].turtle.shape(self.queue_shapes[right_index])
                right_index += 1
                count_right += 66
    def enqueue(self, x):
        if(self.var["rear"]==self.capacity-1):
            write("Queue Length Exceeded")
            time.sleep(3)
            return -1
        if(self.var["front"] == -1):
            self.var["front"] += 1
        self.var["rear"] += 1
        self.queue[self.var["rear"]] = x
        self.queue_shapes[self.var["rear"]] = "arr"+str(random.randint(1, 9))+".gif"
        self.update()
        write("Enqueued "+str(x)+" To Queue")
        time.sleep(3)
    def dequeue(self):
        if(self.var["front"] == -1):
            write("Queue is Empty")
            time.sleep(3)
            self.update()
            return -1
        data = self.queue[self.var["front"]]
        self.queue_turtles[self.var["front"]].turtle.shape("arrgold.gif")
        write("Dequeueing "+str(data)+" From Queue")
        time.sleep(3)
        self.queue[self.var["front"]] = "NULL"
        self.queue_shapes[self.var["front"]] = "arr-1.gif"
        if(self.var["front"] == self.var["rear"]):
            self.var["front"] = self.var["rear"] = -1
            self.update()
            return data
        self.var["front"] += 1
        self.update()
        return data
    def peek(self):
        if(self.var["front"] == -1):
            write("Queue is Empty")
            time.sleep(3)
            return -1
        write("Data At Front is "+str(self.queue[self.var["front"]]))
        self.queue_turtles[self.var["front"]].turtle.shape("arrgold.gif")
        time.sleep(3)
        self.update()
        return self.queue[self.var["front"]]
    def size(self):
        write("There Are "+str(self.var["rear"]+1)+" Element(s) In The Queue")
        time.sleep(3)
        return self.var["rear"]+1
    def is_empty(self):
        if(self.var["front"] == -1):
            write("Queue is Empty")
            time.sleep(3)
        else:
            write("Queue is Not Empty")
            time.sleep(3)
    def is_full(self):
        if(self.var["rear"] == self.capacity-1):
            write("Queue is Full")
            time.sleep(3)
        else:
            write("Queue is Not Full")
            time.sleep(3)
        
"""q = Queue(6)
q.is_empty()
q.enqueue("Hi")
q.enqueue(1)
q.enqueue("Hello")
q.dequeue()
q.peek()
q.is_full()"""

class Linked_Turtle:
    def __init__(self, x=0, y=0, data = "NULL", address = "NULL", next_node = "NULL"):
        self.data = data
        self.address = address
        self.next = next_node
        self.turtle = t.Turtle()
        self.link = t.Turtle()
        self.link.width(7)
        self.turtle.turtlesize(40)
        self.data_pen = t.Turtle()
        self.next_address_pen = t.Turtle()
        self.address_pen = t.Turtle()
        self.turtle.up()
        self.data_pen.up()
        self.next_address_pen.up()
        self.address_pen.up()
        self.link.up()
        self.data_pen.ht()
        self.next_address_pen.ht()
        self.address_pen.ht()
        self.link.ht()
        self.turtle.shape("linked"+str(random.randint(1, 9))+".gif")
        self.move(x, y)
        self.turtle.onclick(fun = self.get_data)
        self.data_pen.onclick(fun = self.get_data)
        self.next_address_pen.onclick(fun = self.get_data)
        self.address_pen.onclick(fun = self.get_data)
    def move(self, x, y):
        self.turtle.setposition(x, y)
        self.data_pen.setposition(x-31, y-11)
        self.next_address_pen.setposition(x+17, y-11)
        self.address_pen.setposition(self.turtle.xcor(), self.turtle.ycor()-70)
        self.link.setposition(x+49, y)
    def get_data(self, x, y):
        self.turtle.onclick(fun = None)
        self.data_pen.onclick(fun = None)
        self.next_address_pen.onclick(fun = None)
        self.address_pen.onclick(fun = None)
        write(str(self.address)+" :: "+str(self.data)+" -> "+str(self.next))
        time.sleep(3)
        undo()
        self.turtle.onclick(fun = self.get_data)
        self.data_pen.onclick(fun = self.get_data)
        self.next_address_pen.onclick(fun = self.get_data)
        self.address_pen.onclick(fun = self.get_data)
    def write(self, index = -1):
        self.data_pen.clear()
        self.address_pen.clear()
        self.next_address_pen.clear()
        self.data_pen.write(str(self.data)[:2], align = "center", font = ("Arial", 15, "bold"))
        self.next_address_pen.write(str(self.next)[:4], align = "center", font = ("Arial", 15, "bold"))
        self.address_pen.write(str(self.address), align = "center", font = ("Arial", 15, "bold"))
    def clr(self):
        self.hide()
        self.turtle.clear()
        self.data_pen.clear()
        self.link.clear()
        self.next_address_pen.clear()
        self.address_pen.clear()
    def hide(self):
        self.data_pen.ht()
        self.turtle.ht()
        self.address_pen.ht()
        self.next_address_pen.ht()
    def set_data(self, data, address):
        self.data = data
        self.address = address
        self.write(data, address)
    def link_draw(self):
        if(self.next != None):
            self.link.down()
            self.link.forward(20)
            self.link.up()
            self.link.backward(20)

#[data, address, next, shape]
class Linked_List:
    def __init__(self, size = 7):
        global main_turtle
        self.linked_turtles = [Linked_Turtle() for i in range(size)]
        self.list = []
        for i in range(size):
            self.list.append(["NULL", "NULL", "NULL", "linked-1.gif"])
        self.capacity = size
        self.append_index = 0
        self.var = {"head":self.list[0][1]}
        self.update()
        write("Created Linked List Of Size "+str(size))
        time.sleep(3)
    def __del__(self):
        global pointer_turtle
        pointer_turtle.clear()
        for i in range(len(self.linked_turtles)):
            self.linked_turtles[0].clr()
            del self.linked_turtles[0]
    def pointer_update(self, var):
        global main_turtle, pointer_turtle
        pointer_turtle.clear()
        init_y = main_turtle.ycor()-130
        for i in list(sorted(var.keys())):
            pointer_turtle.setposition(main_turtle.xcor(), init_y)
            pointer_turtle.write(str(i)+" : "+str(var[i]), align = "center", font = ("Arial", 20, "bold"))
            init_y -= 30
    def update(self):
        #print(self.list[:self.append_index], end = "\n\n\n")
        self.pointer_update(self.var)
        if(len(self.list)>self.capacity):
            write("Linked List Limit Exceeded")
            time.sleep(3)
            undo()
            return -1
        else:
            for i in range(len(self.list)-1):
                self.list[i][2] = self.list[i+1][1]
            self.list[-1][2] = "NULL"
            count_right = 130
            count_left = -10
            n = self.capacity//2
            for i in range(n, -1, -1):
                self.linked_turtles[i].data = self.list[i][0]
                self.linked_turtles[i].address = self.list[i][1]
                if(i<len(self.list)-1):
                    self.linked_turtles[i].next = self.list[i][2]
                else:
                    self.linked_turtles[i].next = "NULL"
                self.linked_turtles[i].turtle.shape(self.list[i][3])
                self.linked_turtles[i].move(main_turtle.xcor()-count_left, main_turtle.ycor())
                self.linked_turtles[i].write(self.linked_turtles[i].data)
                if(self.linked_turtles[i].next != "NULL"):
                    self.linked_turtles[i].link_draw()
                count_left += 120
            right_index = n+1
            while(right_index<self.capacity):
                self.linked_turtles[right_index].data = self.list[right_index][0]
                self.linked_turtles[right_index].address = self.list[right_index][1]
                if(right_index<len(self.list)-1):
                    self.linked_turtles[right_index].next = self.list[right_index][2]
                else:
                    self.linked_turtles[right_index].next = "NULL"
                self.linked_turtles[right_index].turtle.shape(self.list[right_index][3])
                self.linked_turtles[right_index].move(main_turtle.xcor()+count_right, main_turtle.ycor())
                self.linked_turtles[right_index].write(self.linked_turtles[right_index].data)
                if(self.linked_turtles[right_index].next != "NULL"):
                    self.linked_turtles[right_index].link_draw()
                right_index += 1
                count_right += 120
    def gen_address(self):
        address = random.randint(100, 999)
        i = 0
        for i in range(len(self.list)):
            if(self.list[i][1] == address):
                address = random.randint(100, 999)
                i = 0
        return address
    def insert(self, pos = -1, x = "NULL"):
        if(pos == -1):
            index = self.append_index
        else:
            index = pos-1
        if(self.append_index>=self.capacity):
            write("Linked List Length Exceeded")
            time.sleep(3)
            undo()
            return -1
        self.append_index += 1
        newNode = [x, self.gen_address(), self.list[index][1], "linked"+str(random.randint(1, 9))+".gif"]
        for i in range(self.append_index-1, index, -1):
            self.list[i] = self.list[i-1]
        self.list[index] = newNode
        self.var["head"] = self.list[0][1]
        self.update()
        if(pos == -1):
            write("Inserted "+str(x)+" At End")
        else:
            write("Inserted "+str(x)+" At Position "+str(index+1))
        time.sleep(3)
    def delete(self, pos = -1):
        if(pos == -1):
            index = self.append_index
        else:
            index = pos-1
        if(index>=self.append_index):
            write("Linked List Length Exceeded")
            time.sleep(3)
            undo()
            return -1
        self.append_index -= 1
        data = self.list[index][0]
        for i in range(index, self.append_index):
            self.list[i] = self.list[i+1]
        self.list[self.append_index] = ["NULL", "NULL", "NULL", "linked-1.gif"]
        self.var["head"] = self.list[0][1]
        self.update()
        write("Deleted "+str(data)+" At Position "+str(pos))
        time.sleep(3)
    def count(self):
        var = {"head":self.var["head"], "count":0}
        for i in range(self.append_index):
            self.linked_turtles[i].turtle.shape("linkedgold.gif")
            var["count"] += 1
            self.pointer_update(var)
            write("Incrementing Count")
            time.sleep(3)
        self.pointer_update(var)
        write("There Are "+str(var["count"])+" Element(s) in Linked List")
        time.sleep(3)
        self.update()
        return var["count"]
    def search(self, data):
        var = {"current":self.var["head"]}
        for i in range(self.append_index):
            self.linked_turtles[i].turtle.shape("linkedgold.gif")
            if(self.linked_turtles[i].data != data):
                write("Going To Next Node")
                var["current"] = self.list[i][1]
                self.pointer_update(var)
                time.sleep(3)
            else:
                write(str(data)+" Found At Position "+str(i+1))
                time.sleep(3)
                self.update()
                return i+1
        write(str(data)+" Not Present in Linked List")
        time.sleep(3)
        self.update()
        return -1
    def remove(self, data):
        pos = self.search(data)
        if(pos != -1):
            self.delete(pos)
    def reverse(self):
        var = {"current":self.var["head"], "previous":"NULL", "next":"NULL"}
        for i in range(self.append_index):
            self.linked_turtles[i].link.clear()
        for i in range(self.append_index):
            self.linked_turtles[i].turtle.shape("linkedgold.gif")
            self.pointer_update(var)
            time.sleep(3)
            var["next"] = self.list[i][2]
            self.list[i][2] = var["previous"]
            self.linked_turtles[i].next_address_pen.clear()
            self.linked_turtles[i].next_address_pen.write(str(var["previous"])[:4], align = "center", font = ("Arial", 15, "bold"))
            var["previous"] = var["current"]
            self.pointer_update(var)
            var["current"] = var["next"]
            write("Updating Links")
            time.sleep(3)
        self.var["head"] = var["previous"]
        self.pointer_update(self.var)
        self.list = self.list[:self.append_index][::-1] + self.list[self.append_index:]
        self.update()
        write("Linked List Reversed")
        time.sleep(3)
        
#Init Linked Turtles
"""linked_turtles = [Linked_Turtle(data = i, address = random.randint(100, 999), next_node = 100) for i in range(7)]
count_right = 130
count_left = -10
n = 7//2
for i in range(n, -1, -1):
    linked_turtles[i].move(main_turtle.xcor()-count_left, main_turtle.ycor())
    linked_turtles[i].link_draw()
    linked_turtles[i].write(i)
    count_left += 120
right_index = n+1
while(right_index<7):
    linked_turtles[right_index].move(main_turtle.xcor()+count_right, main_turtle.ycor())
    linked_turtles[right_index].write(right_index)
    linked_turtles[right_index].link_draw()
    right_index += 1
    count_right += 120"""

"""linked = Linked_List(6)
linked.insert(1, "Hi")
linked.insert(2, "Hello")
linked.insert(1, "Yo")
linked.insert(1, "On")
linked.delete(1)
linked.remove("Hello")
linked.search("Hi")
linked.count()
linked.reverse()"""

class Tree_Turtle:
    def __init__(self, x=0, y=0, data = "NULL"):
        self.data = data
        self.turtle = t.Turtle()
        self.link = t.Turtle()
        self.link.width(7)
        self.turtle.turtlesize(40)
        self.pen = t.Turtle()
        self.turtle.up()
        self.pen.up()
        self.link.up()
        self.link.right(90)
        self.pen.ht()
        self.link.ht()
        self.turtle.shape("tree"+str(random.randint(1, 9))+".gif")
        self.move(x, y)
        self.turtle.onclick(fun = self.get_data)
        self.pen.onclick(fun = self.get_data)
    def move(self, x, y):
        self.turtle.setposition(x, y)
        self.pen.setposition(x, y-11)
        self.link.setposition(x, y)
    def get_data(self, x, y):
        self.turtle.onclick(fun = None)
        self.pen.onclick(fun = None)
        write(str(self.data))
        time.sleep(3)
        undo()
        self.turtle.onclick(fun = self.get_data)
        self.pen.onclick(fun = self.get_data)
    def write(self, index = -1):
        self.pen.clear()
        self.pen.write(str(self.data), align = "center", font = ("Arial", 15, "bold"))
    def clr(self):
        self.pen.clear()
        self.turtle.ht()
        self.link.clear()
    def hide(self):
        self.data_pen.ht()
        self.turtle.ht()
    def set_data(self, data):
        self.data = data
        self.write(data)

class Binary_Tree:
    def __init__(self, levels = 3):
        global main_turtle
        count = 0
        for i in range(levels):
            count += pow(2, i)
        self.tree_turtles = [Tree_Turtle() for i in range(count)]
        self.tree_shapes = ["tree-1.gif" for i in range(count)]
        self.height = levels
        self.append_index = 0
        self.var = {"root":self.tree_turtles[0].data}
        self.order = ""
        self.update()
        write("Created Binary Tree Of Height "+str(levels))
        time.sleep(3)
    def __del__(self):
        global pointer_turtle
        pointer_turtle.clear()
        for i in range(len(self.tree_turtles)):
            self.tree_turtles[0].clr()
            del self.tree_turtles[0]
    def pointer_update(self, var):
        global main_turtle, pointer_turtle
        pointer_turtle.clear()
        init_y = main_turtle.ycor()-130
        for i in list(sorted(var.keys())):
            pointer_turtle.setposition(main_turtle.xcor(), init_y)
            pointer_turtle.write(str(i)+" : "+str(var[i]), align = "center", font = ("Arial", 20, "bold"))
            init_y -= 30
    def update(self):
        global main_turtle
        self.var = {"root":self.tree_turtles[0].data}
        self.pointer_update(self.var)
        self.tree_turtles[0].move(main_turtle.xcor(), 250)
        cur_index = 0
        x = main_turtle.xcor()
        level = 0
        levels = [[x], [x-160, x+160], [x-240, x-80, x+80, x+240]]
        level_angles = [60, 45]
        level_forward = [116, 57]
        for i in range(0, self.height):
            for j in range(len(levels[i])):
                self.tree_turtles[cur_index].turtle.shape(self.tree_shapes[cur_index])
                self.tree_turtles[cur_index].move(levels[i][j], 225-level*100)
                self.tree_turtles[cur_index].write(self.tree_turtles[cur_index].data)
                if(level<2 and ((2*cur_index+2)<len(self.tree_turtles))):
                    self.tree_turtles[cur_index].link.clear()
                    #print(self.tree_turtles[self.get_left_child(cur_index)]+"  "+str(self.tree_turtles[self.get_right_child(cur_index)]))
                    if(self.tree_turtles[self.get_left_child(cur_index)].data!="NULL"):
                        self.tree_turtles[cur_index].link.right(level_angles[level])
                        self.tree_turtles[cur_index].link.forward(36)
                        self.tree_turtles[cur_index].link.down()
                        self.tree_turtles[cur_index].link.forward(level_forward[level])
                        self.tree_turtles[cur_index].link.up()
                        self.tree_turtles[cur_index].link.backward(level_forward[level]+36)
                        self.tree_turtles[cur_index].link.left(level_angles[level])
                    if(self.tree_turtles[self.get_right_child(cur_index)].data!="NULL"):
                        self.tree_turtles[cur_index].link.left(level_angles[level])
                        self.tree_turtles[cur_index].link.up()
                        self.tree_turtles[cur_index].link.forward(36)
                        self.tree_turtles[cur_index].link.down()
                        self.tree_turtles[cur_index].link.forward(level_forward[level])
                        self.tree_turtles[cur_index].link.up()
                        self.tree_turtles[cur_index].link.setposition(self.tree_turtles[cur_index].turtle.xcor(), self.tree_turtles[cur_index].turtle.ycor())
                        self.tree_turtles[cur_index].link.right(level_angles[level])
                cur_index += 1
            level += 1
    def insert(self, data):
        if(self.append_index>=len(self.tree_turtles)):
            write("Binary Tree Limit Exceeded")
            time.sleep(3)
            return -1
        self.tree_turtles[self.append_index].data = data
        self.tree_shapes[self.append_index] = "tree"+str(random.randint(1, 9))+".gif"
        self.append_index += 1
        self.update()
        write("Inserted "+str(data)+" In Binary Tree")
        time.sleep(3)
    def search(self, data):
        for i in range(self.append_index):
            self.tree_turtles[i].turtle.shape("treegold.gif")
            write("Searching For "+str(data))
            time.sleep(3)
            if(self.tree_turtles[i].data == data):
                write(str(data)+" Found At Index "+str(i))
                time.sleep(3)
                self.update()
                return i
        write(str(data)+" Not Present in Binary Tree")
        time.sleep(3)
        self.update()
        return -1
    def delete(self, data):
        index = self.search(data)
        if(index != -1):
            if(self.append_index != 1):
                self.tree_turtles[index].turtle.shape("treegold.gif")
                self.tree_turtles[self.append_index-1].turtle.shape("treegold.gif")
                write("Replacing With RightMost Node")
                time.sleep(3)
                (self.tree_turtles[index].data, self.tree_turtles[self.append_index-1].data) = (self.tree_turtles[self.append_index-1].data, self.tree_turtles[index].data)
                (self.tree_shapes[index], self.tree_shapes[self.append_index-1]) = (self.tree_shapes[self.append_index-1], self.tree_shapes[index])
                self.update()
                time.sleep(3)
                write("Deleting RightMost Node")
                self.tree_turtles[self.append_index-1].data = "NULL"
                self.tree_shapes[self.append_index-1] = "tree-1.gif"
                self.update()
                time.sleep(3)
                write("Deleted "+str(data)+" From Binary Tree")
            else:
                self.tree_turtles[index].turtle.shape("treegold.gif")
                write("Deleting Root "+str(data)+" From Binary Tree")
                time.sleep(3)
                self.tree_turtles[index].data = "NULL"
                self.tree_shapes[index] = "tree-1.gif"
                self.update()
                time.sleep(3)
                write("Deleted "+str(data)+" From Binary Tree")
            self.append_index -= 1
    def count(self):
        count = 0
        var = {"count":0}
        for i in range(self.append_index):
            self.tree_turtles[i].turtle.shape("treegold.gif")
            write("Incrementing Count")
            count += 1
            var["count"] += 1
            self.pointer_update(var)
            time.sleep(3)
        write("There are "+str(count)+" Element(s) in Binary Tree")
        time.sleep(3)
        self.update()
        return count
    def level_order(self):
        s = ""
        for i in range(self.append_index):
            self.tree_turtles[i].turtle.shape("treegold.gif")
            if(i==self.append_index-1):
                s += str(self.tree_turtles[i].data)
            else:
                s += str(self.tree_turtles[i].data)+", "
            write("Level Order: "+s)
            time.sleep(3)
        self.update()
    def get_right_child(self, index):
        res = 2*index + 2
        if(res>=len(self.tree_turtles)):
            return -1
        return res
    def get_left_child(self, index):
        res = 2*index + 1
        if(res>=len(self.tree_turtles)):
            return -1
        return res
    def pre_order(self, index = 0, num = 1):
        if(num == 1):
            self.order = ""
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.tree_turtles[index].turtle.shape("treegold.gif")
            self.order += str(self.tree_turtles[index].data) + ", "
            write("Pre Order: "+str(self.order))
            time.sleep(3)
            self.pre_order(self.get_left_child(index), 2)
            self.pre_order(self.get_right_child(index), 2)
        if(num == 1):
            self.update()
    def in_order(self, index = 0, num = 1):
        if(num == 1):
            self.order = ""
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.in_order(self.get_left_child(index), 2)
            self.tree_turtles[index].turtle.shape("treegold.gif")
            self.order += str(self.tree_turtles[index].data) + ", "
            write("In Order: "+str(self.order))
            time.sleep(3)
            self.in_order(self.get_right_child(index), 2)
        if(num == 1):
            self.update()
    def post_order(self, index = 0, num = 1):
        if(num == 1):
            self.order = ""
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.post_order(self.get_left_child(index), 2)
            self.post_order(self.get_right_child(index), 2)
            self.tree_turtles[index].turtle.shape("treegold.gif")
            self.order += str(self.tree_turtles[index].data) + ", "
            write("Post Order: "+str(self.order))
            time.sleep(3)
        if(num == 1):
            self.update()
                

#Init Tree Turtles (Array Representation)
"""
tree_turtles = [Tree_Turtle() for i in range(7)]
tree_turtles[0].move(main_turtle.xcor(), 250)
cur_index = 0
x = main_turtle.xcor()
level = 0
levels = [[x], [x-160, x+160], [x-240, x-80, x+80, x+240]]
level_angles = [60, 45]
level_forward = [116, 57]
for i in range(0, 3):
    for j in range(len(levels[i])):
        tree_turtles[cur_index].move(levels[i][j], 225-level*100)
        tree_turtles[cur_index].write(cur_index)
        if(level<2):
            tree_turtles[cur_index].link.right(level_angles[level])
            tree_turtles[cur_index].link.forward(36)
            tree_turtles[cur_index].link.down()
            tree_turtles[cur_index].link.forward(level_forward[level])
            tree_turtles[cur_index].link.up()
            tree_turtles[cur_index].link.backward(level_forward[level]+36)
            tree_turtles[cur_index].link.left(2*level_angles[level])
            tree_turtles[cur_index].link.up()
            tree_turtles[cur_index].link.forward(36)
            tree_turtles[cur_index].link.down()
            tree_turtles[cur_index].link.forward(level_forward[level])
            tree_turtles[cur_index].link.up()
            tree_turtles[cur_index].link.setposition(tree_turtles[cur_index].turtle.xcor(), tree_turtles[cur_index].turtle.ycor())
            tree_turtles[cur_index].link.right(level_angles[level])
        cur_index += 1
    level += 1"""

"""tree = Binary_Tree(3)
tree.insert("Hello")
tree.insert("What")
tree.insert("Yo")
tree.insert("Yup")
tree.delete("Hello")
tree.pre_order()
tree.in_order()
tree.post_order()
tree.level_order()
tree.count()"""

class Binary_Search_Tree:
    def __init__(self, levels = 3):
        global main_turtle
        count = 0
        for i in range(levels):
            count += pow(2, i)
        self.tree_turtles = [Tree_Turtle() for i in range(count)]
        self.tree_shapes = ["tree-1.gif" for i in range(count)]
        self.height = levels
        self.append_index = 0
        self.var = {"root":self.tree_turtles[0].data}
        self.order = ""
        self.update()
        write("Created Binary Search Tree Of Height "+str(levels))
        time.sleep(3)
    def __del__(self):
        global pointer_turtle
        pointer_turtle.clear()
        for i in range(len(self.tree_turtles)):
            self.tree_turtles[0].clr()
            del self.tree_turtles[0]
    def pointer_update(self, var):
        global main_turtle, pointer_turtle
        pointer_turtle.clear()
        init_y = main_turtle.ycor()-130
        for i in list(sorted(var.keys())):
            pointer_turtle.setposition(main_turtle.xcor(), init_y)
            pointer_turtle.write(str(i)+" : "+str(var[i]), align = "center", font = ("Arial", 20, "bold"))
            init_y -= 30
    def update(self):
        global main_turtle
        self.var = {"root":self.tree_turtles[0].data}
        self.pointer_update(self.var)
        self.tree_turtles[0].move(main_turtle.xcor(), 250)
        cur_index = 0
        x = main_turtle.xcor()
        level = 0
        levels = [[x], [x-160, x+160], [x-240, x-80, x+80, x+240]]
        level_angles = [60, 45]
        level_forward = [116, 57]
        for i in range(0, self.height):
            for j in range(len(levels[i])):
                self.tree_turtles[cur_index].turtle.shape(self.tree_shapes[cur_index])
                self.tree_turtles[cur_index].move(levels[i][j], 225-level*100)
                self.tree_turtles[cur_index].write(self.tree_turtles[cur_index].data)
                if(level<2 and ((2*cur_index+2)<len(self.tree_turtles))):
                    self.tree_turtles[cur_index].link.clear()
                    #print(self.tree_turtles[self.get_left_child(cur_index)]+"  "+str(self.tree_turtles[self.get_right_child(cur_index)]))
                    if(self.tree_turtles[self.get_left_child(cur_index)].data!="NULL"):
                        self.tree_turtles[cur_index].link.right(level_angles[level])
                        self.tree_turtles[cur_index].link.forward(36)
                        self.tree_turtles[cur_index].link.down()
                        self.tree_turtles[cur_index].link.forward(level_forward[level])
                        self.tree_turtles[cur_index].link.up()
                        self.tree_turtles[cur_index].link.backward(level_forward[level]+36)
                        self.tree_turtles[cur_index].link.left(level_angles[level])
                    if(self.tree_turtles[self.get_right_child(cur_index)].data!="NULL"):
                        self.tree_turtles[cur_index].link.left(level_angles[level])
                        self.tree_turtles[cur_index].link.up()
                        self.tree_turtles[cur_index].link.forward(36)
                        self.tree_turtles[cur_index].link.down()
                        self.tree_turtles[cur_index].link.forward(level_forward[level])
                        self.tree_turtles[cur_index].link.up()
                        self.tree_turtles[cur_index].link.setposition(self.tree_turtles[cur_index].turtle.xcor(), self.tree_turtles[cur_index].turtle.ycor())
                        self.tree_turtles[cur_index].link.right(level_angles[level])
                cur_index += 1
            level += 1
    def insert(self, data, index = 0):
        #print(index)
        if(index == -1):
            write("Binary Search Tree Limit Exceeded")
            self.update()
            time.sleep(3)
            return -1
        if(self.tree_turtles[index].data == "NULL"):
            self.tree_turtles[index].data = data
            self.tree_shapes[index] = "tree"+str(random.randint(1, 9))+".gif"
            self.update()
            write("Inserted "+str(data)+" In Binary Search Tree")
            time.sleep(3)
            return 1
        if(data < self.tree_turtles[index].data):
            #print("Lesser")
            self.tree_turtles[index].turtle.shape("treegold.gif")
            time.sleep(3)
            self.insert(data, self.get_left_child(index))
        elif(data > self.tree_turtles[index].data):
            #print("Greater")
            self.tree_turtles[index].turtle.shape("treegold.gif")
            time.sleep(3)
            self.insert(data, self.get_right_child(index))
    def search(self, data, index = 0):
        if(index == -1):
            write("Binary Search Tree Limit Exceeded")
            self.update()
            time.sleep(3)
            return -1
        if(self.tree_turtles[index].data == "NULL"):
            self.update()
            write(str(data)+" Not Present In Binary Search Tree")
            time.sleep(3)
            return 1
        if(data < self.tree_turtles[index].data):
            self.tree_turtles[index].turtle.shape("treegold.gif")
            time.sleep(3)
            self.search(data, self.get_left_child(index))
        elif(data > self.tree_turtles[index].data):
            self.tree_turtles[index].turtle.shape("treegold.gif")
            time.sleep(3)
            self.search(data, self.get_right_child(index))
        else:
            self.tree_turtles[index].turtle.shape("treegold.gif")
            write(str(data)+" Found at Index "+str(index))
            time.sleep(3)
            self.update()
    def min(self, index = 0, data = "NULL"):
        if(self.tree_turtles[0].data == "NULL"):
            write("Empty Binary Search Tree")
            time.sleep(3)
            return -1
        if(index>=0 and index<len(self.tree_turtles)):
            self.tree_turtles[index].turtle.shape("treegold.gif")
            time.sleep(3)
            #print(index)
            if(self.get_left_child(index)>=0):
                if(self.tree_turtles[self.get_left_child(index)].data != "NULL"):
                    self.min(self.get_left_child(index))
                else:
                    write("Minimum Element in Sub-Tree is "+str(self.tree_turtles[index].data))
                    time.sleep(3)
                    self.update()
                    return index
            else:
                write("Minimum Element in Sub-Tree is "+str(self.tree_turtles[index].data))
                time.sleep(3)
                self.update()
                return index
        self.update()
        return -1
    def delete(self, data, index = 0, num = 1):
        if(index>=0):
            self.tree_turtles[index].turtle.shape("treegold.gif")
            time.sleep(3)
            if(self.tree_turtles[index].data == "NULL"):
                return "NULL"
            if(data < self.tree_turtles[index].data):
                self.delete(data, self.get_left_child(index), 2)
            elif(data > self.tree_turtles[index].data):
                self.delete(data, self.get_right_child(index), 2)
            else:
                (left_index, right_index) = (self.get_left_child(index), self.get_right_child(index))
                if(left_index<0 and right_index<0):
                    self.tree_turtles[index].data = "NULL"
                    self.tree_shapes[index] = "tree-1.gif"
                    write("Deleted "+str(data)+" From Binary Search Tree")
                    self.update()
                    time.sleep(3)
                    return
                if(left_index>=0 and left_index<len(self.tree_turtles) and self.tree_turtles[left_index].data == "NULL"):
                    self.tree_turtles[index].data = self.tree_turtles[right_index].data
                    self.tree_shapes[index] = self.tree_shapes[right_index]
                    self.tree_turtles[right_index].data = "NULL"
                    self.tree_shapes[right_index] = "tree-1.gif"
                    write("Deleted "+str(data)+" From Binary Search Tree")
                    self.update()
                    time.sleep(3)
                elif(right_index>=0 and right_index<len(self.tree_turtles) and self.tree_turtles[right_index].data == "NULL"):
                    self.tree_turtles[index].data = self.tree_turtles[left_index].data
                    self.tree_shapes[index] = self.tree_shapes[left_index]
                    self.tree_turtles[left_index].data = "NULL"
                    self.tree_shapes[left_index] = "tree-1.gif"
                    write("Deleted "+str(data)+" From Binary Search Tree")
                    self.update()
                    time.sleep(3)
                else:
                    min_index = self.min(right_index)
                    if(min_index>=0 and min_index<len(self.tree_turtles)):
                        self.tree_turtles[index].data = self.tree_turtles[min_index].data
                        self.tree_shapes[index] = self.tree_shapes[min_index]
                        self.delete(self.tree_turtles[min_index].data, right_index, 2)
                        if(num == 1):
                            write("Deleted "+str(data)+" From Binary Search Tree")
                        self.update()
                        time.sleep(3)
                        return 1
                    else:
                        write("Binary Search Tree Limit Exceeded")
                        self.update()
                        time.sleep(3)
                        return -1
    def count(self, index = 0, num = 1):
        if(num == 1):
            self.order = 0
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.count(self.get_left_child(index), 2)
            self.tree_turtles[index].turtle.shape("treegold.gif")
            write("Incrementing Count ")
            self.order += 1
            self.pointer_update({"count":self.order})
            time.sleep(3)
            self.count(self.get_right_child(index), 2)
        if(num == 1):
            self.update()
            write("There are "+str(self.order)+" Element(s) in Binary Tree")
            time.sleep(3)
            self.update()
            return self.order
    def level_order(self):
        s = ""
        for i in range(len(self.tree_turtles)):
            if(self.tree_turtles[i].data != "NULL"):
                self.tree_turtles[i].turtle.shape("treegold.gif")
                s += str(self.tree_turtles[i].data)+", "
            write("Level Order: "+s)
            time.sleep(3)
        self.update()
    def get_right_child(self, index):
        res = 2*index + 2
        if(res>=len(self.tree_turtles)):
            return -1
        return res
    def get_left_child(self, index):
        res = 2*index + 1
        if(res>=len(self.tree_turtles)):
            return -1
        return res
    def pre_order(self, index = 0, num = 1):
        if(num == 1):
            self.order = ""
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.tree_turtles[index].turtle.shape("treegold.gif")
            self.order += str(self.tree_turtles[index].data) + ", "
            write("Pre Order: "+str(self.order))
            time.sleep(3)
            self.pre_order(self.get_left_child(index), 2)
            self.pre_order(self.get_right_child(index), 2)
        if(num == 1):
            self.update()
    def in_order(self, index = 0, num = 1):
        if(num == 1):
            self.order = ""
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.in_order(self.get_left_child(index), 2)
            self.tree_turtles[index].turtle.shape("treegold.gif")
            self.order += str(self.tree_turtles[index].data) + ", "
            write("In Order: "+str(self.order))
            time.sleep(3)
            self.in_order(self.get_right_child(index), 2)
        if(num == 1):
            self.update()
    def post_order(self, index = 0, num = 1):
        if(num == 1):
            self.order = ""
        if(index>=0 and self.tree_turtles[index].data != "NULL"):
            self.post_order(self.get_left_child(index), 2)
            self.post_order(self.get_right_child(index), 2)
            self.tree_turtles[index].turtle.shape("treegold.gif")
            self.order += str(self.tree_turtles[index].data) + ", "
            write("Post Order: "+str(self.order))
            time.sleep(3)
        if(num == 1):
            self.update()

"""tree = Binary_Search_Tree(3)
tree.insert(10)
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(100)
#tree.delete(10)
#tree.delete(5)
#tree.delete(100)
#tree.delete(3)
tree.level_order()
tree.pre_order()
tree.in_order()
tree.post_order()
#tree.count()
#tree.search(100)"""
"""
objects = ['s1', 's2', 's3', 'l1', 'l2', 'a1']
final = {'stack': [['s1', 'int', '5', ['push(5)']], ['s2', 'int', '6', ['pop()']], ['s3', 'int', '4', ['pop()', 'push(4)']]], 'list': [['l1', 'char', '6', ['insert(1,4)', 'pop()']], ['l2', 'char', '5']], 'array': [['a1', 'int', '9']]}
"""

check = 0

def extract(meth):
    name = meth[:meth.index("(")]
    
    vals = list((meth[meth.index("(")+1:-1]).split(","))
    for i in range(len(vals)):
        vals[i] = vals[i].strip()
    res = []
    res.append(name)
    res.append(vals)
    return res

def set_check(x, y):
    global check
    check = 1
    return

def loop():
    global next_turtle, check
    check = 0
    while(check == 0):
        next_turtle.onclick(fun = set_check)
    return

def rest():
    os.startfile(sys.argv[0])
    sys.exit()

def run(objects, final):
    global root, win, init_dir, main_turtle, ins_turtle, next_turtle, ds_turtle, main_turtle_left, pointer_turtle, msg_stack
    temp_dir = os.getcwd()
    os.chdir(init_dir)
    #root = tkinter.Toplevel()
    #root.withdraw()

    win = t.Screen()
    win.setup(1250, 700, 100, 75)
    win.delay(0)
    win.bgpic("background.gif")
    win.addshape("background.gif")
    win.addshape("ds.gif")
    win.addshape("arr1.gif")
    win.addshape("arr2.gif")
    win.addshape("arr3.gif")
    win.addshape("arr4.gif")
    win.addshape("arr5.gif")
    win.addshape("arr6.gif")
    win.addshape("arr7.gif")
    win.addshape("arr8.gif")
    win.addshape("arr9.gif")
    win.addshape("arr-1.gif")
    win.addshape("arrred.gif")
    win.addshape("arrgreen.gif")
    win.addshape("arrgold.gif")
    win.addshape("stack1.gif")
    win.addshape("stack2.gif")
    win.addshape("stack3.gif")
    win.addshape("stack4.gif")
    win.addshape("stack5.gif")
    win.addshape("stack6.gif")
    win.addshape("stack7.gif")
    win.addshape("stack8.gif")
    win.addshape("stack9.gif")
    win.addshape("stack-1.gif")
    win.addshape("stackgold.gif")
    win.addshape("stackcontainer.gif")
    win.addshape("linked1.gif")
    win.addshape("linked2.gif")
    win.addshape("linked3.gif")
    win.addshape("linked4.gif")
    win.addshape("linked5.gif")
    win.addshape("linked6.gif")
    win.addshape("linked7.gif")
    win.addshape("linked8.gif")
    win.addshape("linked9.gif")
    win.addshape("linked-1.gif")
    win.addshape("linkedgold.gif")
    win.addshape("tree1.gif")
    win.addshape("tree2.gif")
    win.addshape("tree3.gif")
    win.addshape("tree4.gif")
    win.addshape("tree5.gif")
    win.addshape("tree6.gif")
    win.addshape("tree7.gif")
    win.addshape("tree8.gif")
    win.addshape("tree9.gif")
    win.addshape("tree-1.gif")
    win.addshape("treegold.gif")
    win.addshape("next_ds.gif")
    win.addshape("next_method.gif")
    win.addshape("next.gif")

    main_turtle = t.Turtle()
    ins_turtle = t.Turtle()
    next_turtle = t.Turtle()
    ds_turtle = t.Turtle()
    main_turtle_left = t.Turtle()
    pointer_turtle = t.Turtle()

    main_turtle.up()
    ins_turtle.up()
    next_turtle.up()
    ds_turtle.up()
    main_turtle_left.up()
    pointer_turtle.up()
    main_turtle_left.ht()
    main_turtle.ht()
    ins_turtle.ht()
    ds_turtle.ht()
    pointer_turtle.ht()

    main_turtle.setposition(-156.5, 61.5)
    ins_turtle.setposition(-156.5, -280)
    ds_turtle.setposition(454, 290)
    main_turtle_left.setposition(-400, 61.5)
    next_turtle.setposition(454, -265)
    next_turtle.shape("next_ds.gif")
    ins_turtle.write("Welcome!", align = "center", font = ("Arial", 20, "bold"))
    msg_stack = ["Welcome!"]
    data_type = "str"
    while(len(objects)>0):
        del_ds()
        init_screen()
        init_ds(objects)
        next_turtle.shape("next_ds.gif")
        loop()
        cur_obj = objects[0]
        (cur_ds, cur_cap, cur_methods) = ("NULL", "NULL", "NULL")
        for i in final.keys():
            for j in final[i]:
                if(j[0] == cur_obj):
                    cur_ds = i
                    cur_cap = int(j[2])
                    data_type = j[1]
                    try:
                        cur_methods = j[3]
                    except:
                        cur_methods = []
                    break
        #print(cur_ds, cur_cap, cur_methods)
        #print(data_type)
        if(cur_ds == "stack"):
            obj = Stack(cur_cap)
        elif(cur_ds == "linkedlist"):
            obj = Linked_List(cur_cap)
        elif(cur_ds == "array"):
            obj = Array(cur_cap)
        elif(cur_ds == "queue"):
            obj = Queue(cur_cap)
        elif(cur_ds == "binarytree"):
            obj = Binary_Tree(cur_cap)
        elif(cur_ds == "binarysearchtree"):
            obj = Binary_Search_Tree(cur_cap)
        while(len(cur_methods)>0):
            next_turtle.shape("next_method.gif")
            loop()
            write("Executing "+str(cur_methods[0]))
            time.sleep(3)
            res = extract(cur_methods[0])
            name = res[0]
            try:
                if(len(res[1])>1):
                    for i in range(1, len(res)):
                        if(data_type == "str"):
                            res[1][i] = str(res[1][i])
                        if(data_type == "int"):
                            res[1][i] = int(res[1][i])
                        if(data_type == "float"):
                            res[1][i] = float(res[1][i])
                elif(len(res[1])==1):
                    if(data_type == "str"):
                            res[1][0] = str(res[1][0])
                    if(data_type == "int"):
                            res[1][0] = int(res[1][0])
                    if(data_type == "float"):
                            res[1][0] = float(res[1][0])
            except:
                pass                     
            if(cur_ds == "array"):
                if(name == "set"):
                    obj.set(int(res[1][0]), res[1][1])
                elif(name == "get"):
                    obj.get(int(res[1][0]))
                elif(name == "insert"):
                    obj.insert(int(res[1][0]), res[1][1])
                elif(name == "append"):
                    obj.append(res[1][0])
                elif(name == "delete"):
                    obj.delete(int(res[1][0]))
                elif(name == "pop"):
                    obj.pop()
                elif(name == "search"):
                    obj.search(res[1][0])
                elif(name == "reverse"):
                    obj.reverse()
                elif(name == "count"):
                    obj.count()
                elif(name == "sort"):
                    obj.sort()
            elif(cur_ds == "stack"):
                if(name == "push"):
                    obj.push(res[1][0])
                elif(name == "pop"):
                    obj.pop()
                elif(name == "peek"):
                    obj.peek()
                elif(name == "size"):
                    obj.size()
                elif(name == "is_empty"):
                    obj.is_empty()
                elif(name == "is_full"):
                    obj.is_full()
            elif(cur_ds == "queue"):
                if(name == "enqueue"):
                    obj.enqueue(res[1][0])
                elif(name == "dequeue"):
                    obj.dequeue()
                elif(name == "peek"):
                    obj.peek()
                elif(name == "size"):
                    obj.size()
                elif(name == "is_empty"):
                    obj.is_empty()
                elif(name == "is_full"):
                    obj.is_full()
            elif(cur_ds == "linkedlist"):
                try:
                    if(name == "insert"):
                        obj.insert(int(res[1][0]), res[1][1])
                except:
                    obj.insert(-1, res[-1][0])
                if(name == "delete"):
                    obj.delete(int(res[1][0]))
                elif(name == "count"):
                    obj.count()
                elif(name == "search"):
                    obj.search(res[1][0])
                elif(name == "remove"):
                    obj.remove(res[1][0])
                elif(name == "reverse"):
                    obj.reverse()
            elif(cur_ds == "binarytree" or cur_ds == "binarysearchtree"):
                if(name == "insert"):
                    obj.insert(res[1][0])
                elif(name == "search"):
                    obj.search(res[1][0])
                elif(name == "delete"):
                    obj.delete(res[1][0])
                elif(name == "count"):
                    obj.count()
                elif(name == "level_order"):
                    obj.level_order()
                elif(name == "pre_order"):
                    obj.pre_order()
                elif(name == "post_order"):
                    obj.post_order()
                elif(name == "in_order"):
                    obj.in_order()
            write(str(cur_methods[0])+" Executed! Press Next To Continue")
            cur_methods = cur_methods[1:]
        write(cur_obj+" Executed! Press Next To Continue")
        next_turtle.shape("next_ds.gif")
        loop()
        try:
            del obj
        except:
            pass
        objects = objects[1:]
    write("Press Next To Exit")
    loop()
    t.bye()
    #rest()
    os.chdir(temp_dir)
    del win
    del main_turtle
    del ins_turtle
    del next_turtle
    del ds_turtle
    del main_turtle_left
    del pointer_turtle
    del msg_stack
    os.system("taskkill /f /im pythonw.exe")
    return


l = []
clrprint("Type \"help\" To Check Commands", clr = "blue")
os.chdir("scripts")
scripts = os.listdir()
cur_name= ""
class MyPrompt(Cmd):
   def do_exit(self, inp):
        """Exit Interface"""
        clrprint("Bye", clr = "blue")
        return True

   def do_list(self, inp):
        """List All Scripts"""
        clrprint("\nExisting Scripts:", clr = "blue")
        for i in scripts:
            if(".py" in i[-3:]):
               clrprint(i[:-3], clr = "blue")
 
   def do_add(self, inp):
        """Add New Script"""
        global scripts
        clrprint("\nExisting Scripts:", clr = "green")
        for i in scripts:
            if(".py" in i[-3:]):
               clrprint(i[:-3], clr = "green")
        clrprint("Enter Script To Add:", clr = "green")
        name = input()
        name += ".py"
        if name in scripts:
            clrprint("Error: Script Name Already Exists!", clr = "green")
        else:
            clrprint("Successfully Created Script!", clr = "green")
            with open(name, "w") as f:
                pass
            scripts = os.listdir()
            
   def do_remove(self, inp):
       """Remove Script"""
       global scripts
       clrprint("\nExisting Scripts:", clr = "red")
       for i in scripts:
            if(".py" in i[-3:]):
               clrprint(i[:-3], clr = "red")
       clrprint("Enter Script To Remove:", clr = "red")
       name = input()
       name += ".py"
       if name not in scripts:
           clrprint("Error: File Not Found!", clr = "red")
       else:
           os.remove(name)
           clrprint("Successfully Removed Script!", clr = "red")
           scripts = os.listdir()    
   def do_view(self, inp):
      """View Script"""
      global scripts
      clrprint("\nExisting Scripts:", clr = "blue")
      for i in scripts:
            if(".py" in i[-3:]):
               clrprint(i[:-3], clr = "blue")
      clrprint("Enter Script To View:", clr = "blue")
      name = input()
      name += ".py"
      if name not in scripts:
           clrprint("Error: File Not Found!", clr = "blue")
      else:
           print(name[:-3]+"\n")
           with open(name, "r") as f:
              lines = list(f.readlines())
              for i in range(len(lines)):
                 print(str(i+1)+".   "+lines[i], end = "")
                 
   def do_edit(self, inp):
      """Edit Script"""
      global scripts, cur_name, txt_edit
      clrprint("\nExisting Scripts:", clr = "blue")
      for i in scripts:
            if(".py" in i[-3:]):
               clrprint(i[:-3], clr = "blue")
      clrprint("Enter Script To Edit:", clr = "blue")
      name = input()
      name += ".py"
      if name not in scripts:
           clrprint("Error: File Not Found!", clr = "blue")
      else:
         cur_name = name
         window = tk.Tk()
         window.title(name[:-3])
         window.rowconfigure(0, minsize=800, weight=1)
         window.columnconfigure(1, minsize=800, weight=1)
         window.attributes('-topmost',True)

         txt_edit = tk.Text(window)
         fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

         with open(os.getcwd()+"/"+name, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
         
         btn_save = tk.Button(fr_buttons, text="Save", command=save_file)
         btn_save.grid(row=1, column=0, sticky="ew", padx=5)

         fr_buttons.grid(row=0, column=0, sticky="ns")
         txt_edit.grid(row=0, column=1, sticky="nsew")

         window.mainloop()
   def do_visualize(self, inp):
      """Compile and Show Visualization"""
      global scripts, cur_name, txt_edit
      scripts = os.listdir()
      clrprint("\nExisting Scripts:", clr = "blue")
      for i in scripts:
            if(".py" in i[-3:]):
               clrprint(i[:-3], clr = "blue")
      clrprint("Enter Script To Visualize:", clr = "blue")
      name = input()
      name += ".py"
      if name not in scripts:
         clrprint("Error: File Not Found!", clr = "blue")
      else:
         cur_name = name
      instructions=[(re.sub(r'\s+','',i)) for i in filter(lambda x : x.strip(),open(os.getcwd()+"/"+name,"r").readlines())]
      instructiondeclaration=[]
      for i in range(len(instructions)):
          instructiondeclaration.append(instructions[i])
          if(instructions[i+1]=="init:"):
                break
      declaration = instructiondeclaration[1:]
      instructioninitialisation=[]
      for i in instructions:
          if i not in instructiondeclaration:
                if i == "code:":
                    break
                instructioninitialisation.append(i)
      initialisation=instructioninitialisation[1:]
      code=[i for i in instructions if i not in instructiondeclaration and i not in instructioninitialisation][1:]
      structures=[i.split('<')[0] for i in declaration]
      objects=[i.split(">")[1].split("(")[0] for i in declaration]
      data_types=[i.split("<")[1].split(">")[0] for i in declaration]
      capacity=[i.split("(")[1].split(")")[0] for i in declaration]
      methods={}
      for i in code:
          j=i.split('.')[0]
          k=i.split('.')[1]
          if j in methods:
                methods[j].append(k)
          else:
                methods[j]=[k]

      output = {}
      for t, o in zip(structures, objects):
          if t in output:
                output[t].append(o)
          else:
                output[t] = [o]

      valu=[]
      obj=[]
      for i in initialisation:
          j=i.split("=")
          k1=j[0].strip()
          k2=j[1].strip()
          obj.append(k1)
          valu.append(k2)
      dict1=dict(zip(obj,valu))
      dict1 = {k: ast.literal_eval(v) for k, v in dict1.items()}
      output1 = {}
      for data_structure, names in output.items():
          output1[data_structure] = {}
          for name in names:
                output1[data_structure][name] = dict1.get(name, [])

      output2= {}
      for data_structure, values in output1.items():
          operation = initialise.get(data_structure, None)
          if operation is None:
                continue
          for ds, ds_values in values.items():
                if ds_values:
                    output2[ds] = [f"{operation}({value})" for value in ds_values]

      final={}
      for i in range(len(structures)):
          if structures[i] in final:
                final[structures[i]].append([objects[i],data_types[i],capacity[i]])
          else:
                final[structures[i]]=[[objects[i],data_types[i],capacity[i]]]

      for key1, value1 in output2.items():
          [v.extend(value1) for key2, values in final.items() for v in values if key1 == v[0]]
      for key1, value1 in methods.items():
          [v.extend(value1) for key2, values in final.items() for v in values if key1 == v[0]]

      for structure_type, nested_lists in final.items():
          default_capacity = maxCapacity.get(structure_type)
          for nested_list in nested_lists:
                if not nested_list[2]:
                    nested_list[2] = default_capacity


      for structure_type, nested_lists in final.items():
          for nested_list in nested_lists:
                nested_list[2] = int(nested_list[2])


      converted_data = {
        key: [[x[0], x[1], x[2], x[3:]] for x in value]
        for key, value in final.items()
      }
      run(objects, converted_data)
      """
      for i in range(len(instructions)):
          instructiondeclaration.append(instructions[i])
          if(instructions[i+1]=="init:" or instructions[i+1]=="Init:" or instructions[i+1]=="INIT:"):
              break
      declaration = instructiondeclaration[1:]
      instructioninitialisation=[]
      for i in instructions:
          if i not in instructiondeclaration:
              if i=="Code:" or i=="code:" or i=="CODE:":
                  break
              instructioninitialisation.append(i)
      initialisation=instructioninitialisation[1:]
      code=[i for i in instructions if i not in instructiondeclaration and i not in instructioninitialisation][1:]
      structures=[i.split('<')[0] for i in declaration]
      objects=[i.split(">")[1].split("(")[0] for i in declaration]
      data_types=[i.split("<")[1].split(">")[0] for i in declaration]
      capacity=[i.split("(")[1].split(")")[0] for i in declaration]
      methods={}
      for i in code:
          j=i.split('.')[0]
          k=i.split('.')[1]
          if j in methods:
              methods[j].append(k)
          else:
              methods[j]=[k]
      final={}
      for i in range(len(structures)):
          if structures[i] in final:
              final[structures[i]].append([objects[i],data_types[i],capacity[i]])
          else:
              final[structures[i]]=[[objects[i],data_types[i],capacity[i]]]
      for key1, value1 in methods.items():
          [v.append(value1) for key2, values in final.items() for v in values if key1 == v[0]]"""
      

def save_file():
    """Save the current file as a new file."""
    global cur_name, txt_edit
    filepath = os.getcwd()+"/"+cur_name
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    messagebox.showinfo(cur_name[:-3], "File Saved Successfully")


MyPrompt.prompt = "::"
MyPrompt().cmdloop()
