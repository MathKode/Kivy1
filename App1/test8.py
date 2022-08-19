from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.animation import Animation

class FirstWindow(BoxLayout):
    def __init__(self, **kwargs):
        #Fait le init du fichier hérité
        super(FirstWindow, self).__init__(**kwargs)

        #Init perso
        self.bt = self.ids.button_
        self.animate_it(self.bt) #Auto Animation
        
    def animate_it(self, button):
        #Define Animation
        animate = Animation(
            background_color=(0,0,1,1),
            duration=1.2   
        )
        
        #Define Second Animation (execute after)
        animate += Animation(
            opacity=0,
            duration=.2
        )
        
        #Last Animations
        animate += Animation(
            size_hint = (1,1),
            opacity = 1
        )
        animate += Animation(
            size_hint = (.5,.5),
        )
        
        #Start Animation
        animate.start(button)


class MyApp(App):
    def build(self):
        return FirstWindow()

Builder.load_file("test8.kv")
MyApp().run()