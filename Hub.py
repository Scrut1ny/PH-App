import webbrowser
from tkinter import *


# Defining the button functions

def a():
    url = 'https://www.pornhub.com/'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def b():
    url = 'https://www.pornhub.com/model/mini-diva/'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def c():
    url = 'https://www.pornhub.com/pornstar/mia-khalifa'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def d():
    url = 'https://www.pornhub.com/pornstar/britney-amber'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def e():
    url = 'https://www.pornhub.com/pornstar/kelsi-monroe'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def f():
    url = 'https://www.pornhub.com/pornstar/rose-monroe'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def g():
    root.destroy()


### Main Window ###
root = Tk()
root.title("Pornhub App - v1.5")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry('450x300')

### Program Icon ###
photo = PhotoImage(file="logo.png")
root.iconphoto(False, photo)

### Buttons ###
button1 = Button(text='Incognito', command=a)
button2 = Button(text='Mini Diva', command=b)
button3 = Button(text='Mia Khalifa', command=c)
button4 = Button(text='Britney Amber', command=d)
button5 = Button(text='Kelsi Monroe', command=e)
button6 = Button(text='Rose Monroe', command=f)
button7 = Button(text='Exit', command=g)

### Button Design ###
button1.place(x=8, y=8), button1.config(bg="grey10", fg="orange", font=('bazooka', 15), width=16, height=3)
button2.place(x=8, y=250), button2.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button3.place(x=8, y=200), button3.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button4.place(x=8, y=150), button4.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button5.place(x=8, y=100), button5.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button6.place(x=103, y=100), button6.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button7.place(x=375, y=250), button7.config(bg="grey10", fg="orange", font=('bazooka', 15), width=5, height=1)

### Main loop ###
root.mainloop()
