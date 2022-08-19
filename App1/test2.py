from kivy.app import App
from kivy.uix.button import Label

class MyApp(App):
    def build(self):
        text = Label(text="Bonjour")
        return text

application = MyApp()
application.run()