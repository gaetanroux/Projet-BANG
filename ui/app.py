from tkinter import *
import webbrowser

def open_graven_channel():
    webbrowser.open_new("https://fr.wikipedia.org/wiki/Bang!_(jeu_de_cartes)")

#Creer une premiere fenetre
window = Tk()

#personnaliser cette fenetre
window.title("BANG!")
window.geometry("720x480")
window.minsize(480, 360)
<<<<<<< HEAD
window.iconbitmap("C:/Users/gaeta/Desktop/Algo jeux de societé/BANG/BANG!/ui/logo.ico")
window.config(background='#41B77F')
=======
window.iconbitmap("c:/Users/Paul/Desktop/YDAYS/Algo&Jeu de société/BANG!/ui/logo.ico")
window.config(background='#F09316')

#creer la frame
frame = Frame(window, bg='#F09316')
>>>>>>> 3517e959e9775f25df27fda64192d7ad087cbedd

#ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur le jeu BANG !", font=("Western Bang Bang", 40), bg='#F09316', fg='white')
label_title.pack()

#ajouter un second texte
label_subtitle = Label(frame, text="Créé par Gaëtan Roux & Paul Vigneron", font=("Western Bang Bang", 25), bg='#F09316', fg='white')
label_subtitle.pack()

#ajouter un premier bouton
rules_button = Button(frame, text="Voir les règles du jeu", font=("Western Bang Bang", 20), bg='white', fg='#F09316', command=open_graven_channel)
rules_button.pack(pady=25, fill=X)

#création image
width = 300
height = 300
image = PhotoImage(file="C:/Users/Paul/Desktop/YDAYS/Algo&Jeu de société/BANG!/ui/photo.jpg")
canvas = Canvas(window, width=width, height=height, bg='F09316')
canvas.create_image(width/2, height/2, image=image)
#canvas.pack(expand=YES)

#ajouter
frame.pack(expand=YES)

#afficher
window.mainloop()