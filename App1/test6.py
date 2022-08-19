from kivy.app import App 

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button


ARGUMENT = True

class MyApp(App):
    def build(self):
        # Création de la fenetre
        self.window = GridLayout()
        if ARGUMENT:
            self.window.cols = 1
            self.window.rows = 2

        # Création du menu
        self.menu = GridLayout()
        if ARGUMENT:
            self.menu.cols = 4
            self.menu.rows = 1
            self.menu.size_hint = (1,0.1)
            self.menu.pos_hint = {"center_x": 0.5, "center_y":0.1}
        self.home_label = Label(text="Home",bold=True)
        self.actu_label = Button(text="Actu",bold=True)
        self.look_label = Label(text="Search",bold=True)
        self.info_label = Label(text="Info",bold=True)
        self.menu.add_widget(self.home_label)
        self.menu.add_widget(self.actu_label)
        self.menu.add_widget(self.look_label)
        self.menu.add_widget(self.info_label)
        self.window.add_widget(self.menu)

        # Création du Scroll
        self.scroll = ScrollView()
        self.content = GridLayout(cols=1,size_hint_y=None)
        self.content.row_default_height = 60
        self.content.height = 60 * 100
        for i in range(100):
            self.content.add_widget(Button(text=f"{i}"))
        self.scroll.add_widget(self.content)
        self.window.add_widget(self.scroll)


        return self.window
application = MyApp()
application.run()