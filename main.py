from menu import start
from game import game
from pvp import pvp
from editor import red
from levels_selection import write_level, lvl
from game_result import men
from pvp_result import pvp_end


stand = 1
mp1, mp2, level, score, win, winner = None, None, None, None, None, None
while stand != 0:
    if stand == 1:
        stand = start()
    elif stand == 2:
        stand, score, level, win = game(mp1, mp2, level)
    elif stand == 3:
        stand, winner = pvp()
    elif stand == 4:
        stand, m1, m2 = red()
        write_level(m1, m2)
    elif stand == 5:
        stand, mp1, mp2, level = lvl()
    elif stand == 6:
        stand, mp1, mp2 = men(score, level, win)
    elif stand == 7:
        stand = pvp_end(winner)
