import webbrowser
from tkinter import *
import threading

# Main Window
root = Tk()
root.title("Pornhub App | v3.3")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry('450x301')

# Program Icon
photo = PhotoImage(file="logo.png")
root.iconphoto(False, photo)

# Line
canvas = Canvas(root, width=450, height=301, background='black', highlightthickness=0)
canvas.grid(row=0, column=0)  # Fuck Cords
canvas.create_line(202, 300, 202, 0, 202, 93, 51000, 0, fill='orange', width=3)

# webbrowser.open_new_tab(url)
# Defining the button functions


def a():
    url = 'https://www.pornhub.com/'
    webbrowser.open_new(url)


def b():
    url = 'https://www.pornhub.com/model/mini-diva/'
    webbrowser.open_new(url)


def c():
    url = 'https://www.pornhub.com/pornstar/mia-khalifa'
    webbrowser.open_new(url)


def d():
    url = 'https://www.pornhub.com/pornstar/britney-amber'
    webbrowser.open_new(url)


def e():
    url = 'https://www.pornhub.com/pornstar/kelsi-monroe'
    webbrowser.open_new(url)


def f():
    url = 'https://www.pornhub.com/pornstar/rose-monroe'
    webbrowser.open_new(url)


def g():
    url = 'https://www.pornhub.com/pornstar/leolulu'
    webbrowser.open_new(url)


def h():
    url = 'https://www.pornhub.com/model/yinyleon'
    webbrowser.open_new(url)


def i():
    url = 'https://www.pornhub.com/pornstar/aria-banks'
    webbrowser.open_new(url)


def j():
    url = 'https://www.pornhub.com/recommended'
    webbrowser.open_new(url)


def k():
    url = 'https://www.pornhub.com/video?o=ht&cc=us'
    webbrowser.open_new(url)


def l():
    url = 'https://www.pornhub.com/video?o=mv&cc=us'
    webbrowser.open_new(url)


def m():
    url = 'https://www.pornhub.com/video?o=tr'
    webbrowser.open_new(url)


# Buttons
button1 = Button(text='Pornhub', command=a)
button2 = Button(text='Mini Diva', command=b)
button3 = Button(text='Mia Khalifa', command=c)
button4 = Button(text='Britney Amber', command=d)
button5 = Button(text='Kelsi Monroe', command=e)
button6 = Button(text='Rose Monroe', command=f)
button7 = Button(text='Leolulu', command=g)
button8 = Button(text='yinyleon', command=h)
button9 = Button(text='aria-banks', command=i)
button10 = Button(text='Recommended', command=j)
button11 = Button(text='🔥 Hottest 🔥', command=k)
button12 = Button(text='Most Viewed', command=l)
button13 = Button(text='Top Rated', command=m)

# Button Design
threading.Thread(button1.place(x=8, y=8),
                 button1.config(bg="grey10", fg="orange", font=('bazooka', 15), width=16, height=3))
threading.Thread(button2.place(x=8, y=250),
                 button2.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button3.place(x=8, y=200),
                 button3.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button4.place(x=8, y=150),
                 button4.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button5.place(x=8, y=100),
                 button5.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button6.place(x=104, y=100),
                 button6.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button7.place(x=104, y=150),
                 button7.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button8.place(x=104, y=200),
                 button8.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button9.place(x=104, y=250),
                 button9.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2))
threading.Thread(button10.place(x=216, y=53),
                 button10.config(bg="grey10", fg="orange", font=('bazooka', 10), width=12, height=1))
threading.Thread(button11.place(x=216, y=13),
                 button11.config(bg="grey10", fg="red", font=('bazooka', 10), width=12, height=1))
threading.Thread(button12.place(x=333, y=53),
                 button12.config(bg="grey10", fg="orange", font=('bazooka', 10), width=12, height=1))
threading.Thread(button13.place(x=333, y=13),
                 button13.config(bg="grey10", fg="yellow", font=('bazooka', 10), width=12, height=1))

# Main loop
root.mainloop()
