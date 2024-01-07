from tkinter import *

window=Tk()
window.title("CyberShop")
window.geometry("1200x800+10+10")
img1 = PhotoImage(file="Fondo.png")
Label(window, image=img1, width=1200, height=800).place(x=0, y=0)


img1A = PhotoImage(file="ELDEN.gif")
img1B = PhotoImage(file="PERSONA.png")
img1C = PhotoImage(file="SOULS3.png")
img1D = PhotoImage(file="SMASH.png")

img2A = PhotoImage(file="DON.png")
img2B = PhotoImage(file="ODISEA.png")
img2C = PhotoImage(file="SOLEDAD.png")
img2D = PhotoImage(file="HARRY.gif")

img3A = PhotoImage(file="UNDER.png")
img3B = PhotoImage(file="ADIDAS.png")
img3C = PhotoImage(file="NIKE.png")
img3D = PhotoImage(file="PUMA.png")

img4A = PhotoImage(file="ROLEX.png")
img4B = PhotoImage(file="OMEGA.png")
img4C = PhotoImage(file="TAG.png")
img4D = PhotoImage(file="BREITLING.png")

img5A = PhotoImage(file="PS4.png")
img5B = PhotoImage(file="SWITCH.png")
img5C = PhotoImage(file="XBOX.png")
img5D = PhotoImage(file="PS5.png")

