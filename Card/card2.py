from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.core.clipboard import Clipboard
from kivy.uix.behaviors import ButtonBehavior
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.dictstore import DictStore

kv = """
<Contact@FLoatLayout>
    size_hint_y: None
    height: 50
    name: "main_layout"
    id: "ok"
    canvas.before:
        Color:
            rgb: 240/255,240/255,240/255
        RoundedRectangle:
            pos: self.pos[0] + 15, self.pos[1]
            size: self.size[0] - 30, self.size[1] 
            radius: 10, 10
    Label:
        id: name
        pos: root.pos[0] , root.pos[1]
        text: root.name
        text_size: root.size[0] - 30, root.size[1]
        halign: "left"
        valign: "center"
        font_size: 18
        font_name: "Mollen"
        padding: 10, 0
        color: 0,0,0,1
    Label:
        id: num
        pos: root.pos[0] , root.pos[1]
        text: root.num
        text_size: root.size[0] - 30, root.size[1]
        halign: "right"
        valign: "center"
        font_size: 15
        padding: 15, 0
        color: 100/255,100/255,100/255,1
        italic: True
    Label:
        id: copie
        opacity: 0
        pos: root.pos[0] , root.pos[1]
        text: "Copié !"
        font_size: 20
        bold: True
        canvas.before:
            Color:
                rgba: 58/255, 234/255, 0, 1
            RoundedRectangle:
                pos: self.pos[0] + 15, self.pos[1]
                size: self.size[0] - 30, self.size[1] 
                radius: 10, 10

<new_contact_button>
    MDRectangleFlatButton:
        pos_hint: {"center_x":.5}
        y: -40
        text: "Nouveau Contact"
        font_name: "Mollen"
        font_size: 15
        line_width: 1.5
        text_color: 2/255,196/255,222/255,1
        line_color: 2/255,196/255,222/255,1
        on_press: root.change_screen()

<new_contact_screen>
    name:"new"
    FloatLayout:
        BoxLayout:
            pos_hint: {"center_x":.5, "center_y":.45}
            size_hint: .65, None
            orientation: "vertical"
            spacing: 10
            MDLabel:
                text: "Nouveau Contact"
                font_name: "Mollen"
                font_size: 22
                text_size: self.size[0], self.size[1] + 20
                halign: "left"
                valign: "top"
                size_hint_y: None
                height: 25
            MDTextField:
                id: name_field
                hint_text: "Nom"
                multiline: False
                mode: "fill"
                radius: 11, 11
                line_color_focus: 1, 0, 1, 1
            MDTextField:
                id: num_field
                hint_text: "Numéro de téléphone"
                multiline: False
                mode: "fill"
                radius: 10, 10
                line_color_focus: 1, 0, 1, 1
            GridLayout:
                cols: 2
                rows: 1
                size_hint_y: None
                height: 60
                spacing: 20
                MDFlatButton:
                    text: "Enregistrer"
                    radius: 10, 10
                    md_bg_color: 155/255, 1, 194/255,1
                    font_name: "Mollen"
                    font_size: 15
                    size_hint: .5, .8
                    pos_hint: {"center_x":.5}
                    on_release: root.new_contact()
                MDFlatButton:
                    text: "Annuler"
                    radius: 10, 10
                    md_bg_color: 1,1,1,1
                    font_name: "Mollen"
                    font_size: 15
                    size_hint: .5, .8
                    pos_hint: {"center_x":.5}
                    line_width: 1
                    line_color: 0,0,0,1
                    on_release: root.come_back()

<Main_screen>
    name:"main"
    MDFloatLayout:
        
        #Top Bar
        MDBoxLayout:
            pos_hint: {"top":1}
            md_bg_color: 2/255,196/255,222/255,1
            size_hint: 1, None
            height: 50
            Label:
                text: "My Contact"
                font_name: "Mollen"
                font_size: 28
                color: 1,1,1,1
        
        #Contact
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            y: -60
            
            GridLayout:
                cols: 1
                spacing: 10
                size_hint_y: None
                height: 0


"""

class new_contact_button(FloatLayout):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)
        self.sm = sm
    def change_screen(self):
        self.sm.transition.direction = "left"
        self.sm.current = "new"

class new_contact_screen(Screen):
    def __init__(self, sm, main, **kwargs):
        super().__init__(**kwargs)
        self.sm = sm
        self.main_screen = main
    def come_back(self):
        self.ids.num_field.text = ""
        self.ids.name_field.text = ""
        self.main_screen.on_start()
        self.sm.transition.direction = "right"
        self.sm.current = "main"
    def new_contact(self):
        num = self.ids.num_field.text
        name = self.ids.name_field.text
        if name != "" and num != "":
            file = open("data", "r")
            c=file.read().split("\n")
            file.close()
            c.append(f"{name}:{num}")
            try: c.remove("")
            except: pass
            file = open("data", "w")
            file.write("\n".join(c))
            file.close()
            self.come_back()
        else:
            self.come_back()
        
        
        

class Contact(ButtonBehavior, FloatLayout):
    name=""
    num=""
    def __init__(self, name, num, **kwargs):
        super().__init__(**kwargs)
        self.ids.name.text = str(name)
        self.ids.num.text = str(num)
        self.num = str(num)
        float_layout = self.ids.name.parent
        print(float_layout)
    
    def on_press(self):
        Clipboard.copy(self.ids.num.text)
        anim = Animation(
            opacity=1,
            duration=.05
        )
        anim += Animation(
            opacity=0,
            duration=.75
        )
        anim.start(self.ids.copie)

class Main_screen(Screen):
    def __init__(self, sm, **kw):
        super().__init__(**kw)
        self.sm = sm

    def on_start(self):
        #contact = [["Maman", "0670561533"], ["Papa", "0670561533"], ["Mathis", "0671676883"]]
        try:
            file = open("data", "r")
            c=file.read().split("\n")
            file.close()
            contact=[]
            for i in c:
                contact.append(i.split(":"))
        except:
            contact = []
            file = open("data", "w")
            file.close()
        grid = self.children[0].children[0].children[0]
        grid.clear_widgets()
        grid.height = 0
        for name, num in contact:
            """
            grid.add_widget(Button(text=name, size_hint_y=None, height=500 ))
            grid.height += 500
            """
            grid.add_widget(Contact(name=name,num=num))
            grid.height += 60
        grid.add_widget(new_contact_button(self.sm))
    
class MyApp(MDApp):
    def build(self):

        Builder.load_string(kv)
        sm = ScreenManager()
        self.main = Main_screen(sm)
        sm.add_widget(self.main)
        sm.add_widget(new_contact_screen(sm, self.main))
        sm.current = "main"
        return sm
    
    def on_start(self):
        self.main.on_start()
        
    


LabelBase.register(name='Mollen', 
                   fn_regular='MollenBold.otf')
MyApp().run()