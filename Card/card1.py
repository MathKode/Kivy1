from kivy.lang.builder import Builder

from kivymd.app import MDApp 
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard

# Card Size
"""
size_hint: <x%>, <y%>

size_hint_x: None
width: 100

size_hint_y: None
height: 20

size_hint_y: None
size_hint_x: None
size: 20,25

size_hint_x: self.minimum_width
From children
"""

kv = """
<Card_Class>
    md_bg_color: 1,0,0,1
    size_hint_y: .3
    size_hint_x: None
    width: 100
    MDRelativeLayout:
        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"right":1,"top":1}
        MDLabel:
            text: root.text
            pos_hint: {"center_x": 0.5, "center_y": .5}



   


MDScreen:
    MDBoxLayout:
        id: box
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .5, .5
        radius: 10,10,10,10
        md_bg_color: 0.83,0.83,0.83,1

"""

class Card_Class(MDCard, RoundedRectangularElevationBehavior):
    text = "okk"

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
    def on_start(self):
        box = self.root.ids.box
        box.add_widget(Card_Class()) 

MyApp().run()
    