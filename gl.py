import struct
from collections import namedtuple

V2 = namedtuple("Point2", ["x", "y"])


def char(c):
    # 1 byte
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    # 2 bytes
    return struct.pack("=h", w)


def dword(d):
    # 4 bytes
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clearColor = color(0, 0, 0)
        self.currentColor = color(1, 1, 1)

        self.glViewport(0, 0, self.width, self.height)

        self.glClear()

    def glViewport(self, posx, posy, width, height):
        self.vpx = posx
        self.vpy = posy
        self.vpWidth = width
        self.vpHeight = height

    def glClearColor(self, r, g, b):
        self.clearColor = color(r, g, b)

    def glColor(self, r, g, b):
        self.currentColor = color(r, g, b)

    def glClearViewport(self, clr=None):
        for x in range(self.vpx, self.vpx + self.vpWidth):
            for y in range(self.vpy, self.vpy + self.vpHeight):
                self.glPoint(x, y, clr or self.clearColor)

    def glPoint(self, x, y, clr=None):  # Window cordinates
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = clr or self.currentColor

    def glPointvp(self, ndcx, ndcy, clr=None):  # NDC
        x = (ndcx + 1) * (self.vpWidth / 2) + self.vpx
        y = (ndcy + 1) * (self.vpHeight / 2) + self.vpy
        x = int(x)
        y = int(y)

        self.glPoint(x, y, clr or self.currentColor)

    def glLine(self, v0, v1, clr=None):
        # Brassenham line algorithm
        # y = m * x + b

        x0 = int(v0.x)
        x1 = int(v1.x)
        y0 = int(v0.y)
        y1 = int(v1.y)

        # Si el punto 0 es igual al punto 1, dibujar un punto
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0, clr)
            return

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # Si la linea tiene pendiente mayor a 1 o menor a -1, cambiar los valores de x y y
        # Se dibuja de manera vertical
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # Si el punto inicial x es mayor que el punto final x, intercambio los puntos
        # para siempre dibujar de la izquierda a la derecha
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy / dx
        y = y0

        for x in range(x0, x1 + 1):
            if steep:
                # Dibujar de manera vertical
                self.glPoint(y, x, clr)
            else:
                # Dibujar de manera horizontal
                self.glPoint(x, y, clr)

            offset += m

            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y -= 1

                limit += 1

    def glClear(self):
        self.pixels = [
            [self.clearColor for y in range(self.height)] for x in range(self.width)
        ]

    def glFinish(self, fileName):
        with open(fileName, "wb") as file:
            # Header
            file.write(bytes("B".encode("ascii")))
            file.write(bytes("M".encode("ascii")))
            file.write(dword(14 + 40 + self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(14 + 40))

            # Info header
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword(self.width * self.height * 3))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # Color table
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])
