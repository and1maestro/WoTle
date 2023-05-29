import pygame
import random
import sys
import socket
from pygame.constants import QUIT, K_BACKSPACE, K_r, K_m
from difflib import SequenceMatcher
from pygame import mixer

name = socket.gethostname()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)

class Tank:
        def __init__(self, name, typeof, nation, damage, penetration, hp, speed):
            self.name = name
            self.typeof = typeof
            self.nation = nation
            self.damage = int(damage)
            self.penetration = int(penetration)
            self.hp = int(hp)
            self.speed = int(speed)
        def compare(self, other):
            name = other.name
            if self.typeof == other.typeof:
                typeof = other.typeof + "+"
            else:
                typeof = other.typeof
            if self.nation == other.nation:
                nation = other.nation + "+"
            else:
                nation = other.nation
            if self.damage == other.damage:
                damage = str(other.damage) + "+"
            if self.damage > other.damage:
                if self.damage - other.damage <= self.damage * 0.1:
                    damage = str(other.damage) + "↑-"
                else:
                    damage = str(other.damage) + "↑"
            if self.damage < other.damage:
                if other.damage - self.damage <= self.damage * 0.1:
                    damage = str(other.damage) + "↓-"
                else:
                    damage = str(other.damage) + "↓"
            if self.penetration == other.penetration:
                penetration = str(other.penetration) + "+"
            if self.penetration > other.penetration:
                if self.penetration - other.penetration <= self.penetration * 0.1:
                    penetration = str(other.penetration) + "↑-"
                else:
                    penetration = str(other.penetration) + "↑"
            if self.penetration < other.penetration:
                if other.penetration - self.penetration <= self.penetration * 0.1:
                    penetration = str(other.penetration) + "↓-"
                else:
                    penetration = str(other.penetration) + "↓"
            if self.hp == other.hp:
                hp = str(other.hp) + "+"
            if self.hp > other.hp:
                if self.hp - other.hp <= self.hp * 0.1:
                    hp = str(other.hp) + "↑-"
                else:
                    hp = str(other.hp) + "↑"
            if self.hp < other.hp:
                if other.hp - self.hp <= self.hp * 0.1:
                    hp = str(other.hp) + "↓-"
                else:
                    hp = str(other.hp) + "↓"
            if self.speed == other.speed:
                speed = str(other.speed) + "+"
            if self.speed > other.speed:
                if self.speed - other.speed <= self.speed * 0.1:
                    speed = str(other.speed) + "↑-"
                else:
                    speed = str(other.speed) + "↑"
            if self.speed < other.speed:
                if other.speed - self.speed <= self.speed * 0.1:
                    speed = str(other.speed) + "↓-"
                else:
                    speed = str(other.speed) + "↓"
            
            attributes = [name, typeof, nation, damage, penetration, hp, speed]
            return attributes

player_dict = {
        "121": "121.png",
        "121B": "121b.png",
        "113": "113.png",
        "116-F3": "116-f3.png",
        "BZ-75": "bz75.png",
        "WZ-111 model 5A": "wz111.png",
        "114 SP2": "114.png",
        "WZ-113G FT": "wz113.png",
        "WZ-132-1": "wz132.png",

        "TVP T 50/51": "tvp.png",
        "Vz. 55": "vz55.png",

        "AMX 30 B": "amx30b.png",
        "Bat.-Chatillon 25 t": "bc25t.png",
        "AMX 50 B": "amx50b.png",
        "AMX M4 mle. 54": "amxm4.png",
        "AMX 50 Foch B": "fochb.png",
        "AMX 50 Foch 155": "foch155.png",
        "AMX 13 105": "amx13105.png",
        "Panhard EBR 105": "ebr.png",
        "Bat.-Chatillon 155 58": "bc15558.png",

        "E 50 M": "e50m.png",
        "Leopard 1": "leopard.png",
        "E 100": "e100.png",
        "Maus": "maus.png",
        "Pz.Kpfw. VII": "pz7.png",
        "VK 72.01 K": "vk7201k.png",
        "Grille 15": "grille.png",
        "Jagdpanzer E 100": "jgpze100.png",
        "G.W. E 100": "gwe100.png",
        "Rheinmetall Panzerwagen": "rhm.png",

        "Carro 45 t": "carro.png",
        "Lion": "lion.png",
        "Progetto 65": "progetto.png",
        "Rinoceronte": "rino.png",
        "Minotauro": "minotauro.png",

        "STB-1": "stb1.png",
        "Type 5 Heavy": "type5.png",
        "Ho-Ri 3": "hori3.png",

        "CS-63": "cs63.png",
        "60TP Lewandowskiego": "60tp.png",

        "UDES 15/16": "udes.png",
        "Kranvagn": "kranvagn.png",
        "Strv 103B": "strv.png",

        "Centurion Action X": "cent.png",
        "FV215b": "fv215b.png",
        "Super Conqueror": "conq.png",
        "T95/FV4201 Chieftain": "chief.png",
        "FV215b 183": "fv215b183.png",
        "FV217 Badger": "badger.png",
        "FV4005 Stage II": "fv4005.png",
        "Manticore": "manticore.png",
        "Conqueror Gun Carriage": "conq_gc.png",

        "M48A5 Patton": "m48a5.png",
        "M60": "m60.png",
        "T95E6": "t95e6.png",
        "M-V-Y": "mvy.png",
        "T110E5": "t110e5.png",
        "T57 Heavy": "t57.png",
        "T110E3": "t110e3.png",
        "T110E4": "t110e4.png",
        "XM551 Sheridan": "sheridan.png",
        "T92 HMC": "t92.png",

        "K-91": "k91.png",
        "Object 430U": "430.png",
        "Object 140": "140.png",
        "Object 907": "907.png",
        "T-22 Medium": "t22.png",
        "T-62A": "t62.png",
        "IS-4": "is4.png",
        "IS-7": "is7.png",
        "Object 260": "o260.png",
        "Object 277": "o277.png",
        "Object 279 Early": "o279.png",
        "Object 705A": "o705.png",
        "Object 780": "o780.png",
        "ST-II": "st2.png",
        "Object 268": "268.png",
        "Object 268/4": "2684.png",
        "Object 268/5": "2685.png",
        "T-100 LT": "t100.png",
        "Object 261": "261.png"
    }

def get_image(tank):
        return player_dict[tank.name]

t121 = Tank("121", "Medium", "China", "440", "262", "2050", "56")
t121b = Tank("121B", "Medium", "China", "390", "261", "1950", "55")
t113 = Tank("113", "Heavy", "China", "440", "249", "2300", "50")
t116_f3 = Tank("116-F3", "Heavy", "China", "530", "266", "2100", "35")
bz75 = Tank("BZ-75", "Heavy", "China", "650", "258", "2500", "45")
wz111 = Tank("WZ-111 model 5A", "Heavy", "China", "490", "250", "2200", "50")
t114 = Tank("114 SP2", "Destroyer", "China", "650", "273", "2000", "45")
wz113 = Tank("WZ-113G FT", "Destroyer", "China", "750", "290", "2100", "38")
wz132 = Tank("WZ-132-1", "Light", "China", "390", "246", "1500", "65")

tvp = Tank("TVP T 50/51", "Medium", "Czech", "320", "248", "1800", "60")
vz55 = Tank("Vz. 55", "Heavy", "Czech", "490", "260", "2100", "50")

