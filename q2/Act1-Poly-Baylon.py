class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def calculate_bill(self):
        discount = 0.20
        return self.bill_amount - (self.bill_amount * discount)

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        discount = 0.15
        return self.bill_amount - (self.bill_amount * discount)

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


# Create patient objects
patient1 = Patient("Juan Dela Cruz", 15000)
patient2 = SeniorPatient("Maria Santos", 15000)
patient3 = PhilHealthPatient("Pedro Reyes", 15000)


# Display Hospital Billing System
print("Hospital Billing System")
print("------------------------")


# Regular Patient
print("Patient Name:", patient1.get_name())
patient1.display_patient_type()
print("Original Bill:", patient1.get_bill_amount())
print("Final Bill:", patient1.calculate_bill())
print()

# Senior Patient
print("Patient Name:", patient2.get_name())
patient2.display_patient_type()
print("Original Bill:", patient2.get_bill_amount())
print("Final Bill:", patient2.calculate_bill())
print()

# PhilHealth Patient
print("Patient Name:", patient3.get_name())
patient3.display_patient_type()
print("Original Bill:", patient3.get_bill_amount())
print("Final Bill:", patient3.calculate_bill())