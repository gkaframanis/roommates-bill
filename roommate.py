class Roommate:
    """
        Creates a roommate person who lives in the flat
        and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, *roommates):
        roommates_days_total = sum([roommate.days_in_house for roommate in roommates])
        # Calculating the coefficient (Weight) for the flatmate
        weight = self.days_in_house / roommates_days_total
        return round(weight * bill.amount)