amx30b = Tank("AMX 30 B", "Medium", "France", "390", "248", "1900", "65")
bc25t = Tank("Bat.-Chatillon 25 t", "Medium", "France", "390", "259", "1800", "65")
amx50b = Tank("AMX 50 B", "Heavy", "France", "400", "257", "2100", "65")
amxm4 = Tank("AMX M4 mle. 54", "Heavy", "France", "560", "250", "2200", "35")
fochb = Tank("AMX 50 Foch B", "Destroyer", "France", "400", "257", "1850", "50")
foch155 = Tank("AMX 50 Foch 155", "Destroyer", "France", "750", "293", "1850", "50")
amx13105 = Tank("AMX 13 105", "Light", "France", "390", "234", "1400", "68")
ebr = Tank("Panhard EBR 105", "Light", "France", "390", "190", "1300", "91")
bc15558 = Tank("Bat.-Chatillon 155 58", "SPG", "France", "680", "48", "490", "62")

e50m = Tank("E 50 M", "Medium", "Germany", "390", "270", "2050", "60")
leopard = Tank("Leopard 1", "Medium", "Germany", "420", "278", "1850", "70")
e100 = Tank("E 100", "Heavy", "Germany", "750", "246", "2700", "30")
maus = Tank("Maus", "Heavy", "Germany", "490", "246", "3000", "20")
pz7 = Tank("Pz.Kpfw. VII", "Heavy", "Germany", "560", "258", "2500", "33")
vk7201k = Tank("VK 72.01 K", "Heavy", "Germany", "750", "246", "2500", "33")
grille = Tank("Grille 15", "Destroyer", "Germany", "750", "279", "1800", "60")
jdpze100 = Tank("Jagdpanzer E 100", "Destroyer", "Germany", "1050", "299", "2200", "30")
rhm = Tank("Rheinmetall Panzerwagen", "Light", "Germany", "320", "242", "1600", "75")
gwe100 = Tank("G.W. E 100", "SPG", "Germany", "900", "53", "550", "40")

carro = Tank("Carro 45 t", "Medium", "Italy", "400", "248", "1900", "55")
lion = Tank("Lion", "Medium", "Italy", "420", "258", "1850", "60")
progetto = Tank("Progetto 65", "Medium", "Italy", "360", "268", "1900", "65")
rino = Tank("Rinoceronte", "Heavy", "Italy", "490", "268", "2000", "40")
minotauro = Tank("Minotauro", "Destroyer", "Italy", "530", "265", "2100", "30")

stb1 = Tank("STB-1", "Medium", "Japan", "360", "258", "2000", "50")
type5 = Tank("Type 5 Heavy", "Heavy", "Japan", "600", "257", "2900", "25")
hori3 = Tank("Ho-Ri 3", "Destroyer", "Japan", "700", "305", "2000", "35")

cs63 = Tank("CS-63", "Medium", "Poland", "390", "258", "2000", "70")
t60tp = Tank("60TP Lewandowskiego", "Heavy", "Poland", "750", "250", "2600", "35")

udes = Tank("UDES 15/16", "Medium", "Sweden", "440", "254", "1950", "50")
kranvagn = Tank("Kranvagn", "Heavy", "Sweden", "440", "252", "2000", "45")
strv = Tank("Strv 103B", "Destroyer", "Sweden", "390", "308", "1800", "50")

cent = Tank("Centurion Action X", "Medium", "UK", "390", "268", "1950", "55")
fv215b = Tank("FV215b", "Heavy", "UK", "400", "259", "2500", "34")
conq = Tank("Super Conqueror", "Heavy", "UK", "400", "259", "2400", "34")
chief = Tank("T95/FV4201 Chieftain", "Heavy", "UK", "440", "270", "2200", "46")
fv215b183 = Tank("FV215b 183", "Destroyer", "UK", "1150", "310", "2000", "34")
badger = Tank("FV217 Badger",  "Destroyer", "UK", "480", "272", "2100", "30")
fv4005 = Tank("FV4005 Stage II", "Destroyer", "UK", "1150", "310", "1850", "32")
manticore = Tank("Manticore", "Light", "UK", "390", "248", "1400", "68")
conq_gc = Tank("Conqueror Gun Carriage", "SPG", "UK", "1000", "59", "530", "34")

m48 = Tank("M48A5 Patton", "Medium", "USA", "390", "268", "2000", "45")
m60 = Tank("M60", "Medium", "USA", "390", "268", "2000", "60")
t95e6 = Tank("T95E6", "Medium", "USA", "400", "258", "2150", "56")
mvy = Tank("M-V-Y", "Heavy", "USA", "440", "252", "2200", "40")
t110e5 = Tank("T110E5", "Heavy", "USA", "400", "258", "2200", "37")
t57 = Tank("T57 Heavy", "Heavy", "USA", "400", "258", "2250", "35")
t110e3 = Tank("T110E3", "Destroyer", "USA", "750", "295", "1950", "24")
t110e4 = Tank("T110E4", "Destroyer", "USA", "750", "295", "2000", "35")
sheridan = Tank("XM551 Sheridan", "Light", "USA", "910", "76", "1600", "65")
t92 = Tank("T92 HMC", "SPG", "USA", "1100", "60", "500", "32")

k91 = Tank("K-91", "Medium", "USSR", "320", "276", "1950", "55")
o430 = Tank("Object 430U", "Medium", "USSR", "440", "252", "2000", "50")
o140 = Tank("Object 140", "Medium", "USSR", "320", "264", "1950", "55")
o907 = Tank("Object 907", "Medium", "USSR", "320", "264", "2000", "55")
t22 = Tank("T-22 Medium", "Medium", "USSR", "320", "264", "1900", "55")
t62 = Tank("T-62A", "Medium", "USSR", "320", "264", "1950", "50")
is4 = Tank("IS-4", "Heavy", "USSR", "440", "258", "2500", "43")
is7 = Tank("IS-7", "Heavy", "USSR", "490", "250", "2400", "60")
o260 = Tank("Object 260", "Heavy", "USSR", "440", "260", "2100", "60")
o277 = Tank("Object 277", "Heavy", "USSR", "490", "265", "2200", "55")
o279 = Tank("Object 279 Early", "Heavy", "USSR", "440", "260", "2400", "40")
o705 = Tank("Object 705A", "Heavy", "USSR", "650", "256", "2450", "40")
o780 = Tank("Object 780", "Heavy", "USSR", "530", "267", "2200", "45")
st2 = Tank("ST-II", "Heavy", "USSR", "440", "258", "2500", "40")
o268 = Tank("Object 268", "Destroyer", "USSR", "750", "303", "1950", "48")
o2684 = Tank("Object 268/4", "Destroyer", "USSR", "650", "293", "2000", "50")
o2685 = Tank("Object 268/5", "Destroyer", "USSR", "750", "303", "2000", "48")
t100 = Tank("T-100 LT", "Light", "USSR", "300", "230", "1500", "72")
o261 = Tank("Object 261", "SPG", "USSR", "800", "45", "510", "50")

tanks = [t121, t121b, t113, t116_f3, bz75, wz111, t114, wz113, wz132,   tvp, vz55,   amx30b, bc25t, amx50b, amxm4, fochb, foch155, amx13105, ebr, bc15558,           
         e50m, leopard, e100, maus, pz7, vk7201k, grille, jdpze100, rhm, gwe100,   carro, lion, progetto, rino, minotauro,   cs63, t60tp, udes, kranvagn, strv,  
         cent, fv215b, conq, chief, fv215b183, badger, fv4005, manticore, conq_gc,   m48, m60, t95e6, mvy, t110e5, t57, t110e3, t110e4, sheridan, t92,
         k91, o430, o140, o907, t22, t62, is4, is7, o260, o277, o279, o705, st2, o268, o2684, o2685, t100, o261,   stb1, type5, hori3]

