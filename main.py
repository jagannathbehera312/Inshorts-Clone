import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce6431517e45c5b04b589c36e5bed6').json()
        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title('Inshorts Clone')
        self.root.configure(background='white')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):

        # clear the screen for the new news item
        self.clear()

        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='white', fg='black', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root,image=photo,bg='white')
        label.pack()




        details = Label(self.root, text=self.data['articles'][index]['description'], bg='white', fg='green', wraplength=350,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root,bg='white')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='Prev',width=13,height=3,bg='#d9936a',fg='#004aad',command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT,padx=(10,0))

        read = Button(frame, text='Read More', width=13, height=3,bg='#d9936a',fg='#004aad',command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT,padx=(10,0))

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next', width=13, height=3,bg='#d9936a',fg='#004aad',command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT,padx=(10,0))

        labela = Label(self.root, text='CREATED BY JAGANNATH BEHERA')
        labela.pack()

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()