class BudgetManager: 
    def __init__(self):
        self.available = available
        self.budgets = {}
        self.expenditure = {}

    def addBudget(self):
        global available 
        available = int(input('What is the available amount for your budget?\n'))
        if name in self.budgets:
            raise ValueError('Budget Exists')
        if amount > self.available:
            raise ValueError('Insufficient Funds')
        self.budgets[name] = amount
        self.available -= amount
        self.expenditure[name] = 0
        return self.available