pygame.init()

HEIGHT = 1080
WIDTH = 1920
FPS = pygame.time.Clock()

pygame.init()

HEIGHT = 1080
WIDTH = 1920
FPS = pygame.time.Clock()

mixer.music.load("data/music.mp3")
mixer.music.play(-1)

def main():

    HEIGHT = 1080
    WIDTH = 1920
    FPS = pygame.time.Clock()

    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    base_font = pygame.font.SysFont("swiss721black", 30)
    base_font_medium = pygame.font.SysFont("swiss721black", 25)
    base_font_small = pygame.font.SysFont("swiss721black", 20)
    base_font_info = pygame.font.SysFont("timesnewroman", 20)
    base_font_table = pygame.font.SysFont("timesnewroman", 22)
    text = ""
    hint = ""

    color_light = (200,170,150)
    color_dark = (170,140,120)
    color_out = (70,55,45)
    color_out2 = (100,85,75)
    color_green = (80,255,5)
    color_yellow = (255,200,15)

    c = 0

    credits = base_font_small.render("inst: @and1maestro", True, color_dark)
    credits_bg = base_font_small.render("inst: @and1maestro", True, (0,0,0))

    namet1 = base_font_small.render(text, True, (255,255,255))
    damaget1 = base_font_small.render(text, True, (255,255,255))
    penetrationt1 = base_font_small.render(text, True, (255,255,255))
    hpt1 = base_font_small.render(text, True, (255,255,255))
    speedt1 = base_font_small.render(text, True, (255,255,255))

    namet2 = base_font_small.render(text, True, (255,255,255))
    damaget2 = base_font_small.render(text, True, (255,255,255))
    penetrationt2 = base_font_small.render(text, True, (255,255,255))
    hpt2 = base_font_small.render(text, True, (255,255,255))
    speedt2 = base_font_small.render(text, True, (255,255,255))

    namet3 = base_font_small.render(text, True, (255,255,255))
    damaget3 = base_font_small.render(text, True, (255,255,255))
    penetrationt3 = base_font_small.render(text, True, (255,255,255))
    hpt3 = base_font_small.render(text, True, (255,255,255))
    speedt3 = base_font_small.render(text, True, (255,255,255))

    namet4 = base_font_small.render(text, True, (255,255,255))
    damaget4 = base_font_small.render(text, True, (255,255,255))
    penetrationt4 = base_font_small.render(text, True, (255,255,255))
    hpt4 = base_font_small.render(text, True, (255,255,255))
    speedt4 = base_font_small.render(text, True, (255,255,255))

    namet5 = base_font_small.render(text, True, (255,255,255))
    damaget5 = base_font_small.render(text, True, (255,255,255))
    penetrationt5 = base_font_small.render(text, True, (255,255,255))
    hpt5 = base_font_small.render(text, True, (255,255,255))
    speedt5 = base_font_small.render(text, True, (255,255,255))

    text_t1 = base_font.render(text, True, (255,255,255))
    text_t2 = base_font.render(text, True, (255,255,255))
    text_t3 = base_font.render(text, True, (255,255,255))
    text_t4 = base_font.render(text, True, (255,255,255))

    count = 1

    input_rect = pygame.Rect(735, 10, 450, 50)
    color_passive = pygame.Color("gray15")
    color = color_passive
    active = True

    blackgr = pygame.image.load("images/black.jpg")
    blackgr = pygame.transform.scale(blackgr, (1190, 100))
    transp1 = 0
    transp2 = 0
    transp3 = 0
    transp4 = 0
    transp5 = 0

    win_rect = pygame.image.load("images/black.jpg")
    win_rect = pygame.transform.scale(win_rect, (670, 500))

    hint_img = pygame.image.load("images/hint.png")
    hint_img = pygame.transform.scale(hint_img, (30,30))
    hint_t = 0

    right_type = pygame.image.load("images/green.jpg")
    tr1 = 0
    tr2 = 0
    tr3 = 0
    tr4 = 0
    tr5 = 0

    right_nation = pygame.image.load("images/green.jpg")
    tr_1 = 0
    tr_2 = 0
    tr_3 = 0
    tr_4 = 0
    tr_5 = 0

    line = pygame.image.load("images/black.jpg")
    line = pygame.transform.scale(blackgr, (1190, 2))
    transp_1 = 0
    transp_2 = 0
    transp_3 = 0
    transp_4 = 0
    transp_5 = 0

    img1 = pygame.image.load("images/black.jpg")
    img2 = pygame.image.load("images/black.jpg")
    img3 = pygame.image.load("images/black.jpg")
    img4 = pygame.image.load("images/black.jpg")
    img5 = pygame.image.load("images/black.jpg")

    type1 = pygame.image.load("images/black.jpg")
    type2 = pygame.image.load("images/black.jpg")
    type3 = pygame.image.load("images/black.jpg")
    type4 = pygame.image.load("images/black.jpg")
    type5 = pygame.image.load("images/black.jpg")

    nation1 = pygame.image.load("images/black.jpg")
    nation2 = pygame.image.load("images/black.jpg")
    nation3 = pygame.image.load("images/black.jpg")
    nation4 = pygame.image.load("images/black.jpg")
    nation5 = pygame.image.load("images/black.jpg")

    win_text1 = "You are correct!"
    win_text = base_font.render(win_text1, True, color_dark)
    lose_text1 = "You lost! The mystery tank was:"
    lose_text = base_font.render(lose_text1, True, color_dark)

    button = pygame.Rect(900, 70, 100, 50)
    buttext = base_font_small.render('Guess!' , True , (0,0,0))
    buttext1 = base_font_small.render('Guess!' , True , (255,255,255))

    reset = pygame.Rect(1480, 980, 200, 80)
    reset_txt_bg = base_font_medium.render('RESET STATS' , True , (0,0,0))
    reset_txt = base_font_medium.render('RESET STATS' , True , (255,255,255))

    exit = pygame.Rect(1700, 980, 200, 80)
    exit_txt_bg = base_font_medium.render('EXIT' , True , (0,0,0))
    exit_txt = base_font_medium.render('EXIT' , True , (255,255,255))

    fstatus = open("data/musicstatus.txt", "r")
    status = int(fstatus.read())
    fstatus.close()

    volume = pygame.image.load("images/volume1.png")

    if status == 1:
        mixer.music.set_volume(1)
        volume = pygame.image.load("images/volume1.png")
    else:
        mixer.music.set_volume(0)
        volume = pygame.image.load("images/volume0.png")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Guess the tank | " + name)

    bg = pygame.image.load("images/bg.jpg")

    tank = random.choice(tanks)

    win = False
        
    playing = True

    while playing == True:

        keys = pygame.key.get_pressed()

        f1 = open("data/playerdata.txt", "r")
        data2 = f1.read().split(" ")
        data = [int(float(numeric_string)) for numeric_string in data2]
        wins = data[0]
        losses = data[1]
        total_guesses = data[2]
        f1.close()

        ratio = 0
        if wins != 0:
            ratio = round(total_guesses / wins, 2)

        perc = 0
        if (wins + losses) != 0:
            perc = round(wins / (wins + losses) * 100, 2)
        
        if active:
            if keys[K_BACKSPACE] == True:
                FPS.tick(10)
                text = text[:-1]

        FPS.tick(60)
        screen.blit(bg, (0, 0))

        screen.blit(credits_bg, (1657, 72))
        screen.blit(credits, (1660, 70))

        info1_1 = "Green :"
        info_text = base_font_info.render(info1_1, True, color_green)
        screen.blit(info_text, (5, 2))

        info1_2 = "You guessed the exact value"
        info_text = base_font_info.render(info1_2, True, (255,255,255))
        screen.blit(info_text, (70, 2))

        info_y = "Yellow :"
        info_text = base_font_info.render(info_y, True, color_yellow)
        screen.blit(info_text, (5, 22))

        info_y2 = "Your value is within the 10" + "%" + " range"
        info_text = base_font_info.render(info_y2, True, (255,255,255))
        screen.blit(info_text, (75, 22))

        info2 = "↑ : Your value is lower"
        info_text = base_font_info.render(info2, True, (255,255,255))
        screen.blit(info_text, (5, 42))

        info3 = "↓ : Your value is higher"
        info_text = base_font_info.render(info3, True, (255,255,255))
        screen.blit(info_text, (5, 62))

        info4 = "Guess the mystery tank!"
        info_text = base_font_small.render(info4, True, (255,255,255))
        screen.blit(info_text, (1630, 10))

        info5 = "You have %c guesses left." % str(6 - count)
        info_text = base_font_small.render(info5, True, (255,255,255))
        screen.blit(info_text, (1630, 35))

        score = "Wins: " + str(wins) + "    Losses: " + str(losses) + "    Win %: " + str(perc) + "%    Avg. guesses: " + str(ratio)
        score_txt = base_font.render(score, True, color_dark)
        score_txt_bg = base_font.render(score, True, (0,0,0))
        screen.blit(score_txt_bg, (27, 1008))
        screen.blit(score_txt, (30, 1005))

        if active:
            color = color_dark
        else:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect, 2)

        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(screen, color_dark, reset)
        pygame.draw.rect(screen, color_out, reset, 2)
        if 1680 >= mouse[0] >= 1480 and 1060 >= mouse[1] >= 980:
            pygame.draw.rect(screen, color_light, reset)
            pygame.draw.rect(screen, color_out2, reset, 2)
        screen.blit(reset_txt_bg, (1489, 1003))
        screen.blit(reset_txt, (1492, 1001))

        pygame.draw.rect(screen, color_dark, exit)
        pygame.draw.rect(screen, color_out, exit, 2)
        if 1900 >= mouse[0] >= 1700 and 1060 >= mouse[1] >= 980:
            pygame.draw.rect(screen, color_light, exit)
            pygame.draw.rect(screen, color_out2, exit, 2)
        screen.blit(exit_txt_bg, (1765, 1003))
        screen.blit(exit_txt, (1768, 1001))

        pygame.draw.rect(screen, color_dark, button)
        pygame.draw.rect(screen, color_out, button, 2)
        if 1000 >= mouse[0] >= 900 and 120 >= mouse[1] >= 70:
            pygame.draw.rect(screen, color_light, button)
            pygame.draw.rect(screen, color_out2, button, 2)
        screen.blit(buttext, (911, 83))
        screen.blit(buttext1, (913, 81))

        screen.blit(volume, (670, 10))

        blit_alpha(screen, blackgr, (20, 160), transp1)
        blit_alpha(screen, blackgr, (20, 260), transp2)
        blit_alpha(screen, blackgr, (20, 360), transp3)
        blit_alpha(screen, blackgr, (20, 460), transp4)
        blit_alpha(screen, blackgr, (20, 560), transp5)

        blit_alpha(screen, line, (20, 260), transp_1)
        blit_alpha(screen, line, (20, 360), transp_2)
        blit_alpha(screen, line, (20, 460), transp_3)
        blit_alpha(screen, line, (20, 560), transp_4)
        blit_alpha(screen, line, (20, 660), transp_5)
        blit_alpha(screen, img1, (10, 160), transp_1)
        blit_alpha(screen, right_type, (180, 160), tr1)
        blit_alpha(screen, right_nation, (290, 160), tr_1)
        blit_alpha(screen, type1, (215, 195), transp_1)
        blit_alpha(screen, nation1, (310, 190), transp_1)
        screen.blit(namet1, ((680 - 400 - namet1.get_width()) / 2 + 400,200))
        screen.blit(damaget1, (680,200))
        screen.blit(penetrationt1, (800,200))
        screen.blit(hpt1, (960,200))
        screen.blit(speedt1, (1080,200))

        blit_alpha(screen, img2, (10, 260), transp_2)
        blit_alpha(screen, right_type, (180, 260), tr2)
        blit_alpha(screen, right_nation, (290, 260), tr_2)
        blit_alpha(screen, type2, (215, 295), transp_2)
        blit_alpha(screen, nation2, (310, 290), transp_2)
        screen.blit(namet2, ((680 - 400 - namet2.get_width()) / 2 + 400, 300))
        screen.blit(damaget2, (680,300))
        screen.blit(penetrationt2, (800,300))
        screen.blit(hpt2, (960,300))
        screen.blit(speedt2, (1080,300))

        blit_alpha(screen, img3, (10, 360), transp_3)
        blit_alpha(screen, right_type, (180, 360), tr3)
        blit_alpha(screen, right_nation, (290, 360), tr_3)
        blit_alpha(screen, type3, (215, 395), transp_3)
        blit_alpha(screen, nation3, (310, 390), transp_3)
        screen.blit(namet3, ((680 - 400 - namet3.get_width()) / 2 + 400, 400))
        screen.blit(damaget3, (680,400))
        screen.blit(penetrationt3, (800,400))
        screen.blit(hpt3, (960,400))
        screen.blit(speedt3, (1080,400))

        blit_alpha(screen, img4, (10, 460), transp_4)
        blit_alpha(screen, right_type, (180, 460), tr4)
        blit_alpha(screen, right_nation, (290, 460), tr_4)
        blit_alpha(screen, type4, (215, 495), transp_4)
        blit_alpha(screen, nation4, (310, 490), transp_4)
        screen.blit(namet4, ((680 - 400 - namet4.get_width()) / 2 + 400, 500))
        screen.blit(damaget4, (680,500))
        screen.blit(penetrationt4, (800,500))
        screen.blit(hpt4, (960,500))
        screen.blit(speedt4, (1080,500))

        blit_alpha(screen, img5, (10, 560), transp_5)
        blit_alpha(screen, right_type, (180, 560), tr5)
        blit_alpha(screen, right_nation, (290, 560), tr_5)
        blit_alpha(screen, type5, (215, 595), transp_5)
        blit_alpha(screen, nation5, (310, 590), transp_5)
        screen.blit(namet5, ((680 - 400 - namet5.get_width()) / 2 + 400, 600))
        screen.blit(damaget5, (680,600))
        screen.blit(penetrationt5, (800,600))
        screen.blit(hpt5, (960,600))
        screen.blit(speedt5, (1080,600))

        screen.blit(text_t1, (660,130))
        screen.blit(text_t2, (790,130))
        screen.blit(text_t3, (940,130))
        screen.blit(text_t4, (1075,130))

        text_surface = base_font.render(text, True, (255,255,255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        hint_surface = base_font_medium.render(hint, True, (255,255,255))
        screen.blit(hint_surface, (1200, 20))

        hint_width = hint_surface.get_width()
        hint_height = hint_surface.get_height()

        if hint != "":
            hint_t = 256
            blit_alpha(screen, hint_img, (1200 + hint_width + 5, 20), hint_t)

        input_rect.w = max(text_surface.get_width() + 10, 450)

        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                
                if reset.collidepoint(event.pos):
                    wins = 0
                    total_guesses = 0
                    losses = 0
                    f2 = open("data/playerdata.txt", "w")
                    f2.write(str(wins) + " " + str(losses) + " " + str(total_guesses))
                    f2.close()
                
                if exit.collidepoint(event.pos):
                    playing = False
                    pygame.quit()
                    sys.exit()

                if 670 + volume.get_width() >= mouse[0] >= 670 and 10 + volume.get_height() >= mouse[1] >= 10:
                    if status == 1:
                        mixer.music.set_volume(0)
                        status = 0
                        volume = pygame.image.load("images/volume0.png")
                    else:
                        mixer.music.set_volume(1)
                        status = 1
                        volume = pygame.image.load("images/volume1.png")
                    fstatus2 = open("data/musicstatus.txt", "w")
                    fstatus2.write(str(status))
                    fstatus2.close()

                if 1200 + hint_width >= mouse[0] >= 1200 and 20 + hint_height >= mouse[1] >= 20:
                    text = hint
                    active = True
                    hint = ""

                if button.collidepoint(event.pos) and win == False and count <= 5:
                    for i in tanks:
                        if text.lower() == i.name.lower():
                            active = True
                            for i in tanks:
                                if text.lower() == i.name.lower():
                                    tank1 = i
                            attributes = tank.compare(tank1)

                            if count == 1:
                                transp1 = 192
                                transp_1 = 256
                                print(attributes)
                                
                                img1 = pygame.image.load("images/" + get_image(tank1))
                                type1 = pygame.image.load("images/" + tank1.typeof + ".png")
                                nation1 = pygame.image.load("images/" + tank1.nation + ".png")
                                nation1 = pygame.transform.scale(nation1, (60, 40))

                                text_t1 = base_font_table.render("Damage", True, (255,255,255))
                                text_t2 = base_font_table.render("Penetration", True, (255,255,255))
                                text_t3 = base_font_table.render("Hit Points", True, (255,255,255))
                                text_t4 = base_font_table.render("Max speed", True, (255,255,255))

                                if tank.name == tank1.name:
                                    namet1 = base_font_table.render(tank1.name, True, color_green)
                                else:
                                    namet1 = base_font_table.render(tank1.name, True, (255,255,255))
                                if tank.typeof == tank1.typeof:
                                    tr1 = 128
                                if tank.nation == tank1.nation:
                                    tr_1 = 128
                                else:
                                    pass
                                if tank.damage == tank1.damage:
                                    damaget1 = base_font_table.render(str(tank1.damage), True, color_green)
                                if tank.damage > tank1.damage:
                                    if tank.damage - tank1.damage <= tank.damage * 0.1:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                    else:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                if tank.damage < tank1.damage:
                                    if tank1.damage - tank.damage <= tank.damage * 0.1:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                    else:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                if tank.penetration == tank1.penetration:
                                    penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                if tank.penetration > tank1.penetration:
                                    if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                    else:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                if tank.penetration < tank1.penetration:
                                    if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                    else:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                if tank.hp == tank1.hp:
                                    hpt1 = base_font_table.render(str(tank1.hp), True, color_green)
                                if tank.hp > tank1.hp:
                                    if tank.hp - tank1.hp <= tank.hp * 0.1:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                    else:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                if tank.hp < tank1.hp:
                                    if tank1.hp - tank.hp <= tank.hp * 0.1:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                    else:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                if tank.speed == tank1.speed:
                                    speedt1 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                if tank.speed > tank1.speed:
                                    if tank.speed - tank1.speed <= tank.speed * 0.1:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                    else:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                if tank.speed < tank1.speed:
                                    if tank1.speed - tank.speed <= tank.speed * 0.1:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                    else:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                count += 1
                                if tank1.name.lower() == tank.name.lower():
                                    win = True
                                    wins += 1
                                    total_guesses += 1

                            elif count == 2:
                                transp2 = 192
                                transp_2 = 256
                                print(attributes)
                                
                                img2 = pygame.image.load("images/" + get_image(tank1))
                                type2 = pygame.image.load("images/" + tank1.typeof + ".png")
                                nation2 = pygame.image.load("images/" + tank1.nation + ".png")
                                nation2 = pygame.transform.scale(nation2, (60, 40))

                                if tank.name == tank1.name:
                                    namet2 = base_font_table.render(tank1.name, True, color_green)
                                else:
                                    namet2 = base_font_table.render(tank1.name, True, (255,255,255))
                                if tank.typeof == tank1.typeof:
                                    tr2 = 128
                                if tank.nation == tank1.nation:
                                    tr_2 = 128
                                else:
                                    pass
                                if tank.damage == tank1.damage:
                                    damaget2 = base_font_table.render(str(tank1.damage), True, color_green)
                                if tank.damage > tank1.damage:
                                    if tank.damage - tank1.damage <= tank.damage * 0.1:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                    else:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                if tank.damage < tank1.damage:
                                    if tank1.damage - tank.damage <= tank.damage * 0.1:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                    else:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                if tank.penetration == tank1.penetration:
                                    penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                if tank.penetration > tank1.penetration:
                                    if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                    else:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                if tank.penetration < tank1.penetration:
                                    if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                    else:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                if tank.hp == tank1.hp:
                                    hpt2 = base_font_table.render(str(tank1.hp), True, color_green)
                                if tank.hp > tank1.hp:
                                    if tank.hp - tank1.hp <= tank.hp * 0.1:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                    else:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                if tank.hp < tank1.hp:
                                    if tank1.hp - tank.hp <= tank.hp * 0.1:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                    else:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                if tank.speed == tank1.speed:
                                    speedt2 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                if tank.speed > tank1.speed:
                                    if tank.speed - tank1.speed <= tank.speed * 0.1:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                    else:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                if tank.speed < tank1.speed:
                                    if tank1.speed - tank.speed <= tank.speed * 0.1:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                    else:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                count += 1
                                if tank1.name.lower() == tank.name.lower():
                                    win = True
                                    wins += 1
                                    total_guesses += 2
                            
                            elif count == 3:
                                transp3 = 192
                                transp_3 = 256
                                print(attributes)
                                    
                                img3 = pygame.image.load("images/" + get_image(tank1))
                                type3 = pygame.image.load("images/" + tank1.typeof + ".png")
                                nation3 = pygame.image.load("images/" + tank1.nation + ".png")
                                nation3 = pygame.transform.scale(nation3, (60, 40))

                                if tank.name == tank1.name:
                                        namet3 = base_font_table.render(tank1.name, True, color_green)
                                else:
                                        namet3 = base_font_table.render(tank1.name, True, (255,255,255))
                                if tank.typeof == tank1.typeof:
                                        tr3 = 128
                                if tank.nation == tank1.nation:
                                        tr_3 = 128
                                else:
                                        pass
                                if tank.damage == tank1.damage:
                                        damaget3 = base_font_table.render(str(tank1.damage), True, color_green)
                                if tank.damage > tank1.damage:
                                        if tank.damage - tank1.damage <= tank.damage * 0.1:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                        else:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                if tank.damage < tank1.damage:
                                        if tank1.damage - tank.damage <= tank.damage * 0.1:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                        else:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                if tank.penetration == tank1.penetration:
                                        penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                if tank.penetration > tank1.penetration:
                                        if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                        else:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                if tank.penetration < tank1.penetration:
                                        if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                        else:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                if tank.hp == tank1.hp:
                                        hpt3 = base_font_table.render(str(tank1.hp), True, color_green)
                                if tank.hp > tank1.hp:
                                        if tank.hp - tank1.hp <= tank.hp * 0.1:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                        else:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                if tank.hp < tank1.hp:
                                        if tank1.hp - tank.hp <= tank.hp * 0.1:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                        else:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                if tank.speed == tank1.speed:
                                        speedt3 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                if tank.speed > tank1.speed:
                                        if tank.speed - tank1.speed <= tank.speed * 0.1:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                        else:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                if tank.speed < tank1.speed:
                                        if tank1.speed - tank.speed <= tank.speed * 0.1:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                        else:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                count += 1
                                if tank1.name.lower() == tank.name.lower():
                                        win = True
                                        wins += 1
                                        total_guesses += 3

                            elif count == 4:
                                    transp4 = 192
                                    transp_4 = 256
                                    print(attributes)
                                    
                                    img4 = pygame.image.load("images/" + get_image(tank1))
                                    type4 = pygame.image.load("images/" + tank1.typeof + ".png")
                                    nation4 = pygame.image.load("images/" + tank1.nation + ".png")
                                    nation4 = pygame.transform.scale(nation4, (60, 40))

                                    if tank.name == tank1.name:
                                        namet4 = base_font_table.render(tank1.name, True, color_green)
                                    else:
                                        namet4 = base_font_table.render(tank1.name, True, (255,255,255))
                                    if tank.typeof == tank1.typeof:
                                        tr4 = 128
                                    if tank.nation == tank1.nation:
                                        tr_4 = 128
                                    else:
                                        pass
                                    if tank.damage == tank1.damage:
                                        damaget4 = base_font_table.render(str(tank1.damage), True, color_green)
                                    if tank.damage > tank1.damage:
                                        if tank.damage - tank1.damage <= tank.damage * 0.1:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                        else:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                    if tank.damage < tank1.damage:
                                        if tank1.damage - tank.damage <= tank.damage * 0.1:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                        else:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                    if tank.penetration == tank1.penetration:
                                        penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                    if tank.penetration > tank1.penetration:
                                        if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                        else:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                    if tank.penetration < tank1.penetration:
                                        if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                        else:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                    if tank.hp == tank1.hp:
                                        hpt4 = base_font_table.render(str(tank1.hp), True, color_green)
                                    if tank.hp > tank1.hp:
                                        if tank.hp - tank1.hp <= tank.hp * 0.1:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                        else:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                    if tank.hp < tank1.hp:
                                        if tank1.hp - tank.hp <= tank.hp * 0.1:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                        else:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                    if tank.speed == tank1.speed:
                                        speedt4 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                    if tank.speed > tank1.speed:
                                        if tank.speed - tank1.speed <= tank.speed * 0.1:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                        else:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                    if tank.speed < tank1.speed:
                                        if tank1.speed - tank.speed <= tank.speed * 0.1:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                        else:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                    count += 1
                                    if tank1.name.lower() == tank.name.lower():
                                        win = True
                                        wins += 1
                                        total_guesses += 4

                            elif count == 5:
                                    transp5 = 192
                                    transp_5 = 256
                                    print(attributes)
                                    
                                    img5 = pygame.image.load("images/" + get_image(tank1))
                                    type5 = pygame.image.load("images/" + tank1.typeof + ".png")
                                    nation5 = pygame.image.load("images/" + tank1.nation + ".png")
                                    nation5 = pygame.transform.scale(nation5, (60, 40))

                                    if tank.name == tank1.name:
                                        namet5 = base_font_table.render(tank1.name, True, color_green)
                                    else:
                                        namet5 = base_font_table.render(tank1.name, True, (255,255,255))
                                    if tank.typeof == tank1.typeof:
                                        tr5 = 128
                                    if tank.nation == tank1.nation:
                                        tr_5 = 128
                                    else:
                                        pass
                                    if tank.damage == tank1.damage:
                                        damaget5 = base_font_table.render(str(tank1.damage), True, color_green)
                                    if tank.damage > tank1.damage:
                                        if tank.damage - tank1.damage <= tank.damage * 0.1:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                        else:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                    if tank.damage < tank1.damage:
                                        if tank1.damage - tank.damage <= tank.damage * 0.1:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                        else:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                    if tank.penetration == tank1.penetration:
                                        penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                    if tank.penetration > tank1.penetration:
                                        if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                        else:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                    if tank.penetration < tank1.penetration:
                                        if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                        else:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                    if tank.hp == tank1.hp:
                                        hpt5 = base_font_table.render(str(tank1.hp), True, color_green)
                                    if tank.hp > tank1.hp:
                                        if tank.hp - tank1.hp <= tank.hp * 0.1:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                        else:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                    if tank.hp < tank1.hp:
                                        if tank1.hp - tank.hp <= tank.hp * 0.1:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                        else:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                    if tank.speed == tank1.speed:
                                        speedt5 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                    if tank.speed > tank1.speed:
                                        if tank.speed - tank1.speed <= tank.speed * 0.1:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                        else:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                    if tank.speed < tank1.speed:
                                        if tank1.speed - tank.speed <= tank.speed * 0.1:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                        else:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                    count += 1
                                    if tank1.name.lower() == tank.name.lower():
                                        win = True
                                        wins += 1
                                        total_guesses += 5
                                    else:
                                        losses += 1
                            text = ""
                                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and win == False and count <= 5:
                    for i in tanks:
                        if text.lower() == i.name.lower():
                            active = True
                            for i in tanks:
                                if text.lower() == i.name.lower():
                                    tank1 = i
                            attributes = tank.compare(tank1)

                            if count == 1:
                                transp1 = 192
                                transp_1 = 256
                                print(attributes)
                                
                                img1 = pygame.image.load("images/" + get_image(tank1))
                                type1 = pygame.image.load("images/" + tank1.typeof + ".png")
                                nation1 = pygame.image.load("images/" + tank1.nation + ".png")
                                nation1 = pygame.transform.scale(nation1, (60, 40))

                                text_t1 = base_font_table.render("Damage", True, (255,255,255))
                                text_t2 = base_font_table.render("Penetration", True, (255,255,255))
                                text_t3 = base_font_table.render("Hit Points", True, (255,255,255))
                                text_t4 = base_font_table.render("Max speed", True, (255,255,255))

                                if tank.name == tank1.name:
                                    namet1 = base_font_table.render(tank1.name, True, color_green)
                                else:
                                    namet1 = base_font_table.render(tank1.name, True, (255,255,255))
                                if tank.typeof == tank1.typeof:
                                    tr1 = 128
                                if tank.nation == tank1.nation:
                                    tr_1 = 128
                                else:
                                    pass
                                if tank.damage == tank1.damage:
                                    damaget1 = base_font_table.render(str(tank1.damage), True, color_green)
                                if tank.damage > tank1.damage:
                                    if tank.damage - tank1.damage <= tank.damage * 0.1:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                    else:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                if tank.damage < tank1.damage:
                                    if tank1.damage - tank.damage <= tank.damage * 0.1:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                    else:
                                        damaget1 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                if tank.penetration == tank1.penetration:
                                    penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                if tank.penetration > tank1.penetration:
                                    if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                    else:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                if tank.penetration < tank1.penetration:
                                    if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                    else:
                                        penetrationt1 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                if tank.hp == tank1.hp:
                                    hpt1 = base_font_table.render(str(tank1.hp), True, color_green)
                                if tank.hp > tank1.hp:
                                    if tank.hp - tank1.hp <= tank.hp * 0.1:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                    else:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                if tank.hp < tank1.hp:
                                    if tank1.hp - tank.hp <= tank.hp * 0.1:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                    else:
                                        hpt1 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                if tank.speed == tank1.speed:
                                    speedt1 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                if tank.speed > tank1.speed:
                                    if tank.speed - tank1.speed <= tank.speed * 0.1:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                    else:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                if tank.speed < tank1.speed:
                                    if tank1.speed - tank.speed <= tank.speed * 0.1:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                    else:
                                        speedt1 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                count += 1
                                if tank1.name.lower() == tank.name.lower():
                                    win = True
                                    wins += 1
                                    total_guesses += 1

                            elif count == 2:
                                transp2 = 192
                                transp_2 = 256
                                print(attributes)
                                
                                img2 = pygame.image.load("images/" + get_image(tank1))
                                type2 = pygame.image.load("images/" + tank1.typeof + ".png")
                                nation2 = pygame.image.load("images/" + tank1.nation + ".png")
                                nation2 = pygame.transform.scale(nation2, (60, 40))

                                if tank.name == tank1.name:
                                    namet2 = base_font_table.render(tank1.name, True, color_green)
                                else:
                                    namet2 = base_font_table.render(tank1.name, True, (255,255,255))
                                if tank.typeof == tank1.typeof:
                                    tr2 = 128
                                if tank.nation == tank1.nation:
                                    tr_2 = 128
                                else:
                                    pass
                                if tank.damage == tank1.damage:
                                    damaget2 = base_font_table.render(str(tank1.damage), True, color_green)
                                if tank.damage > tank1.damage:
                                    if tank.damage - tank1.damage <= tank.damage * 0.1:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                    else:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                if tank.damage < tank1.damage:
                                    if tank1.damage - tank.damage <= tank.damage * 0.1:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                    else:
                                        damaget2 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                if tank.penetration == tank1.penetration:
                                    penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                if tank.penetration > tank1.penetration:
                                    if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                    else:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                if tank.penetration < tank1.penetration:
                                    if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                    else:
                                        penetrationt2 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                if tank.hp == tank1.hp:
                                    hpt2 = base_font_table.render(str(tank1.hp), True, color_green)
                                if tank.hp > tank1.hp:
                                    if tank.hp - tank1.hp <= tank.hp * 0.1:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                    else:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                if tank.hp < tank1.hp:
                                    if tank1.hp - tank.hp <= tank.hp * 0.1:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                    else:
                                        hpt2 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                if tank.speed == tank1.speed:
                                    speedt2 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                if tank.speed > tank1.speed:
                                    if tank.speed - tank1.speed <= tank.speed * 0.1:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                    else:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                if tank.speed < tank1.speed:
                                    if tank1.speed - tank.speed <= tank.speed * 0.1:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                    else:
                                        speedt2 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                count += 1
                                if tank1.name.lower() == tank.name.lower():
                                    win = True
                                    wins += 1
                                    total_guesses += 2
                            
                            elif count == 3:
                                transp3 = 192
                                transp_3 = 256
                                print(attributes)
                                    
                                img3 = pygame.image.load("images/" + get_image(tank1))
                                type3 = pygame.image.load("images/" + tank1.typeof + ".png")
                                nation3 = pygame.image.load("images/" + tank1.nation + ".png")
                                nation3 = pygame.transform.scale(nation3, (60, 40))

                                if tank.name == tank1.name:
                                        namet3 = base_font_table.render(tank1.name, True, color_green)
                                else:
                                        namet3 = base_font_table.render(tank1.name, True, (255,255,255))
                                if tank.typeof == tank1.typeof:
                                        tr3 = 128
                                if tank.nation == tank1.nation:
                                        tr_3 = 128
                                else:
                                        pass
                                if tank.damage == tank1.damage:
                                        damaget3 = base_font_table.render(str(tank1.damage), True, color_green)
                                if tank.damage > tank1.damage:
                                        if tank.damage - tank1.damage <= tank.damage * 0.1:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                        else:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                if tank.damage < tank1.damage:
                                        if tank1.damage - tank.damage <= tank.damage * 0.1:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                        else:
                                            damaget3 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                if tank.penetration == tank1.penetration:
                                        penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                if tank.penetration > tank1.penetration:
                                        if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                        else:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                if tank.penetration < tank1.penetration:
                                        if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                        else:
                                            penetrationt3 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                if tank.hp == tank1.hp:
                                        hpt3 = base_font_table.render(str(tank1.hp), True, color_green)
                                if tank.hp > tank1.hp:
                                        if tank.hp - tank1.hp <= tank.hp * 0.1:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                        else:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                if tank.hp < tank1.hp:
                                        if tank1.hp - tank.hp <= tank.hp * 0.1:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                        else:
                                            hpt3 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                if tank.speed == tank1.speed:
                                        speedt3 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                if tank.speed > tank1.speed:
                                        if tank.speed - tank1.speed <= tank.speed * 0.1:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                        else:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                if tank.speed < tank1.speed:
                                        if tank1.speed - tank.speed <= tank.speed * 0.1:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                        else:
                                            speedt3 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                count += 1
                                if tank1.name.lower() == tank.name.lower():
                                        win = True
                                        wins += 1
                                        total_guesses += 3

                            elif count == 4:
                                    transp4 = 192
                                    transp_4 = 256
                                    print(attributes)
                                    
                                    img4 = pygame.image.load("images/" + get_image(tank1))
                                    type4 = pygame.image.load("images/" + tank1.typeof + ".png")
                                    nation4 = pygame.image.load("images/" + tank1.nation + ".png")
                                    nation4 = pygame.transform.scale(nation4, (60, 40))

                                    if tank.name == tank1.name:
                                        namet4 = base_font_table.render(tank1.name, True, color_green)
                                    else:
                                        namet4 = base_font_table.render(tank1.name, True, (255,255,255))
                                    if tank.typeof == tank1.typeof:
                                        tr4 = 128
                                    if tank.nation == tank1.nation:
                                        tr_4 = 128
                                    else:
                                        pass
                                    if tank.damage == tank1.damage:
                                        damaget4 = base_font_table.render(str(tank1.damage), True, color_green)
                                    if tank.damage > tank1.damage:
                                        if tank.damage - tank1.damage <= tank.damage * 0.1:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                        else:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                    if tank.damage < tank1.damage:
                                        if tank1.damage - tank.damage <= tank.damage * 0.1:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                        else:
                                            damaget4 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                    if tank.penetration == tank1.penetration:
                                        penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                    if tank.penetration > tank1.penetration:
                                        if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                        else:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                    if tank.penetration < tank1.penetration:
                                        if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                        else:
                                            penetrationt4 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                    if tank.hp == tank1.hp:
                                        hpt4 = base_font_table.render(str(tank1.hp), True, color_green)
                                    if tank.hp > tank1.hp:
                                        if tank.hp - tank1.hp <= tank.hp * 0.1:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                        else:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                    if tank.hp < tank1.hp:
                                        if tank1.hp - tank.hp <= tank.hp * 0.1:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                        else:
                                            hpt4 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                    if tank.speed == tank1.speed:
                                        speedt4 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                    if tank.speed > tank1.speed:
                                        if tank.speed - tank1.speed <= tank.speed * 0.1:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                        else:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                    if tank.speed < tank1.speed:
                                        if tank1.speed - tank.speed <= tank.speed * 0.1:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                        else:
                                            speedt4 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                    count += 1
                                    if tank1.name.lower() == tank.name.lower():
                                        win = True
                                        wins += 1
                                        total_guesses += 4

                            elif count == 5:
                                    transp5 = 192
                                    transp_5 = 256
                                    print(attributes)
                                    
                                    img5 = pygame.image.load("images/" + get_image(tank1))
                                    type5 = pygame.image.load("images/" + tank1.typeof + ".png")
                                    nation5 = pygame.image.load("images/" + tank1.nation + ".png")
                                    nation5 = pygame.transform.scale(nation5, (60, 40))

                                    if tank.name == tank1.name:
                                        namet5 = base_font_table.render(tank1.name, True, color_green)
                                    else:
                                        namet5 = base_font_table.render(tank1.name, True, (255,255,255))
                                    if tank.typeof == tank1.typeof:
                                        tr5 = 128
                                    if tank.nation == tank1.nation:
                                        tr_5 = 128
                                    else:
                                        pass
                                    if tank.damage == tank1.damage:
                                        damaget5 = base_font_table.render(str(tank1.damage), True, color_green)
                                    if tank.damage > tank1.damage:
                                        if tank.damage - tank1.damage <= tank.damage * 0.1:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↑", True, color_yellow)
                                        else:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↑", True, (255,255,255))
                                    if tank.damage < tank1.damage:
                                        if tank1.damage - tank.damage <= tank.damage * 0.1:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↓", True, color_yellow)
                                        else:
                                            damaget5 = base_font_table.render(str(tank1.damage) + "↓", True, (255,255,255)) 
                                    if tank.penetration == tank1.penetration:
                                        penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ", True, color_green)
                                    if tank.penetration > tank1.penetration:
                                        if tank.penetration - tank1.penetration <= tank.penetration * 0.1:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, color_yellow)
                                        else:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↑", True, (255,255,255))
                                    if tank.penetration < tank1.penetration:
                                        if tank1.penetration - tank.penetration <= tank.penetration * 0.1:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, color_yellow)
                                        else:
                                            penetrationt5 = base_font_table.render(str(tank1.penetration) + " mm ↓", True, (255,255,255)) 
                                    if tank.hp == tank1.hp:
                                        hpt5 = base_font_table.render(str(tank1.hp), True, color_green)
                                    if tank.hp > tank1.hp:
                                        if tank.hp - tank1.hp <= tank.hp * 0.1:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↑", True, color_yellow)
                                        else:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↑", True, (255,255,255))
                                    if tank.hp < tank1.hp:
                                        if tank1.hp - tank.hp <= tank.hp * 0.1:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↓", True, color_yellow)
                                        else:
                                            hpt5 = base_font_table.render(str(tank1.hp) + "↓", True, (255,255,255))  
                                    if tank.speed == tank1.speed:
                                        speedt5 = base_font_table.render(str(tank1.speed) + " km/h", True, color_green)
                                    if tank.speed > tank1.speed:
                                        if tank.speed - tank1.speed <= tank.speed * 0.1:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, color_yellow)
                                        else:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↑", True, (255,255,255))
                                    if tank.speed < tank1.speed:
                                        if tank1.speed - tank.speed <= tank.speed * 0.1:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, color_yellow)
                                        else:
                                            speedt5 = base_font_table.render(str(tank1.speed) + " km/h ↓", True, (255,255,255))  
                                    count += 1
                                    if tank1.name.lower() == tank.name.lower():
                                        win = True
                                        wins += 1
                                        total_guesses += 5
                                    else:
                                        losses += 1
                            text = ""                                

            if event.type == pygame.KEYDOWN:
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            pass
                        elif event.key != pygame.K_RETURN:
                            text += event.unicode
                    for i in tanks:
                        if text.lower() in i.name.lower() and text != "":
                            hint = i.name
                            break
                        else:
                            hint = ""

        if win == True:
            active = False
            blit_alpha(screen, win_rect, (1230, 160), 192)
            win_text_bg = base_font.render(win_text1, True, (0,0,0))
            screen.blit(win_text_bg, ((1920 - win_text_bg.get_width() + 1210) / 2, 190))
            screen.blit(win_text, ((1920 - win_text_bg.get_width() + 1210) / 2 + 3, 188))

            guesses = "Guesses: " + str(count - 1)
            guesses_txt = base_font.render(guesses, True, color_dark)
            guesses_txt_bg = base_font.render(guesses, True, (0,0,0))
            screen.blit(guesses_txt_bg, ((1920 - guesses_txt_bg.get_width() + 1210) / 2, 530))
            screen.blit(guesses_txt, ((1920 - guesses_txt_bg.get_width() + 1210) / 2 + 3, 528))

            restart1 = "Press R to play again"
            restart = base_font.render(restart1, True, color_dark)
            restart_bg = base_font.render(restart1, True, (0,0,0))
            screen.blit(restart_bg, ((1920 - restart_bg.get_width() + 1210) / 2, 590))
            screen.blit(restart, ((1920 - restart_bg.get_width() + 1210) / 2 + 3, 588))

            path1 = get_image(tank)
            img = pygame.image.load("images/" + path1)
            img = pygame.transform.scale(img, (320,200))
            screen.blit(img, (1400,270))

            f2 = open("data/playerdata.txt", "w")
            f2.write(str(wins) + " " + str(losses) + " " + str(total_guesses))
            f2.close()

            if keys[K_r] == True and c == 0:
                main()
                c = 1

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        if count > 5 and win == False:
            active = False
            blit_alpha(screen, win_rect, (1230, 160), 192)
            lose_text_bg = base_font.render(lose_text1, True, (0,0,0))
            screen.blit(lose_text_bg, ((1920 - lose_text_bg.get_width() + 1210) / 2, 190))
            screen.blit(lose_text, ((1920 - lose_text_bg.get_width() + 1210) / 2 + 3, 188))
            mystery = base_font.render(tank.name, True, color_dark)
            mystery_bg = base_font.render(tank.name, True, (0,0,0))
            screen.blit(mystery_bg, ((1920 - mystery.get_width() + 1210) / 2, 240))
            screen.blit(mystery, ((1920 - mystery.get_width() + 1210) / 2 + 3, 238))

            restart1 = "Press R to play again"
            restart = base_font.render(restart1, True, color_dark)
            restart_bg = base_font.render(restart1, True, (0,0,0))
            screen.blit(restart_bg, ((1920 - restart_bg.get_width() + 1210) / 2, 570))
            screen.blit(restart, ((1920 - restart_bg.get_width() + 1210) / 2 + 3, 568))

            f2 = open("data/playerdata.txt", "w")
            f2.write(str(wins) + " " + str(losses) + " " + str(total_guesses))
            f2.close()

            img = pygame.image.load("images/clown.jpg")
            img = pygame.transform.scale(img, (200, 200))
            screen.blit(img, (1465, 310))
            
            if keys[K_r] == True and c == 0:
                main()
                c = 1

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main()