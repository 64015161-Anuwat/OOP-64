# ========== Hand Tools ==========

class TapeMeasure:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class Screwdriver:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class Hammer:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class Drill:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class Saw:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class Plier:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


# ========== Human ==========

class Employee:
    def __init__(self, name, age, address, position):
        self.name = name
        self.age = age
        self.address = address
        self.position = position


class Customer:
    def __init__(self, name, age, address, discount):
        self.name = name
        self.age = age
        self.address = address
        self.discount = discount


# ========== Instance of Class ==========

tape_measure = TapeMeasure(50, 225)
screwdriver = Screwdriver(20, 100)
hammer = Hammer(25, 150)
drill = Drill(10, 250)
saw = Saw(15, 75)
plier = Plier(5, 50)
employee_seller_00 = Employee("Mr. Anuwat Sa-ubol", 21, "Samutsongkhram", "Seller")
customer_00 = Customer("Mr. Supamit thiensiri", 21, "Samutsongkhram", 5)

# ========== Access & Update ==========
print("===== tape_measure =====")
print("tape_measure Price : "+str(tape_measure.price))
tape_measure.price = 275
print("Update tape_measure Price : "+str(tape_measure.price)+"\n")

print("===== screwdriver =====")
print("screwdriver Price : "+str(tape_measure.price))
screwdriver.price = 125
print("Update screwdriver Price : "+str(tape_measure.price)+"\n")

print("===== hammer =====")
print("hammer Price : "+str(tape_measure.price))
screwdriver.price = 175
print("Update hammer Price : "+str(tape_measure.price)+"\n")

print("===== drill =====")
print("drill Price : "+str(tape_measure.price))
screwdriver.price = 300
print("Update drill Price : "+str(tape_measure.price)+"\n")

print("===== saw =====")
print("saw Price : "+str(tape_measure.price))
screwdriver.price = 100
print("Update saw Price : "+str(tape_measure.price)+"\n")

print("===== plier =====")
print("plier Price : "+str(tape_measure.price))
screwdriver.price = 75
print("Update plier Price : "+str(tape_measure.price)+"\n")

print("===== amount of Product =====")
print("tape_measure amount : "+str(tape_measure.amount))
print("screwdriver amount : "+str(screwdriver.amount))
print("hammer amount : "+str(hammer.amount))
print("drill amount : "+str(drill.amount))
print("saw amount : "+str(saw.amount))
print("plier amount : "+str(plier.amount))
print("===== total_amount of Product =====")
total_amount = tape_measure.amount + screwdriver.amount + hammer.amount + drill.amount + saw.amount + plier.amount
print("total_amount : "+str(total_amount)+"\n")

print("===== employee_seller_00 =====")
print("employee_seller_00 Name : "+employee_seller_00.name)
print("employee_seller_00 Address : "+employee_seller_00.address)
employee_seller_00.address = "Bangkok"
print("Update employee_seller_00 Address : "+employee_seller_00.address+"\n")

print("===== customer_00 =====")
print("customer_00 Name : "+customer_00.name)
print("customer_00 Age : "+str(customer_00.age))
customer_00.age = 22
print("Update customer_00 Age : "+str(customer_00.age))
