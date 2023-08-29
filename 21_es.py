import play
from random import randint

instr = play.new_text(words='Saca cartas y suma puntos intentando alcanzar 21', x=0, y=250, angle=0, font=None, font_size=35, color='black')
count_jug = play.new_text(words='0', x=-150, y=-240, angle=0, font=None, font_size=25, color='black')
count_cpu = play.new_text(words='0', x=150, y=-240, angle=0, font=None, font_size=25, color='black')
c_jug = 0
c_cpu = 0

mov = play.new_text(words='0', x=-150, y=-275, angle=0, font=None, font_size=25, color='black')
mov_txt = play.new_text(words='Movimientos realizados:', x=-275, y=-275, angle=0, font=None, font_size=25, color='black')
c_mov = 0

bot_jug = play.new_box(color='light green', x=-150, y=-200, width=200, height=40, border_color="grey", border_width=2)
bj_txt = play.new_text(words='Carta Jugador', x=-150, y=-200, angle=0, font=None, font_size=25, color='black')
bot_cpu = play.new_box(color='red', x=150, y=-200, width=200, height=40, border_color="grey", border_width=2)
bcpu_txt = play.new_text(words='VS Computadora', x=150, y=-200, angle=0, font=None, font_size=25, color='black')

final = play.new_text(words='aa', x=0, y=75, angle=0, font=None, font_size=60, color='black')
reset = play.new_box(color='black', x=0, y=0, width=200, height=40, border_color="grey", border_width=2)
reset_txt = play.new_text(words='aa', x=0, y=0, angle=0, font=None, font_size=50, color='white')

cards = []
for i in range(11):
    carta = play.new_image(image=str(i+1)+'.png', x=-150, y=0, angle=0, size=45)
    carta.hide()
    cards.append(carta)
flag=False

def togle_final(stat):
    if stat:
        final.show()
        reset.show()
        reset_txt.show()
        bot_cpu.hide()
        bcpu_txt.hide()
        bot_jug.hide()
        bj_txt.hide()
    else:
        final.hide()
        reset.hide()
        reset_txt.hide()
        bot_cpu.show()
        bcpu_txt.show()
        bot_jug.show()
        bj_txt.show()

@play.when_program_starts
def start():
    final.hide()
    reset.hide()
    reset_txt.hide()

@bot_jug.when_clicked
async def boton_jugador():
    global c_jug, c_mov
    num = randint(1,11)
    cards[num-1].show()
    c_jug += num
    c_mov += 1
    await play.timer(seconds=1)
    cards[num-1].hide()

@bot_cpu.when_clicked
async def boton_cpu():
    global c_cpu, c_mov, flag
    for i in range(11):
        cards[i].x *= -1
    for i in range(c_mov):
        num = randint(1,11)
        cards[num-1].show()
        c_cpu +=num
        await play.timer(seconds=1)
        cards[num-1].hide()
    flag =True

@play.repeat_forever
async def game():
    global flag, c_jug, c_cpu, c_mov
    count_jug.words = str(c_jug)
    count_cpu.words = str(c_cpu)
    mov.words = str(c_mov)
    if c_jug > 21 or (c_jug <= c_cpu and flag):
        await play.timer(seconds=1)
        final.words = 'Pierdes'
        final.color = 'red'
        togle_final(True)
        while not(reset.is_clicked):
            await play.timer(seconds=0.01)
        togle_final(False)
        c_jug = 0
        c_mov = 0
        c_cpu = 0
play.start_program()

#comentario final
#segundo comentario