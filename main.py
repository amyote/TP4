import math
import random
import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


# La classe de balles.
class Balle:
    def __init__(self, x, y, changeX, changeY, rayon, couleur):
        self.x = x
        self.y = y
        self.changeX = changeX
        self.changeY = changeY
        self.rayon = rayon
        self.couleur = couleur
    
    # Dessiner la balle.
    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.couleur)
    
    # Detecter si la balle sort du cadre sur la prochaine image. Si oui, inverser la direction.
    def on_update(self):

        if self.x + self.changeX + self.rayon > SCREEN_WIDTH or self.x + self.changeX - self.rayon < 0:
            self.changeX *= -1

        if self.y + self.changeY + self.rayon > SCREEN_HEIGHT or self.y + self.changeY - self.rayon < 0:
            self.changeY *= -1
        
        self.x += self.changeX
        self.y += self.changeY

# La classe de rectangles.
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

        angleRad = math.pi * angle / 180

        # Lignes du point central au milieu d'une arete du rectangle. Soit dans le sens de la largeur ou dans le sens de la hauteur.
        vecteurLargeur = (self.largeur * math.cos(angleRad) / 2, self.largeur * math.sin(angleRad) / 2)
        vecteurHauteur = (self.hauteur * math.cos(angleRad + math.pi / 2) / 2, self.hauteur * math.sin(angleRad + math.pi / 2) / 2)

        # Avec ca, on calcule les 4 points du rectangle.
        point1 = tuple([vecteurLargeur[i] + vecteurHauteur[i] + (self.x, self.y)[i] for i in range(2)])
        point2 = tuple([vecteurLargeur[i] - vecteurHauteur[i] + (self.x, self.y)[i] for i in range(2)])
        point3 = tuple([-vecteurLargeur[i] + vecteurHauteur[i] + (self.x, self.y)[i] for i in range(2)])
        point4 = tuple([-vecteurLargeur[i] - vecteurHauteur[i] + (self.x, self.y)[i] for i in range(2)])

        # Finalement, on calcule le plus haut, plus bas, plus a droite et plus a gauche du rectangle tourne.
        self.droiteMax = max(max(point1[0], point2[0]), max(point3[0], point4[0]))
        self.gaucheMax = min(min(point1[0], point2[0]), min(point3[0], point4[0]))
        self.hautMax = max(max(point1[1], point2[1]), max(point3[1], point4[1]))
        self.basMax = min(min(point1[1], point2[1]), min(point3[1], point4[1]))
    
    # Dessiner le rectangle.
    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.largeur, self.hauteur, self.couleur, self.angle)
    
    # Detecter si le rectangle sort du cadre sur la prochaine image. Si oui, inverser la direction.
    def on_update(self):

        if self.droiteMax + self.changeX > SCREEN_WIDTH or self.gaucheMax + self.changeX < 0:
            self.changeX *= -1

        if self.hautMax + self.changeY > SCREEN_HEIGHT or self.basMax + self.changeY < 0:
            self.changeY *= -1
        
        self.x += self.changeX
        self.y += self.changeY

        # Bouger les bords de detection de collision avec le rectangle.
        self.droiteMax += self.changeX
        self.gaucheMax += self.changeX
        self.hautMax += self.changeY
        self.basMax += self.changeY
        

# La classe du jeu.
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.balles = []
        self.rectangles = []

    # Pour dessiner une image, on dessine les balles et rectangles individuellement.
    def on_draw(self):
        arcade.start_render()
        for balle in self.balles:
            balle.on_draw()
        for rectangle in self.rectangles:
            rectangle.on_draw()
    
    # Pour mettre a jour la logique du jeu, on le fait individuellement sur les balles et rectangles.
    def on_update(self, deltaTime):
        for balle in self.balles:
            balle.on_update()
        for rectangle in self.rectangles:
            rectangle.on_update()
    
    # Si on clique, creer soit une balle ou un rectangle, dependant de si c'est un clic droit ou gauche.
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.balles.append(Balle(x, y, 3, 3, 10, (255, 0, 0)))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            self.rectangles.append(Rectangle(x, y, 3, 3, 30, 20, (0, 0, 255), random.randint(0, 360)))

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "TP4")
    arcade.run()

# Partir le jeu.
main()
