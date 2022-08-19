from kivy.app import App
from kivy.uix.label import Label

# LABEL TEXT (si markup=True)
"""
[b][/b] -> Gras
[i][/i] -> Italic
[u][/u] -> Sous-ligné
[s][/s] -> Sur-ligné
[font=][/font] -> Police d'écriture (font)
[size=][/size]] -> Font size
[color=#][/color] -> Couleur
[ref=][/ref] -> Add an interactive zone. The reference + bounding box inside the reference will be available in Label.refs
[anchor=] -> Put an anchor in the text. You can get the position of your anchor within the text with Label.anchors
[sub][/sub] -> Display the text at a subscript position relative to the text before it.
[sup][/sup] -> Display the text at a superscript position relative to the text before it.
"""

# LABEL ARGUMENT
"""
text=""          -> Affiche du text
markup=True      -> Autorise les balises markup
font_size='20sp' -> Taille Globale
font_style="H1"  -> Taille Version HTML
pos_hint={'center_x':0.8,
          'center_y':0.5} 
                 -> Position selon :
                    (0X,1Y) +-----------+
                            |           |
                            |           |
                            +-----------+ (1X,0Y)
"""

class MyApp(App):
    
    def build(self):
        text = Label(text="[color=ff3333][b]'Label'[/b] is Added [/color]\n[ref=world]World[/ref]", 
                    markup=True,
                    #posix={"center_x":1,"center_y":1})
        )
        return text

application = MyApp()
application.run()