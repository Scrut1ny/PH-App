import webbrowser
from tkinter import *

### Main Window ###
root = Tk()
root.title("Pornhub App - v2.5")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry('450x301')

### Program Icon ###
photo = PhotoImage(file="logo.png")
root.iconphoto(False, photo)

### Line ###
canvas = Canvas(root, width=450, height=301, background='black', highlightthickness=0)
canvas.grid(row=0, column=0)    #Fuck Cords
canvas.create_line(202, 300, 202, 0, 202, 93, 51000, 0, fill='orange', width=3)


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


def h():
    url = 'https://www.pornhub.com/pornstar/leolulu'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def i():
    url = 'https://www.pornhub.com/model/yinyleon'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def j():
    url = 'https://www.pornhub.com/pornstar/aria-banks'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def k():
    url = 'https://www.pornhub.com/recommended'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def l():
    url = 'https://www.pornhub.com/video?o=ht&cc=us'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def m():
    url = 'https://www.pornhub.com/video?o=mv&cc=us'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


def n():
    url = 'https://www.pornhub.com/video?o=tr'
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
    webbrowser.get(chrome_path).open_new(url)


### Buttons ###
button1 = Button(text='Hub', command=a)
button2 = Button(text='Mini Diva', command=b)
button3 = Button(text='Mia Khalifa', command=c)
button4 = Button(text='Britney Amber', command=d)
button5 = Button(text='Kelsi Monroe', command=e)
button6 = Button(text='Rose Monroe', command=f)
button7 = Button(text='Exit', command=g)
button8 = Button(text='Leolulu', command=h)
button9 = Button(text='yinyleon', command=i)
button10 = Button(text='aria-banks', command=j)
button11 = Button(text='- Recommended -', command=k)
button12 = Button(text='🔥 Hottest 🔥', command=l)
button13 = Button(text='- Most Viewed -', command=m)
button14 = Button(text='- Top Rated -', command=n)

### Button Design ###
button1.place(x=8, y=8), button1.config(bg="grey10", fg="orange", font=('bazooka', 15), width=16, height=3)
button2.place(x=8, y=250), button2.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button3.place(x=8, y=200), button3.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button4.place(x=8, y=150), button4.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button5.place(x=8, y=100), button5.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button6.place(x=104, y=100), button6.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button7.place(x=375, y=250), button7.config(bg="grey10", fg="red", font=('bazooka', 15), width=5, height=1)
button8.place(x=104, y=150), button8.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button9.place(x=104, y=200), button9.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button10.place(x=104, y=250), button10.config(bg="grey10", fg="orange", font=('bazooka', 10), width=10, height=2)
button11.place(x=216, y=53), button11.config(bg="grey10", fg="orange", font=('bazooka', 10), width=12, height=1)
button12.place(x=216, y=13), button12.config(bg="grey10", fg="red", font=('bazooka', 10), width=12, height=1)
button13.place(x=333, y=53), button13.config(bg="grey10", fg="orange", font=('bazooka', 10), width=12, height=1)
button14.place(x=333, y=13), button14.config(bg="grey10", fg="yellow", font=('bazooka', 10), width=12, height=1)

### Main loop ###
root.mainloop()
