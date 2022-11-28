from kivy.app import App
from kivy.lang import Builder

import budgetManager

kv = '''
BoxLayout:
    orientation: 'vertical'
    Label: 
        text: 'Budget for Broke Bitches'
    Button:
        text: 'Budget Button'
        on_press: budgetManager.add_budget()
        
'''


class BudgetApp(App):
    def build(self):
        return Builder.load_string(kv)


BudgetApp().run()