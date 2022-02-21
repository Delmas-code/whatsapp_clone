Kv = '''
<Tab>:

    MDLabel:
        id: label
        # text: "Tab 0"
        halign: "center"
BoxLayout:
    orientation: 'vertical'
    
    MDToolbar:
        title: 'WhatsApp'
        theme_text_color: 'Custom'
        text_color: 1, 1, 1, 1
        # font_size: '150sp'
        right_action_items: [ ['wifi', lambda x: print("wifi")], ['moon-waxing-crescent', lambda x: app.show()], ['magnify', lambda x: print("magnify")],['dots-vertical', lambda x: print("Dots")] ]
        # MDIconButton:
        #     icon: "wifi"
        # MDIconButton:
        #     icon: "moon-waxing-crescent"
        # MDIconButton:
        #     icon: "magnify"            
        # MDIconButton:
        #     icon: "hamburger"
    MDTabs:
        id: tabs
        on_tab_switch: app.on_tab_switch(*args)
        Tab: 
            text: 'CHATS'
            ScrollView:
                MDList:
                    TwoLineIconListItem:
                        text: "Patrick"
                        secondary_text: "Africa is just becoming more..."
                        IconLeftWidget:
                            icon: "account-circle"
                    TwoLineIconListItem:
                        text: "Juniour"
                        secondary_text: "Ok thanks"
                        IconLeftWidget:
                            icon: "account-circle"
                    TwoLineIconListItem:
                        text: "Rapha"
                        secondary_text: "Hey bruh have you entered..."
                        IconLeftWidget:
                            icon: "account-circle"
                    TwoLineIconListItem:
                        text: "Brandon"
                        secondary_text: "Lol"
                        IconLeftWidget:
                            icon: "account-circle"
                    TwoLineIconListItem:
                        text: "jons"
                        secondary_text: "I need a website ASAp"
                        IconLeftWidget:
                            icon: "account-circle"
                    TwoLineIconListItem:
                        text: "Flame"
                        secondary_text: "Contact arnd"
                        IconLeftWidget:
                            icon: "account-circle"
                    TwoLineIconListItem:
                        text: "Brandon"
                        secondary_text: "Lol"
                        IconLeftWidget:
                            icon: "account-circle"
        Tab:
            text: 'STATUS'
        Tab:
            text: 'CALLS'

'''