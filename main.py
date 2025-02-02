from gl import Renderer, color, V2
import random

width = 1920
height = 1080

rend = Renderer(width, height)

# Poligono 1:
# (165, 380) (185, 360) (180, 330) (207, 345) (233, 330) (230, 360) (250, 380) (220, 385) (205, 410) (193, 383)

# Poligono 2:
# (321, 335) (288, 286) (339, 251) (374, 302)

# Poligono 3:
# (377, 249) (411, 197) (436, 249)

# Poligono 4:
# (413, 177) (448, 159) (502, 88) (553, 53) (535, 36) (676, 37) (660, 52)
# (750, 145) (761, 179) (672, 192) (659, 214) (615, 214) (632, 230) (580, 230)
# (597, 215) (552, 214) (517, 144) (466, 180)

# Poligono 5:
# (682, 175) (708, 120) (735, 148) (739, 170)


# Funciones para generar los poligonos:
def drawPoli(poligono, clr=None):
    for i in range(len(poligono)):
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)


def fillPoli(poligono, clr=None):
    # rasterizar el poligono y llenar con lineas
    for i in range(len(poligono)):
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)
        rend.glLine(poligono[i], poligono[(i + 1) % len(poligono)], clr)


pol1 = [
    V2(165, 380),
    V2(185, 360),
    V2(180, 330),
    V2(207, 345),
    V2(233, 330),
    V2(230, 360),
    V2(250, 380),
    V2(220, 385),
    V2(205, 410),
    V2(193, 383),
]

pol2 = [
    V2(321, 335),
    V2(288, 286),
    V2(339, 251),
    V2(374, 302),
]

pol3 = [
    V2(377, 249),
    V2(411, 197),
    V2(436, 249),
]

pol4 = [
    V2(413, 177),
    V2(448, 159),
    V2(502, 88),
    V2(553, 53),
    V2(535, 36),
    V2(676, 37),
    V2(660, 52),
    V2(750, 145),
    V2(761, 179),
    V2(672, 192),
    V2(659, 214),
    V2(615, 214),
    V2(632, 230),
    V2(580, 230),
    V2(597, 215),
    V2(552, 214),
    V2(517, 144),
    V2(466, 180),
]

pol5 = [
    V2(682, 175),
    V2(708, 120),
    V2(735, 148),
    V2(739, 170),
]

drawPoli(pol1, color(1, 0, 0))
drawPoli(pol2, color(0, 1, 0))
drawPoli(pol3, color(0, 0, 1))
drawPoli(pol4, color(1, 1, 0))
drawPoli(pol5, color(1, 1, 0))

# Funcion para llenar los poligonos con lineas
fillPoli(pol1, color(1, 0, 0))
fillPoli(pol2, color(0, 1, 0))
fillPoli(pol3, color(0, 0, 1))
fillPoli(pol4, color(1, 1, 0))
fillPoli(pol5, color(1, 1, 0))

rend.glFinish("output.bmp")