def purchased():
    NewWindow = Toplevel()
    NewWindow.title("Purcased")
    NewWindow.geometry("400x400")
    Label(NewWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(NewWindow, text="PURCHASED",font=("Freestyle Script",60),fg="red").place(relx=0.5, rely=0.5, anchor='center')
def openNewWindow1A(): 
    newWindow = Toplevel() 
    newWindow.title("EldenRing") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Elden Ring", font=("Freestyle Script",40),fg="red", width=30).pack()
    Label(newWindow, text ="The video game of Elden Ring is the fifth game of dark souls, that differs in the free world program.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="59.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img1A, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow1B(): 
    newWindow = Toplevel() 
    newWindow.title("Persona 5 Royal") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Persona5Royal", font=("Freestyle Script",40),fg="red", width=30).pack()
    Label(newWindow, text ="The video game of Persona 5 Royal is the fifth game of saga related to be the best persona user.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="19.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img1B, width=300, height=160).place(relx=0.3,rely=0.3)

def openNewWindow1C(): 
    newWindow = Toplevel() 
    newWindow.title("Dark Souls 3") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="DarkSouls3", font=("Freestyle Script",40),fg="red", width=30).pack()
    Label(newWindow, text ="It was known as the hardest game existed, if you like adventure and hardest, this is your game.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="14.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img1C, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow1D(): 
    newWindow = Toplevel() 
    newWindow.title("Super Smash Bros") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Super Smash Bros", font=("Freestyle Script",40),fg="red", width=30).pack()
    Label(newWindow, text ="We have the best Nintendo's seller, where you fight online or local with your favorite character.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="49.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img1D, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow2A(): 
    newWindow = Toplevel() 
    newWindow.title("Don Quijote") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Don Quijote", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="Sancho Panza and Don Quijote's adventure as Knigts around the world.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="10$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img2A, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow2B(): 
    newWindow = Toplevel() 
    newWindow.title("La Odisea") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="La Odisea", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="Odiseo and Ulises return to their home in Greek, what will happen to their return?", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="10$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img2B, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow2C(): 
    newWindow = Toplevel() 
    newWindow.title("100 años de Soledad") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="100 años de Soledad", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="Could you live without human interaction? This is what happen to people excluided of society!", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="11$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img2C, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow2D(): 
    newWindow = Toplevel() 
    newWindow.title("Harry Potter") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Harry Potter", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="A new magician is coming to the school, his name is Harry Potter and it seems to be a genius.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="10.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img2D, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow3A(): 
    newWindow = Toplevel() 
    newWindow.title("Under Armor") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Under Armor", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="The last shoes implemented in Under Armour, they are absolutely new with a fine design.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="23.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img3A, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow3B(): 
    newWindow = Toplevel() 
    newWindow.title("Adidas") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Adidas", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text =" Nice black shoes, we can say that has a long resistance from water and are perfect for running.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="27.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img3B, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow3C(): 
    newWindow = Toplevel() 
    newWindow.title("Nike") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Nike", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="Elegant shoes for running, they are gray with some white design perfect to look good while running.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="24.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img3C, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow3D(): 
    newWindow = Toplevel() 
    newWindow.title("Puma") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Puma", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="This are the most infrecuent design in Puma, the orange color does't apper regulary, they are unique!", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="39.99$", font=("Freestyle Script",20),fg="black", width=5).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img3D, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow4A(): 
    newWindow = Toplevel() 
    newWindow.title("Rolex") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Rolex", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="The most famous and expensive brand of watches, it has the best materials of the market.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="5000$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img4A, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow4B(): 
    newWindow = Toplevel() 
    newWindow.title("Omega") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Omega", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="If you like to look elegant with little money, you need one!.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="2499.99$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img4B, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow4C(): 
    newWindow = Toplevel() 
    newWindow.title("TAG Heuer") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="TAG Heuer", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="A different type of watch for elegant situacions accompanied with a tuxedo.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="1499.99$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img4C, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow4D(): 
    newWindow = Toplevel() 
    newWindow.title("Breitling") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Breitling", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="The newest brand of the market, the best value for money with a quite elegant design.", font=("Sans serif fonts",15),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="1000$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img4D, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow5A(): 
    newWindow = Toplevel() 
    newWindow.title("Play Station 4") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Play Station 4", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="The most popular console released 8 years ago, it has the best components of the market for it's price.", font=("Sans serif fonts",12),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="299.99$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img5A, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow5B(): 
    newWindow = Toplevel() 
    newWindow.title("Nintendo Switch") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Nintendo Switch", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="For Nintendo fans, this console can run Pokemon, Smash bros and Zelda, that other consoles can't.", font=("Sans serif fonts",12),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="330$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img5B, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow5C(): 
    newWindow = Toplevel() 
    newWindow.title("Xbox One") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Xbox One", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="This console is the competence of the Play Station 4, but PS4 was best recieved by the fans.", font=("Sans serif fonts",12),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="249.99$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img5C, width=300, height=160).place(relx=0.3,rely=0.3)
    
def openNewWindow5D(): 
    newWindow = Toplevel() 
    newWindow.title("Play Station 5") 
    newWindow.geometry("1200x800+10+10")
    Label(newWindow, image=img1, width=1200, height=800).place(x=0, y=0)
    Label(newWindow, text ="Play Station 5", font=("Freestyle Script",40),fg="red", width=20).pack()
    Label(newWindow, text ="The newest version of PlayStation, it has a white design with an enormous improvement from PS4.", font=("Sans serif fonts",12),fg="black", width=80).place(relx=0.4, rely=0.7, anchor='center')
    Label(newWindow, text ="499.99$", font=("Freestyle Script",20),fg="black", width=10).place(relx=0.85, rely=0.3, anchor='center')
    btn=Button(newWindow, text="Order Here",fg="white",bg="Red",activebackground="green", width=12, command=purchased).place(relx=0.85,rely=0.7,anchor='center')
    Label(newWindow, image=img5D, width=300, height=160).place(relx=0.3,rely=0.3)

def click_button1():

    lbl=Label(window, text="Videogames", font=("Freestyle Script",40),fg="red", width=10)
    lbl.place(relx=0.5, rely=0.1, anchor='center')
    btnA=Button(window, command = openNewWindow1A, image=img1A, width=300, height=160).place(relx=0.3, rely=0.2)
    Label(window, text="Elden Ring", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.45,anchor='center')
    btnB=Button(window, command = openNewWindow1B, image=img1B, width=300, height=160).place(relx=0.7, rely=0.2)
    Label(window, text="Persona 5 Royal", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.45,anchor='center')
    btnC_=Button(window, command = openNewWindow1C, image=img1C, width=300, height=160).place(relx=0.3, rely=0.6)
    Label(window, text="Dark Souls 3", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.85,anchor='center')
    btnD=Button(window, command = openNewWindow1D, image=img1D, width=300, height=160).place(relx=0.7, rely=0.6)
    Label(window, text="Super Smash Bros", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.85,anchor='center')

def click_button2():

    lbl=Label(window, text="Books", font=("Freestyle Script",40),fg="red", width=10)
    lbl.place(relx=0.5, rely=0.1, anchor='center')
    btnA=Button(window, command = openNewWindow2A, image=img2A, width=300, height=160).place(relx=0.3, rely=0.2)
    Label(window, text="Don Quijote", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.45,anchor='center')
    btnB=Button(window, command = openNewWindow2B, image=img2B, width=300, height=160).place(relx=0.7, rely=0.2)
    Label(window, text="La Odisea", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.45,anchor='center')
    btnC_=Button(window, command = openNewWindow2C, image=img2C, width=300, height=160).place(relx=0.3, rely=0.6)
    Label(window, text="100 años de Soledad", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.85,anchor='center')
    btnD=Button(window, command = openNewWindow2D, image=img2D, width=300, height=160).place(relx=0.7, rely=0.6)
    Label(window, text="Harry Potter", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.85,anchor='center')

def click_button3():

    lbl=Label(window, text="Shoes", font=("Freestyle Script",40),fg="red", width=10)
    lbl.place(relx=0.5, rely=0.1, anchor='center')
    btnA=Button(window, command = openNewWindow3A, image=img3A, width=300, height=160).place(relx=0.3, rely=0.2)
    Label(window, text="Under Armour ", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.45,anchor='center')
    btnB=Button(window, command = openNewWindow3B, image=img3B, width=300, height=160).place(relx=0.7, rely=0.2)
    Label(window, text="Adidas", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.45,anchor='center')
    btnC_=Button(window, command = openNewWindow3C, image=img3C, width=300, height=160).place(relx=0.3, rely=0.6)
    Label(window, text="Nike", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.85,anchor='center')
    btnD=Button(window, command = openNewWindow3D, image=img3D, width=300, height=160).place(relx=0.7, rely=0.6)
    Label(window, text="Puma", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.85,anchor='center')

def click_button4():

    lbl=Label(window, text="Watches", font=("Freestyle Script",40),fg="red", width=10)
    lbl.place(relx=0.5, rely=0.1, anchor='center')
    btnA=Button(window, command = openNewWindow4A, image=img4A, width=300, height=160).place(relx=0.3, rely=0.2)
    Label(window, text="Rolex", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.45,anchor='center')
    btnB=Button(window, command = openNewWindow4B, image=img4B, width=300, height=160).place(relx=0.7, rely=0.2)
    Label(window, text="Omega", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.45,anchor='center')
    btnC_=Button(window, command = openNewWindow4C, image=img4C, width=300, height=160).place(relx=0.3, rely=0.6)
    Label(window, text="TAG Heuer", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.85,anchor='center')
    btnD=Button(window, command = openNewWindow4D, image=img4D, width=300, height=160).place(relx=0.7, rely=0.6)
    Label(window, text="Breitling", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.85,anchor='center')
    
def click_button5():

    lbl=Label(window, text="Consoles", font=("Freestyle Script",40),fg="red", width=10)
    lbl.place(relx=0.5, rely=0.1, anchor='center')
    btnA=Button(window, command = openNewWindow5A, image=img5A, width=300, height=160).place(relx=0.3, rely=0.2)
    Label(window, text="Play Station 4", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.45,anchor='center')
    btnB=Button(window, command = openNewWindow5B, image=img5B, width=300, height=160).place(relx=0.7, rely=0.2)
    Label(window, text="Nintendo Switch", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.45,anchor='center')
    btnC_=Button(window, command = openNewWindow5C, image=img5C, width=300, height=160).place(relx=0.3, rely=0.6)
    Label(window, text="Xbox One", font=("Freestyle Script",20), width=20).place(relx=0.42,rely=0.85,anchor='center')
    btnD=Button(window, command = openNewWindow5D, image=img5D, width=300, height=160).place(relx=0.7, rely=0.6)
    Label(window, text="Play Station 5", font=("Freestyle Script",20), width=20).place(relx=0.82,rely=0.85,anchor='center')

lbl=Label(window, text="CyberShop", font=("Freestyle Script",40),fg="red")
lbl.place(relx=0.5, rely=0.1, anchor='center')


btn1=Button(window, text="Videogames",fg="white",bg="black",activebackground="orange", width=12, command=click_button1)
btn1.place(relx=0.1, rely=0.4, anchor='center')

btn2=Button(window, text="Books",fg="white",bg="black",activebackground="orange",width=12, command=click_button2)
btn2.place(relx=0.1, rely=0.435, anchor='center')

btn3=Button(window, text="Shoes",fg="white",bg="black",activebackground="orange",width=12, command=click_button3)
btn3.place(relx=0.1, rely=0.47, anchor='center')

btn4=Button(window, text="Watches",fg="white",bg="black",activebackground="orange",width=12, command=click_button4)
btn4.place(relx=0.1, rely=0.505, anchor='center')

btn5=Button(window, text="Consoles",fg="white",bg="black",activebackground="orange",width=12, command=click_button5)
btn5.place(relx=0.1, rely=0.54, anchor='center')

window.mainloop()
#Fernando Terrazas Llanos 5/11/22-15/11/22