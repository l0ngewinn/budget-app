class BudgetManager: 
    def __init__(self, available):
        self.available = int(input('What is the available amount for your budget?'))
        self.budgets = {}
        self.expenditure = {}

    name = int(input('What is the name of the budget category?\n'))
    amount = input('What is the amount of this budget category?\n ')
    def add_budget(self, name, amount):
        return