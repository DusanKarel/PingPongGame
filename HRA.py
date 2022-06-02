import tkinter


class Doska:

    def __init__(self, farba, rozmer_x, rozmer_y, speed, plocha, home_x, home_y):
        self.rychlost = speed
        self.farba = farba
        self.rozmer_x = rozmer_x
        self.rozmer_y = rozmer_y
        self.home_x = home_x
        self.home_y = home_y
        self.plocha = plocha
        self.objekt = plocha.create_rectangle(home_x - rozmer_x, home_y - rozmer_y,
                                              home_x + rozmer_x, home_y + rozmer_y,
                                              fill=farba)

    def move_right(self, event):
        global width
        self.plocha.move(self.objekt, +self.rychlost, 0)
        if self.plocha.coords(self.objekt)[2] > width:
            self.teleport(True)

    def move_left(self, event):
        global width
        self.plocha.move(self.objekt, -self.rychlost, 0)
        if self.plocha.coords(self.objekt)[0] < 0:
            self.teleport(False)

    def teleport(self, poloha):
        if poloha:
            self.plocha.coords(self.objekt,
                               0, self.home_y - self.rozmer_y,
                               0 + 2 * self.rozmer_x, self.home_y + self.rozmer_y)
        elif not poloha:
            self.plocha.coords(self.objekt,
                               width - 2 * self.rozmer_x, self.home_y - self.rozmer_y,
                               width, self.home_y + self.rozmer_y)
        else:
            print("invalid poloha")


# vyroba platna
width, height, background = 700, 500, "black"
plocha = tkinter.Canvas(width=width, height=height, background=background)
plocha.pack()



doska = Doska(farba="green", rozmer_x=30, rozmer_y=5,  # vyroba dosky
              speed=15, plocha=plocha, home_x=width / 2, home_y=height - 30)

plocha.bind_all('<Right>', doska.move_right)  # nabidnovat si hybanie ta tlacitko

plocha.bind_all('<Left>', doska.move_left)  # nabidnovat si hybanie ta tlacitko


# Toto je potrebné aby aj keď zbehneš tento program cez PyCharm sa reálne všetko spojené s plochou zobrazilo
plocha.mainloop()
