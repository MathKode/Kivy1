from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder 
from kivy.core.window import Window

Builder.load_file("test10.kv")
Window.size = (350, 550)

class MainWindow(MDBoxLayout):
    def call_back(self):
        print("ok")

class MyApp(MDApp):
    def build(self):
        return MainWindow()

MyApp().run()
