from kivy.app import App
from kivy.lang import Builder

kv = '''
ScreenManager:
    Screen:
        name: 'main_screen'
        BoxLayout:
            orientation: 'vertical'
            Label:
                text: 'Budget for a Brokey'
            BoxLayout:
                orientation: 'vertical'
                BoxLayout:
                    orientation: 'horizontal'
                    Label:
                        text: 'Input the amount of money you have for the month:'
                    TextInput:
                        text: 'Amount'
                BoxLayout:
                    orientation: 'horizontal'
                    Label: 
                        text: 'Input the categories you want to spend your money on for this month, separated by commas:'
                    TextInput: 
                        text: 'Categories'

'''

class BudgetApp(App):
    def build(self):
        return Builder.load_string(kv)


BudgetApp().run()