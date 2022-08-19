from kivy.app import App 

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class HomePage(BoxLayout):
    def modify(self):
        self.ids.greeting.text = self.ids.entry.text

class MyApp(App):
    def build(self):
        return HomePage()

Builder.load_file("App1/text7.kv")
app = MyApp()
app.run()