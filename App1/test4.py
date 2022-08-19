from kivy.app import App

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        for i in range(5):
            layout.add_widget(Button(text=f"Button {i}"))
        return layout

app = MyApp()
app.run()