from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder

Builder.load_file("Calc/calculator.kv")
Window.size = (350, 550) # (x,y)

class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text = "0"

    def button_value(self, number):
        previous_number = self.ids.input_box.text
        if previous_number == "0" or previous_number == "Wrong Equation":
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text = previous_number + f"{number}"

    def signs(self, sign):
        prev_number = self.ids.input_box.text
        self.ids.input_box.text = f"{prev_number}{sign}"

    def remove(self):
        self.ids.input_box.text = self.ids.input_box.text[:-1]
        if self.ids.input_box.text == '':
            self.clear()
    
    def result(self):
        prev_number = self.ids.input_box.text
        try:
            result = round(eval(prev_number),3)
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "Wrong Equation"
    
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-','')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"
    
    def dot(self):
        prev_number = self.ids.input_box.text
        l=list("+-*/")
        for i in range(4):
            prev_number = prev_number.split(l[i])
            try:
                prev_number = l[i+1].join(prev_number)
            except:
                pass
        if "." not in prev_number[-1]:
            if prev_number[-1] == '':
                self.signs("0.")
            else:
                self.signs(".")


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()