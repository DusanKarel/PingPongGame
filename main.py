import tkinter
import random
from Triedy import *

# vyroba platna
width, height, background = 700, 500, "black"
plocha = tkinter.Canvas(width=width, height=height, background=background)
plocha.pack()

doska_1 = Doska(farba="dark red", rozmer=Coords(30, 5),
                speed=15, plocha=plocha, home=Coords(width/2, height - 30),
                platno_width=width, zrychlovanie=1)

plocha.bind_all('<Right>', doska_1.move_right)

plocha.bind_all('<Left>', doska_1.move_left)

plocha.bind_all('<Up>', doska_1.speed_up)

plocha.bind_all('<Down>', doska_1.speed_down)


doska_2 = Doska(farba="dark blue", rozmer=Coords(30, 5),
                speed=15, plocha=plocha, home=Coords(width / 2, 30),
                platno_width=width, zrychlovanie=1)

plocha.bind_all('<d>', doska_2.move_right)

plocha.bind_all('<a>', doska_2.move_left)

plocha.bind_all('<w>', doska_2.speed_up)

plocha.bind_all('<s>', doska_2.speed_down)


lopta = Lopta(priemer=5, farba="white", home=Coords(width/2, height/2),
              plocha=plocha, speed=Coords(random.randint(1, 10), 5))

# Toto je potrebné aby aj keď zbehneš tento program cez PyCharm sa reálne všetko spojené s plochou zobrazilo
plocha.mainloop()
