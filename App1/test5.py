#Barre de menu
from kivy.app import App

#Size
from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '600')

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        #Windows
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8,0.9) #x,y
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        #Logo
        self.logo = Image(source="logo1.png")
        self.window.add_widget(self.logo)

        #Label
        self.label = Label(text="[b]What's your name ?[/b]")
        self.label.color = "#00FFCE"
        self.label.font_size = 20
        self.label.markup = True
        self.window.add_widget(self.label)

        #Entry
        self.user = TextInput(multiline=False)
        self.user.padding_y = (27,27)
        self.user.size_hint = (1,0.4)
        self.window.add_widget(self.user)

        #Button
        self.button = Button(text="Greet")
        self.button.bind(on_press=self.greeting)
        self.button.background_color = "#00FFCE"
        self.button.size_hint = (1,0.4)
        self.window.add_widget(self.button)

        return self.window
    
    def greeting(self, instance):
        self.label.text = f"Hello {self.user.text} !"

ok = MyApp()
ok.run()