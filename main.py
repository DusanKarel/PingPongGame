import tkinter
from Triedy import *

# vyroba platna
width, height, background = 700, 500, "black"
plocha = tkinter.Canvas(width=width, height=height, background=background)
plocha.pack()

doska_1 = Doska(farba="dark red", rozmer_x=30, rozmer_y=5,  # vyroba dosky
                speed=15, plocha=plocha, home_x=width / 2, home_y=height - 30, platno_width=width)

plocha.bind_all('<Right>', doska_1.move_right)  # nabidnovat si hybanie ta tlacitko

plocha.bind_all('<Left>', doska_1.move_left)  # nabidnovat si hybanie ta tlacitko

doska_2 = Doska(farba="dark blue", rozmer_x=30, rozmer_y=5,  # vyroba dosky
                speed=15, plocha=plocha, home_x=width / 2, home_y= 30, platno_width=width)

plocha.bind_all('<d>', doska_2.move_right)  # nabidnovat si hybanie ta tlacitko

plocha.bind_all('<a>', doska_2.move_left)  # nabidnovat si hybanie ta tlacitko


# Toto je potrebné aby aj keď zbehneš tento program cez PyCharm sa reálne všetko spojené s plochou zobrazilo
plocha.mainloop()
