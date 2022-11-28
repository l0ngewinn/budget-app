from kivy.app import App
from kivy.lang import Builder

import budgetManager

kv = '''
BoxLayout:
    orientation: 'vertical'
    Label: 
        text: 'Budget for Broke Bitches'
'''


class BudgetApp(App):
    def build(self):
        return Builder.load_string(kv)


BudgetApp().run()