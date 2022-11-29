from kivy.app import App
from kivy.lang import Builder

kv = '''
ScreenManager:
    Screen:
        name: 'main_screen'
    BoxLayout:
        orientation: 'vertical'
        Label: 
            text: 'Budget for Broke Bitches'
        Button:
            text: 'Budget Button'
            on_press: budgetManager.addBudget()
        
'''

class BudgetApp(App):
    def build(self):
        return Builder.load_string(kv)


BudgetApp().run()