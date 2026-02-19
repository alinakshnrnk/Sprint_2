class EmployeeSalary:
    hourly_payment = 400
    
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email=None):
        if email is None:
            email = f'{name}@company.com'
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
       cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment


scl = EmployeeSalary(name='Петрович', hours=40, rest_days=2, email='petrovich@company.com')
scl.set_hourly_payment(300)
print(scl.salary())