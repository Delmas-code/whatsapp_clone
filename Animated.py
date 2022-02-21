from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation
from kivy.core.window import Window

Window.size = (305, 480)

Kvy = '''
MDScreen:
    name: "LogInPage"
    on_enter:
        app.anime(back)
        app.anime1(back1)
        app.icons(icon)
        app.text(label)
    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y: .6
            pos_hint: {'center_y': 1.8}
            radius: [0, 0, 0, 40]
            canvas:
                Color:
                    rgb: (211/255, 155/255, 255/255, 0)
                Rectangle:
                    size: self.size
                    pos: self.pos

        MDFloatLayout:
            id: back1
            size_hint_y: .58
            pos_hint: {'center_y': 1.8}
            radius: [0, 0, 0, 40]
            canvas:
                Color:
                    rgb: (211/255, 155/255, 255/255, 0)
                Ellipse:
                    size: self.size
                    pos: self.pos

        MDIconButton:
            id: icon
            icon: 'account-circle'
            pos_hint: {'center_x': .5, 'center_y': .8}
            user_font_size: '60sp'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            
        MDLabel:
            id: label
            text: f"[font=Arial]Login Page[/font]"
            markup: True
            pos_hint: {'center_y': .75}
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H5"
            opacity: 0
        MDTextField:
            hint_text: "Enter Your Email"
            size_hint_x: .8
            pos_hint: {'center_x':.5, 'center_y':.46}
            current_hint_text_color: 0, 0, 0, 1
            color_mode: 'custom'
            line_color_focus: 211/255, 155/255, 255/255, 0
        MDTextField:
            hint_text: "Enter Your Password"
            size_hint_x: .8
            pos_hint: {'center_x':.5, 'center_y':.34}
            current_hint_text_color: 0, 0, 0, 1
            password: True
            color_mode: 'custom'
            line_color_focus: 211/255, 155/255, 255/255, 0
        MDRaisedButton:
            text: "Login"
            pos_hint: {'center_x':.5, 'center_y':.2}
            size_hint_x: .8
            # md_bg_color: 148/255, 0, 211/255, 0
        MDLabel:
            text: "Did you"
            pos_hint: {'center_x':.67, 'center_y': .1}
            font_stye: "Body2"
        MDTextButton:
            text: 'forget your Password'
            pos_hint: {'center_x':.597, 'center_y': .1}
            # custom_color: 211/255, 155/255, 255/255, 0
'''


class LogIn(MDApp):
    def change_scrn(self, name):
        scrn_manager.current = name


    def build(self):
        global scrn_manager
        scrn_manager = ScreenManager()
        scrn_manager.add_widget(Builder.load_string(Kvy))
        return scrn_manager

    def anime(self, widget):
        anime = Animation(pos_hint ={'center_y': 1.15})
        anime.start(widget)

    def anime1(self, widget):
        anime1 = Animation(pos_hint={'center_y': .86})
        anime1.start(widget)
    
    def icons(self, widget):
        anime = Animation(pos_hint = {'center_y': .8})
        anime += Animation(pos_hint = {'center_y': .85})
        anime.start(widget)

    def text(self, widget):
        anime = Animation(opacity= 0, duration = 2)
        anime += Animation(opacity= 1)
        anime.start(widget)


if __name__ == "__main__":
    LogIn().run()