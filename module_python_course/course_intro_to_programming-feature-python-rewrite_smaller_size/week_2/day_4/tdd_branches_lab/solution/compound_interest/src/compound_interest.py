class CompoundInterest:

    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate/100.00
        self.years = years
        self.number_of_times_per_year = 12

    def calculate_final_amount(self):
        #amount = principle (1 + rate/number_of_times_per_year) ** (rate * number)
        final_amount = self.principal * (1 + (self.rate / self.number_of_times_per_year)) ** (self.years * self.number_of_times_per_year)
        return round(final_amount, 2)

    def calculate_final_amount_with_contributions(self, monthly_contribution):
        # amount with contributions =
        # amount_from_principle +
        # monthly_contribution * (((1 + rate/number_of_times_per_year)**(rate * number_of_times_per_year) - 1) / (rate/number_of_times_per_year)) * (1+rate/number_of_times_per_year)

        final_amount_from_contributions =  (monthly_contribution * ((((1 + (self.rate / self.number_of_times_per_year)) ** (self.years * self.number_of_times_per_year)) - 1) / (self.rate / self.number_of_times_per_year))) * (1 + (self.rate / self.number_of_times_per_year))
        return round((self.calculate_final_amount() + final_amount_from_contributions), 2)
