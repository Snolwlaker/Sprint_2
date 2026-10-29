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
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment


# --- Примеры использования (для проверки) ---

# 1. Создаём сотрудника, зная всё (обычный конструктор)
emp1 = EmployeeSalary("Иван", 40, 2, "ivan@company.com")
print(f"Зарплата Ивана: {emp1.salary()}")  # 40 * 400 = 16000

# 2. Создаём сотрудника, не зная часов (используем классовый метод)
emp2 = EmployeeSalary.get_hours("Мария", None, 2, "maria@company.com")
# (7-2)*8 = 40 часов, 40 * 400 = 16000
print(f"Часы Марии: {emp2.hours}, Зарплата: {emp2.salary()}")

# 3. Создаём сотрудника, не зная email (используем классовый метод)
emp3 = EmployeeSalary.get_email("Петр", 32, 3, None)
print(f"Email Петра: {emp3.email}")  # Петр@email.com

# 4. Меняем почасовую оплату для всех
EmployeeSalary.set_hourly_payment(500)
print(f"Новая зарплата Ивана: {emp1.salary()}")  # 40 * 500 = 20000
