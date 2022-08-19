from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.animation import Animation

class FirstWindow(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return FirstWindow()

Builder.load_file("test9.kv")
MyApp().run()