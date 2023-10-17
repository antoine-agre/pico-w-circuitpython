import time
import board
import pwmio

buzzer = pwmio.PWMOut(board.GP26, variable_frequency=True)

noire = 210
temps_note = 60 / noire


do3,re3,mi3,fa3,sol3,la3,si3 = 231.63,293.66,329.63,349.23,392.0,440,493.88
do4,re4,mi4,fa4,sol4,la4,si4 = 523.25,554.37,659.26,698.46,783.99,880,987.77

acdll_notes = [do4,do4,do4,re4,mi4,re4,do4,mi4,re4,re4,do4]
acdll_durees = [1,1,1,1,2,2,1,1,1,1,3]
acdll_bpm = 210

def jouer_son(frequence, duree):
    buzzer.frequency = int(frequence)
    buzzer.duty_cycle = 65535 // 2
    time.sleep(duree)
    buzzer.duty_cycle = 0

def note(frequence, duree):
    jouer_son(frequence, duree * temps_note)
    time.sleep(0.2 * duree * temps_note)

# for i in range(len(acdll_notes)):
# #     jouer_son(acdll_notes[i],acdll_durees[i]*temps_note)
# #     time.sleep(0.2 * acdll_durees[i] * temps_note)
#     note(acdll_notes[i], acdll_durees[i])

hb_notes = [
    re3, re3, mi3, re3, sol3, fa3,
    re3, re3, mi3, re3, la3, sol3,
    re3, re3, la4, si3, sol3, fa3, mi3,
    do4, do4, si3, sol3, la3, sol3
]
hb_durees = [
    0.5, 0.5, 1, 1, 1, 2,
    0.5, 0.5, 1, 1, 1, 2,
    0.5, 0.5, 1, 1, 1, 1, 2,
    0.5, 0.5, 1, 1, 1, 2
]

for i in range(len(hb_notes)):
    note(hb_notes[i], hb_durees[i])