from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.app import App

kv = '''
BoxLayout:
    orientation:'vertical' 
    FloatLayout:
        size: root.width, root.height
        Button:
            size_hint: None, None
            size: 100, 50
            text: "Hello"
            pos: root.width/2-self.width/2, root.height/2-self.height/2
'''
'''
    Widget:
        canvas.before:
            Color: 
                rgb: (1,0,0)
            Rectangle:
                pos: self.pos
                size: self.size
    
'''


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)
    

MyApp().run()