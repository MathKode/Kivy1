from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):
    def add_icon(self, name_icon):
        self.ids.rv.data.append(
            {
                "viewclass": "CustomOneLineIconListItem",
                "icon": name_icon,
                "text": name_icon,
                "callback": lambda x: x,
            }
        )

    def set_list_md_icons(self, text="", search=False):
        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    self.add_icon(name_icon)
            else:
                self.add_icon(name_icon)
    
    def animation_RB(self,dt):
       pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()
    
    def build(self):
        return self.screen
    
    def on_start(self):
        print("-- Start --")
        self.screen.set_list_md_icons()
        Clock.schedule_interval(self.screen.animation_RB, 0.1)

Builder.load_file("test11.kv")
MainApp().run()