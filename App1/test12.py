from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.toolbar.toolbar import MDTopAppBar 
from kivymd.uix.button.button import MDIconButton


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class PreviousMDIcons(Screen):
    
    def __init__(self, **kwargs):
        super(PreviousMDIcons, self).__init__(**kwargs)
        
        # -- Icon LS --
        a = md_icons
        self.icon_ls = []
        for j in a:
            self.icon_ls.append(j)
        
        # -- Icon Setting --
        self.icon_nb = 0
        self.icon_name = self.icon_ls[self.icon_nb]

    def set_list_md_icons(self, text="", search=False):
        # CLEAR
        m = self.ids.gl
        m.clear_widgets()

        #Set model
        def model(icon_name):
            kv = f'''
            MDTopAppBar:
                title: "{icon_name}"
                right_action_items: [["{icon_name}", lambda x: x]]        
            '''
            #return Builder.load_string(kv)
            #el = MDTopAppBar()
            #el.title = f"{icon_name}"
            #el.left_action_items = [[f"{icon_name}", lambda x: x]]
            
            g = GridLayout(cols=2)
            el=MDIconButton(icon=f"{icon_name}")
            g.add_widget(el)
            g.add_widget(Label(text=f"{icon_name}", font_size=20, color=(0,0,0)))
            return g

        #APPEND
        nb = 0
        for name_icon in self.icon_ls[self.icon_nb:(self.icon_nb + 16)] :
            if search:
                if text in name_icon:
                    m.add_widget(model(name_icon))
                    nb += 1
            else:
                m.add_widget(model(name_icon))
                nb += 1
        
        self.h = 60 * nb
        self.ids.gl.height = self.h
     
    
    def animation_RB(self,dt):
       for child in self.ids.gl.children:
            if child.children[0].text == self.icon_name:
                position = child.children[1].to_window(*child.children[1].pos)
                #print(position, self.icon_name)
                position_y = position[1]
                if position_y > 505:
                    #print("change scroll down")
                    self.icon_nb += 1
                    self.icon_name = self.icon_ls[self.icon_nb]
                    self.set_list_md_icons()
                if position_y < 450 and self.icon_nb > 0:
                    #print("scroll up")
                    self.icon_nb -= 1
                    self.icon_name = self.icon_ls[self.icon_nb]
                    self.set_list_md_icons()


            

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()
    
    def build(self):
        return self.screen
    
    def on_start(self):
        print("-- Start --")
        self.screen.set_list_md_icons()
        Clock.schedule_interval(self.screen.animation_RB, 0.5)

Builder.load_file("test12.kv")
MainApp().run()