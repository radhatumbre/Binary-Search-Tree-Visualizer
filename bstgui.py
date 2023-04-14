import math
import tkinter as tk
from tkinter import messagebox

from bst import *
import time


# init tk
root = tk.Tk()
root.title("BST - Radha Tumbre Project")
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))


# create Main Canvas
myCanvas = tk.Canvas(root, bg="white", height=height, width=width)


titlecanvas = myCanvas.create_rectangle(0, 0, width, height*0.07, fill='#027373')
drawingspace = myCanvas.create_rectangle(0, height*0.07, width*0.7, height, fill='#F2E7DC')
leftnav = myCanvas.create_rectangle(width*0.7, height*0.07, width, height, fill='#0D0D0D')


# add title name in the canvas
myCanvas.create_text(width*0.5, 32, text="Binary Search Tree", fill="white", font=('Helvetica 30 bold'))
myCanvas.pack()



tree = None
def get_level(node, data, level=0):
    if node.data == data:
        return level
    if data < node.data:
        if node.left:
            return get_level(node.left,data,level+1)
    else:
        if node.right:
            return get_level(node.right,data,level+1)

    return level

def draw_tree(node, x, y, x_offset, y_offset):
    if node is not None:
        # Draw the current node
        myCanvas.create_oval(x-25, y-25, x+25, y+25, fill="#A9D9D0", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'))

        # Draw the left child node and the edge between current node and its left child
        if node.left is not None:
            x_left = x - x_offset
            y_left = y + y_offset
            myCanvas.create_line(x, y+25, x_left, y_left-25)
            draw_tree(node.left, x_left, y_left, x_offset/2, y_offset+50)

        # Draw the right child node and the edge between current node and its right child
        if node.right is not None:
            x_right = x + x_offset
            y_right = y + y_offset
            myCanvas.create_line(x, y+25, x_right, y_right-25)
            draw_tree(node.right, x_right, y_right, x_offset/2, y_offset+50)


def insert_fnc():
    global tree
    items = insert_elements.get().split(" ")
    for i in items:
        tree = insert(tree,int(i))
        draw_tree(tree, width/3, height*0.15, width/7, 100)
    insert_entry.delete(0, 'end')
    return tree


def delete_fnc():
    global tree
    items = delete_elements.get().split(" ")
    # delete previous tree
    myCanvas.delete("all")
    titlecanvas = myCanvas.create_rectangle(0, 0, width, height*0.07, fill='#027373')
    drawingspace = myCanvas.create_rectangle(0, height*0.07, width*0.7, height, fill='#F2E7DC')
    leftnav = myCanvas.create_rectangle(width*0.7, height*0.07, width, height, fill='#0D0D0D')
    myCanvas.create_text(width*0.5, 32, text="Binary Search Tree", fill="white", font=('Helvetica 30 bold'))
    myCanvas.create_text(width * 0.85, height * 0.12, text="Operations", fill="white", font=('Helvetica 30 bold'))
    myCanvas.create_text(width * 0.85, height * 0.6, text="Traversals", fill="white", font=('Helvetica 30 bold'))
    # insert new tree
    for i in items:
        tree = deleteNode(tree, int(i))
    draw_tree(tree, width / 3, height * 0.15, width / 7, 100)
    delete_entry.delete(0, 'end')

    return tree


def search_fnc():
    key = int(search_elements.get())
    find_element(tree, width / 3, height * 0.15, width / 7, 100,key)
    search_entry.delete(0, 'end')



def find_element(node, x, y, x_offset, y_offset,value):
    if node is not None:
        myCanvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#037C7F", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'), fill='white')
        root.update()
        time.sleep(0.5)

        if node.data == value:
            # Draw the current node
            myCanvas.create_oval(x-25, y-25, x+25, y+25, fill="green", outline="black")
            myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'), fill='white')
            root.update()
            time.sleep(0.9)
            tk.messagebox.showinfo(title="Element Found", message=None)


        myCanvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#A9D9D0", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'))

        if node.left is not None and value < node.data:
            x_left = x - x_offset
            y_left = y + y_offset
            myCanvas.create_line(x, y + 25, x_left, y_left - 25)
            find_element(node.left, x_left, y_left, x_offset / 2, y_offset + 50,value)

        elif node.right is not None and value > node.data :
            x_right = x + x_offset
            y_right = y + y_offset
            myCanvas.create_line(x, y + 25, x_right, y_right - 25)
            find_element(node.right, x_right, y_right, x_offset / 2, y_offset + 50,value)


Refresh_Sec = 0.5
def preorder_display():
    preorder_fnc(tree, width/3, height*0.15, width/7, 100)

def preorder_fnc(node, x, y, x_offset, y_offset):
    if node is not None:
        # Draw the current node
        myCanvas.create_oval(x-25, y-25, x+25, y+25, fill="#037C7F", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'), fill='white')
        root.update()
        time.sleep(Refresh_Sec)
        myCanvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#A9D9D0", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'))

        # Draw the left child node and the edge between current node and its left child
        if node.left is not None:
            x_left = x - x_offset
            y_left = y + y_offset
            myCanvas.create_line(x, y+25, x_left, y_left-25)
            preorder_fnc(node.left, x_left, y_left, x_offset/2, y_offset+50)

        # Draw the right child node and the edge between current node and its right child
        if node.right is not None:
            x_right = x + x_offset
            y_right = y + y_offset
            myCanvas.create_line(x, y+25, x_right, y_right-25)
            preorder_fnc(node.right, x_right, y_right, x_offset/2, y_offset+50)



def inorder_display():
    inorder_fnc(tree, width/3, height*0.15, width/7, 100)

def inorder_fnc(node, x, y, x_offset, y_offset):
    if node is not None:
        # Draw the left child node and the edge between current node and its left child
        if node.left is not None:
            x_left = x - x_offset
            y_left = y + y_offset
            myCanvas.create_line(x, y + 25, x_left, y_left - 25)
            inorder_fnc(node.left, x_left, y_left, x_offset / 2, y_offset + 50)

        # Draw the current node
        myCanvas.create_oval(x-25, y-25, x+25, y+25, fill="#037C7F", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'), fill='white')
        root.update()
        time.sleep(Refresh_Sec)
        myCanvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#A9D9D0", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'))

        # Draw the right child node and the edge between current node and its right child
        if node.right is not None:
            x_right = x + x_offset
            y_right = y + y_offset
            myCanvas.create_line(x, y+25, x_right, y_right-25)
            inorder_fnc(node.right, x_right, y_right, x_offset/2, y_offset+50)

def postorder_display():
    postorder_fnc(tree, width/3, height*0.15, width/7, 100)

def postorder_fnc(node, x, y, x_offset, y_offset):
    if node is not None:
        # Draw the left child node and the edge between current node and its left child
        if node.left is not None:
            x_left = x - x_offset
            y_left = y + y_offset
            myCanvas.create_line(x, y + 25, x_left, y_left - 25)
            postorder_fnc(node.left, x_left, y_left, x_offset / 2, y_offset + 50)

        # Draw the right child node and the edge between current node and its right child
        if node.right is not None:
            x_right = x + x_offset
            y_right = y + y_offset
            myCanvas.create_line(x, y + 25, x_right, y_right - 25)
            postorder_fnc(node.right, x_right, y_right, x_offset / 2, y_offset + 50)

        # Draw the current node
        myCanvas.create_oval(x-25, y-25, x+25, y+25, fill="#037C7F", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'), fill='white')
        root.update()
        time.sleep(Refresh_Sec)
        myCanvas.create_oval(x - 25, y - 25, x + 25, y + 25, fill="#A9D9D0", outline="black")
        myCanvas.create_text(x, y, text=str(node.data), font=('Helvetica 25 bold'))




# OPERATIONS
myCanvas.create_text(width*0.85, height*0.12, text="Operations", fill="white", font=('Helvetica 30 bold'))
myCanvas.create_text(width*0.85, height*0.6, text="Traversals", fill="white", font=('Helvetica 30 bold'))



# INSERT DIV
insert_elements=tk.StringVar()
insert_entry = tk.Entry(root, textvariable = insert_elements, font=('calibre', 10, 'normal'))
insert_entry.place(x=width*0.72, y=height*0.17, width=int(width*0.26), height=int(height*0.037))
insert_btn = tk.Button(root, text ="INSERT",height= 2, width=10, command = insert_fnc)
insert_btn.place(x=width*0.81, y=height*0.22)

# DELETE DIV
delete_elements=tk.StringVar()
delete_entry = tk.Entry(root, textvariable = delete_elements, font=('calibre', 10, 'normal'))
delete_entry.place(x=width*0.72, y=height*0.3, width=int(width*0.26), height=int(height*0.037))
delete_btn = tk.Button(root, text ="DELETE",height= 2, width=10, command = delete_fnc)
delete_btn.place(x=width*0.81, y=height*0.35)

# SEARCH DIV
search_elements=tk.StringVar()
search_entry = tk.Entry(root, textvariable = search_elements, font=('calibre', 10, 'normal'))
search_entry.place(x=width*0.72, y=height*0.43, width=int(width*0.26), height=int(height*0.037))
search_btn = tk.Button(root, text ="SEARCH",height= 2, width=10, command = search_fnc)
search_btn.place(x=width*0.81, y=height*0.48)


# TRAVERSALS
preorder_btn = tk.Button(root, text ="PREORDER",height= 2, width=10, command = preorder_display)
preorder_btn.place(x=width*0.81, y=height*0.64)
inorder_btn = tk.Button(root, text ="INORDER",height= 2, width=10, command = inorder_display)
inorder_btn.place(x=width*0.81, y=height*0.70)
postorder_btn = tk.Button(root, text ="POSTORDER",height= 2, width=10, command = postorder_display)
postorder_btn.place(x=width*0.81, y=height*0.76)






# add to window and show
myCanvas.pack()
root.mainloop()



"""

10 15 7 3 1 12 20 17 5 21 14 11
"""
