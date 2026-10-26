# Parent class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    # Getter methods
    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    # Method to calculate the bill amount
    def calculate_bill(self):
        return self.__bill_amount


# Child class: SeniorPatient
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.80


# Child class: PhilHealthPatient
class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.85


SeniorPatient1 = SeniorPatient("Erikah Mya", 1500)
PhilHealthPatient1 = PhilHealthPatient("Avera Ardreya", 2500)

print("Hospital Billing System")
print("------------------------")
print("Patient Name: ", SeniorPatient1.get_name())
print("Original Bill Amount: ", SeniorPatient1.get_bill_amount())
print("Final Bill: ", SeniorPatient1.calculate_bill())
print("------------------------")
print("Patient Name: ", PhilHealthPatient1.get_name())
print("Original Bill Amount: ", PhilHealthPatient1.get_bill_amount())
print("Final Bill: ", PhilHealthPatient1.calculate_bill())