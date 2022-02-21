from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from Whats_design import Kv
from kivymd.uix import FloatLayout
from kivymd.uix.tab import MDTabsBase
# from kivymd.icon_definitions import md_icons

Window.size =(335, 550)


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class WhatsApp(MDApp):
    # def on_start(self): 
        # self.theme_cls.primary_palette = "Green"
    #     for i in range(1): 
    #         self.root.ids.tabs.add_widget(Tab(text= f"Tab {i}"))
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.theme_hue = "300"  
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "800"
        Display = Builder.load_string(Kv)
        return Display

    def show(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
        # return 'ok'


# This makes the tab clickable
    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
        ):
            '''Called when switching tabs.

            :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
            :param instance_tab: <__main__.Tab object>;
            :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
            :param tab_text: text or name icon of tab;
            '''
            # instance_tab.ids.label.text = tab_text
            pass

        

if __name__ == "__main__":
    WhatsApp().run()