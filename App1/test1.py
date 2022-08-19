from kivy.app import App
from kivy.uix.button import Label


# Class héritée de kivy.APP pour générer une page
class HelloKivy(App):
	def build(self):
		return Label(text ="Hello Geeks")

helloKivy = HelloKivy()
helloKivy.run()
