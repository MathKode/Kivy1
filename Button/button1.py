from kivymd.app import MDApp
from kivy.lang.builder import Builder

from kivy.core.window import Window
Window.size = (300,600)

kv = '''
MDScreen:
    MDRectangleFlatButton:
        text: "hello"
        size_hint: .5, .2
        pos_hint: {"center_x": .5, "center_y": .5}
        
'''

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return Builder.load_string(kv)

MyApp().run()