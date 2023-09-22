import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

LEFT_CLICK = 1
RIGHT_CLICK = 4


class Balle:
    def __init__(self, x, y, changeX, changeY, rayon, couleur):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.rayon = rayon
        self.couleur = couleur
    
    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.couleur)
    
    def on_update(self):
        pass

class Rectangle:
    def __init__(self, x, y, changeX, changeY, largeur, hauteur, couleur, angle):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.angle = angle
    
    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.largeur, self.hauteur, self.couleur, self.angle)
    
    def on_update(self):
        pass

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.balles = []
        self.rectangles = []

    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.on_draw()
        for rectangle in self.rectangles:
            rectangle.on_draw()
    
    def on_update(self, deltaTime):
        for balle in self.balles:
            balle.on_update()
        for rectangle in self.rectangles:
            rectangle.on_update()
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == LEFT_CLICK:
            self.balles.append(Balle(x, y, 3, 3, 10, (255, 0, 0)))
        elif button == RIGHT_CLICK:
            self.rectangles.append(Rectangle(x, y, 3, 3, 30, 20, (0, 0, 255), 45))

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")
    arcade.run()

main()
