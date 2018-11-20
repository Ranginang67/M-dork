#!/usr/bin/python2

"""
dorking with mdork,
MESSAGE: Mdork gui available for linux only
pessan: mdork versi gui hanya berjalan pada linux
sorry if this tool is not perfect, i just learned to be a developer :)
=================================================
Developer: Ms.ambari
Date: 2018-11-20
YouTube: Ms.ambari
Github: https://github.com/Ranginang67
"""

try:
    from Tkinter import *
    import tkMessageBox
    import mechanize
    import os.path
    import sys
    import re
except ImportError as eer:
    exit(eer)

class mdork:

    def __init__(self,**kwargs):
        self.root = kwargs['jendela']
        self.manuk = Menu(self.root)
        self.br = mechanize.Browser()
        self.__w = 640
        self.__h = 630
        self.__ewe = self.root.winfo_screenwidth()
        self.__eha = self.root.winfo_screenheight()
        self.__x = (self.__ewe/2) - (self.__w/2)
        self.__y = (self.__eha/2) - (self.__h/2)

        self.root.title('Mdork')
        self.root.geometry("%dx%d+%d+%d" % (
            self.__w, self.__h,
            self.__x, self.__y
        ))
        
        self.dorkan = Label(self.root,text="Dork")
        cop = Label(
            self.root,text="Copyright2018 - Ms.ambari",
            font=('Courier',9)
            )
        self.inputan_dork = Entry(self.root,width=50,selectbackground="#007CFF")
        self.inputan_dork.insert(END,"your dork here")
        self.bata = Button(self.root,text="start",command=self.dork)

        cop.grid(row=2,
            column=1,
            padx=1,
            columnspan=80)

        self.dorkan.grid(
            row=0,column=0,pady=20
        )
        self.inputan_dork.grid(
            row=0,column=1
        )
        self.bata.grid(
            row=0,column=2
        )

        self.kolom = Text(
            self.root,width=70,height=36,
            selectbackground="#007CFF"
        )
        self.kolom.grid(
            row=1,column=0,
            columnspan=3,
            pady=10,ipady=10
        )
        
        self.men = Menu(self.manuk,tearoff=0)
        self.men.add_command(label="exit",command=self.root.destroy)

        self.men.add_separator()
        self.manuk.add_cascade(label="menu",menu=self.men)

        self.root.config(menu=self.manuk)
        mainloop()
    
    def dork(self):
        i = []
        cout = 0
        filewrite = open('result.txt','a')
        i.append(self.inputan_dork.get())
        if '' in i:
            tkMessageBox.showerror('error','no input dork')
        else:
            try:
                while True:
                    kumpul_lo_semua = "https://www.bing.com/search?q={}&first={}&FORM=PORE".format(i[0],cout)
                    cout += 9
                    self.br.set_handle_robots(False)
                    nisa = self.br.open(kumpul_lo_semua)
                    self.br._factory.is_html = True
                    nisa = nisa.read()
                    hasil = re.findall(r'<li class="b_algo"><h2><a href="(.*?)"',nisa)
                    for kontol in hasil:
                        sm = "%s\n"%kontol
                        filewrite.write(sm)
                        self.kolom.insert(END,sm)

                    if cout is 54:
                        filewrite.close()
                        break

            except:
                tkMessageBox.showerror('error','check your connection')
                exit()

j = Tk()
mdork(jendela=j)
