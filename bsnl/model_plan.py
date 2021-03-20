class BsnlPlan(object):
    plan_type = ''
    amount = ''
    plan_name = ''
    circle = ''
    benefit = ''
    description = ''

    def __int__(self):
        print("plan model initialize")

    def __init__(self, plan_type, amount, benefit, plan_name, circle, description):
        self.plan_type = plan_type
        self.amount = amount
        self.plan_name = plan_name
        self.circle = circle
        self.description = description
        self.benefit = benefit

    def set_plan_type(self, plan_type):
        self.plan_type = plan_type

    def get_plan_type(self):
        return self.plan_type

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_benefit(self, benefit):
        self.benefit = benefit

    def get_benefit(self):
        return self.benefit

    def set_plan_name(self, plan_name):
        self.plan_name = plan_name

    def get_plan_name(self):
        return self.plan_name

    def set_circle(self, circle):
        self.circle = circle

    def get_circle(self):
        return self.circle

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def __str__(self):
        return self.plan_type + " | " \
               + self.plan_name \
               + " | " + self.amount + " | " + self.benefit + " | " + self.circle \
               + " | " + self.description
