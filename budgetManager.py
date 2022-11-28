class BudgetManager: 
    def __init__(self):
        self.available = available
        self.budgets = {}
        self.expenditure = {}

    def addBudget(self):
        # asks for the name in a loop to ensure that the name is an alphabetical character
        i = 0
        while i < 2:
            name = input('What is the name of the budget category?')
            if name.isalpha():
                i += 1
            else:
                print('Please re-enter the name of the budget category')

        # asks for the amount in a loop to ensure that the amount is a numerical character
        j = 0
        while j == 0:
            amount = input('Please enter the amount of the budget category')
            if isinstance(amount, float):
                j = 1
            else:
                print('Please re-enter the amount of the budget category')

        # initializes available amount for the whole budget
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