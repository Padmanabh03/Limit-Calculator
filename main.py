from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from sympy import limit, oo, Symbol




class Calculus_CalculatarApp(MDApp):

    def calculate(self,args):
        x = Symbol('x')
        y = self.function.text
        lim = self.limit.text
        if(lim == "oo" or lim == "infinity"):
            z = limit(y,x,oo)
        elif(lim == "-oo" or lim == "-infinity"):
            z = limit(y,x,-oo)
        else:
            z = limit(y,x,int(lim))
        self.label.text = str(z)

    def navigation_draw(self):
        print("Navigation Successful")


    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette = 'Amber'
        self.theme_cls.accent_palette = 'BlueGray'
        self.theme_cls.theme_style = 'Dark'
        self.toolbar = MDToolbar(title='Limit Caclulator')
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.left_action_items = [["menu",lambda x: self.navigation_draw()]]
        self.toolbar.elevation = 10

        screen.add_widget(self.toolbar)

        #logo
        screen.add_widget(Image(
            source = "Logo.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.75}
        ))



        #user_input
        self.function = MDTextField(
            hint_text = "Enter the function in x",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            font_size = 22
        )
        screen.add_widget(self.function)

        self.limit = MDTextField(
            hint_text="Enter the limit",
            halign="center",
            size_hint=(0.4, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        screen.add_widget(self.limit)

        #label
        self.label = MDLabel(
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)

        #button
        screen.add_widget(MDFillRoundFlatButton(
            text = "Calculate",
            font_size = 17,
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            on_press = self.calculate

        ))


        return screen


if __name__ == '__main__':
    Calculus_CalculatarApp().run()
