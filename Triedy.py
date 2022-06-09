class Doska:

    def __init__(self, farba, rozmer_x, rozmer_y, speed, plocha, home_x,
                 home_y,platno_width, zrychlovanie):
        self.zrychlovanie = zrychlovanie
        self.platno_width = platno_width
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

    def speed_up(self, event):
        self.rychlost += self.zrychlovanie
        print(self.rychlost)

    def speed_down(self, event):
        self.rychlost -= self.zrychlovanie
        if self.rychlost == 0:
            self.rychlost += 1
        print(self.rychlost)

    def move_right(self, event):
        self.plocha.move(self.objekt, +self.rychlost, 0)
        if self.plocha.coords(self.objekt)[2] > self.platno_width:
            self.teleport(True)

    def move_left(self, event):
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
                               self.platno_width - 2 * self.rozmer_x, self.home_y - self.rozmer_y,
                               self.platno_width, self.home_y + self.rozmer_y)
        else:
            print("invalid poloha")

class Lopta:

    def __init__(self, priemer, farba, home_x, home_y, plocha):
        self.priemer = priemer
        self.farba = farba
        self.home_x = home_x
        self.home_y = home_y
        self.plocha = plocha
        self.objekt = plocha.create_oval(home_x - priemer, home_y - priemer,
                                         home_x + priemer, home_y + priemer,
                                         fill=farba)

    def draw(self):
        self.objekt = self.plocha.create_oval(self.home_x - self.priemer, self.home_y - self.priemer,
                                              self.home_x + self.priemer, self.home_y + self.priemer,
                                              fill=self.farba)

