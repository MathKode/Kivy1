from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivymd.app import MDApp

# Size Text
"""
text_size: <width>, <height>
    -> Permet de définir une boxe dans laquelle sera placé le texte
    // text_size: 10, None 
kivy.graphics.texture
    -> Sorete de modèle class
Button.texture_size = text_size
    // Si text_size: root.width, 15
    // Alors texture_size: [800, 15]
    // text_size: None = Automatique
halign: ['left', 'center', 'right', 'justify', 'auto']
    -> Choisit l'alignement du texte en x
valign: ['bottom', 'middle', 'center', 'top']
    -> Choisit l'alignement du texte en y
    // Attention, ceci est par rapport à la boxe
       crée par text_size et pas par size
       root.size != self.text_size
line_height: <nb>
    -> Espace de l'inter_ligne de la zonede texte
       (entre deux lignes)
padding: <x>, <y>
    -> Définit l'espace entre la bordure du bouton
       et le début du texte
    // |  hello  |              Padding: 2, 0
    // |      hello      |      Padding: 6, 0
padding_x: <nb>
    -> Padding Horizontal
padding_y: <nb>
    -> Padding Vertical   
"""

# Style Text
"""
outline_width: <nb> (<10)
    -> Met un contour au lettre
max_lines: <nb>
    -> Nombre de lignes maximales
strikethrough: True/False
    -> Barre le texte
underline: True/False
    -> Sous ligne le texte
"""

# Size Widget
"""
size_hint_x: <nb%>
    -> Espace que le widget utilise dans la direction de
       l'axe x par rapport à la largeur de son parent.
    // size_hint_x: 0.5 (50% de root.width)
size_hint_y: <nb%>
    -> Taille y du widget par rapport à la hauteur du pa
       rent.
size_hint: <x%>, <y%>
    -> Size_hint_x ; Size_hint_y cumulé en 1 seule ligne
width: <nb>
    -> Largeur en pixel du Widget
    // ATTENTION : il faut que size_hint_x: None
height: <nb>
    -> Hauteur du Widget
    // size_hint_y: None
       height: 100
size: <width>, <height>
    -> Regroupe width et height
x: <nb>
    -> Position x de l'objet (par rapport au bord gauche)
y: <nb>
    -> Position y de l'objet (par rapport au bottom)
pos: <x>, <y>
    // pos = (x:, y:) Regroupe x et y
pos_hint: {"x": <nb%>, "y": <nb%>, "center_x": <nb%>, "center_y": <nb%>, "right": <nb%>, "top": <nb%>}
    //  top : HAUT -> WIDGET
        right : DROITE -> WIDGET
        x : GAUCHE -> WIDGET
        y : BAS -> WIDGET
        center_x : GAUCHE -> CENTRE WIDGET
        center_y : BAS -> CENTRE WIDGET
"""

# Button Style
"""
background_color: (<r>,<g>,<b>,<a>)
    -> Couleur de font au format rgb - Alpha
       Cela agit comme multiplicateur de la texture, or comme la texture de base est grise, la couleur obtenu sera plus foncé. Pour éviter cela, il faut mettre la texture du boutton sur ''
    // background_normal: ''
    // background_color: 1, 0, 0
background_normal: <PATH>
    -> Texture Image de fond utilisé lorsque le boutton n'est pas enfoncé
    // background_normal: 'p1.png'
background_down: <PATH>
    -> Texture Image de fond utilisée lorsque le bouton est pressé
    // background_down: "p1.png"

"""

# MDIconButton
"""
icon: "<name>"
    -> Nom de l'icone
icon_size: <nb>
    -> Taille de l'icone
theme_icon_color: (“Primary”, “Secondary”, “Hint”, “Error”, “Custom”, “ContrastParentBackground”)
    -> Theme de l'icon
icon_color: (<r>,<g>,<b>,<a>)
"""

# Argument
"""
root.width
    |- Button.width
self.texture_size
    |- taille de la box text_size
self.top
    |- self.height + self.y (auteur totale depuis le bottom)
self.right
    |- self.width + self.x (largeur totale depuis le cote droit)
self.center
    |- [self.height/2 + self.y, self.width/2 + self.x]
"""
kv = '''
FloatLayout:
    Button:
        text: f"Press Me {self.center} {self.top} {self.size} eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
        id: bt
        text_size: root.width, None
        size: self.texture_size
        valign:"center"
        halign:"justify"
        line_height: 1
        padding: 40, 10
        size_hint_x: 0.7
        x:10
        y:10
        background_down_color: 1,0,0
    MDIconButton:
        pos_hint: {"x": 0.9, "center_y": 0.5}
        icon: "send-clock"
        icon_size: 64
        theme_icon_color: "ContrastParentBackground"
        icon_color: (1,0,0)
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    

MyApp().run()