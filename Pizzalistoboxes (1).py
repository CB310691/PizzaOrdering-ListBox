from tkinter import *
#Choices indicate what selection you've made via mouse cursour.
def toppingsChoice():
    widget = event.widget
    selection=widget.curselection()
    Chosen_Widget1= widget.get(selection[1])
    print (Chosen_Widget1)

def baseChoice():
    widget = event.widget
    selection=widget.curselection()
    Chosen_Widget2 = widget.get(selection[0])
    print (Chosen_Widget2)

def sizeChoice():
    widget = event.widget
    selection=widget.curselection()
    Chosen_Widget3= widget.get(selection[0])
    print (Chosen_Widget3)

def drinkChoice():
    widget = event.widget
    selection=widget.curselection()
    Chosen_Widget4= widget.get(selection[0])
    print (Chosen_Widget4)

def sidesChoice():
    widget = event.widget
    selection=widget.curselection()
    Chosen_Widget5= widget.get(selection[0])
    print (Chosen_Widget5)

#a list of toppings
toppings = ['Pepperoni','Onion','Red Pepper','Green Pepper','Hot sauce','Ham','Pineapple']

base = ['Thin crust', ' Deep crust ', 'Gluten free pizza base']

size = ['Small(4 slices)','Medium(8 Slices)', 'Large(12 slices)','Super sized(18 slices)']

drink = ['Pepsi','Coke','Sprite','7UP','Lucozade','Dr Pepper','Cream soda','Tango Apple','Tango Orange']

sides = ['Potato Wedges','Garlic bread','Cheesy Garlic Bread','Fries','Chicken Wings']

window = Tk()

label1 = Label(window, text="ORDER YOUR PIZZA")
label2 = Label(window, text="Your order =")
#create listboxes
baseLB = Listbox(window)
toppingLB = Listbox(window)
sizeLB = Listbox(window)
drinkLB = Listbox(window)
sidesLB = Listbox(window)


#how you populate a list box
for topping in toppings:
    toppingLB.insert(END, topping)

for base in base:
    baseLB.insert(END, base)

for size in size:
    sizeLB.insert(END, size)

for drink in drink:
    drinkLB.insert(END, drink)

for side in sides:
    sidesLB.insert(END, side)

toppingLB.bind('<<ListboxSelect>>', toppingsChoice)

baseLB.bind('<<ListboxSelect>>',baseChoice)

sizeLB.bind('<<ListboxSelect>>', sizeChoice)

drinkLB.bind('<<ListboxSelect>>', drinkChoice)

sidesLB.bind('<<ListboxSelect>>', sidesChoice)

label1.grid(row=0, column=0, columnspan=5)
label2.grid(row=2, column=0, columnspan=5)
baseLB.grid(row=1, column=0)
toppingLB.grid(row=1, column=1)
sizeLB.grid(row=1, column=2)
drinkLB.grid(row=1, column=3)
sidesLB.grid(row=1, column=4) 
