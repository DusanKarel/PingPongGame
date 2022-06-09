class Coords:

    def __init__(self, suradnica_x, suradnica_y):
        self.x = suradnica_x
        self.y = suradnica_y


class Doska:

    def __init__(self, farba, rozmer: Coords, speed, plocha, home: Coords,
                 platno_width, zrychlovanie):
        self.zrychlovanie = zrychlovanie
        self.platno_width = platno_width
        self.rychlost = speed
        self.farba = farba
        self.rozmer = rozmer
        self.home = home
        self.plocha = plocha
        self.objekt = plocha.create_rectangle(home.x - rozmer.x, home.y - rozmer.y,
                                              home.x + rozmer.x, home.y + rozmer.y,
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
                               0, self.home.y - self.rozmer.y,
                               0 + 2 * self.rozmer.x, self.home.y + self.rozmer.y)
        elif not poloha:
            self.plocha.coords(self.objekt,
                               self.platno_width - 2 * self.rozmer.x, self.home.y - self.rozmer.y,
                               self.platno_width, self.home.y + self.rozmer.y)
        else:
            print("invalid poloha")


class Lopta:

    objekt = 0

    def __init__(self, priemer, farba, home: Coords, plocha, speed: Coords):
        self.priemer = priemer
        self.farba = farba
        self.home = home
        self.plocha = plocha
        self.speed = speed
        self.draw()

    def draw(self):
        self.objekt = self.plocha.create_oval(self.home.x - self.priemer, self.home.y - self.priemer,
                                              self.home.x + self.priemer, self.home.y + self.priemer,
                                              fill=self.farba)



