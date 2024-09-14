 #Q.1 WAP  to Calculate the GROSS PAY of an employee ,
#input  basic pay of an employee (DA ) 40% of basic pay & (HRA) 10% of basic pay

print('CALCULATE THE GROSS PAY OF AN EMPLOYEE')
basic_pay = float(input("Enter the basic pay:"))
da = 0.40*basic_pay # DA is 40% of basic pay
hra = 0.10 * basic_pay # HRA is 10% of basic pay
Gross_Pay =basic_pay + da + hra
print(Gross_Pay)

# (a) Modify the above scenario , such that the DA & HRA percentages are also given as inputs.

basic_pay = float(input("Enter the basic pay:"))
da = float(input("Enter the DA: "))
hra = float(input("Enter the HRA: "))
Gross_Pay =basic_pay + da + hra
print(Gross_Pay)

'''
(b)   Update the program such that program uses a user defined function for calculating the Gross pay .
The function takes basic pay., DA percentage and HRA percentage as inputs and returns the gross pay.
'''
def calculate_gross_pay(basic_pay, da_percentage, hra_percentage):
    da_amount = basic_pay * (da_percentage / 100)
    hra_amount = basic_pay * (hra_percentage / 100)
    gross_pay = basic_pay + da_amount + hra_amount
    return gross_pay


def main():
    basic_pay = float(input("Enter Basic Pay: "))
    da_percentage = float(input("Enter DA Percentage: "))
    hra_percentage = float(input("Enter HRA Percentage: "))

    gross_pay = calculate_gross_pay(basic_pay, da_percentage, hra_percentage)

    print(f"\nGross Pay: {gross_pay:.2f}")

if __name__ == "__main__":
    main()
'''
# Q.2

You have a monthly income of rs. 1100 . Your monthly outgoings are as follows.
a. Rent - 500
b. Food - 300
c. Electricity - 40
d. Phone - 60
e. Cable TV - 30
Calculate the monthly Expenses and the remainder (what's left over each month.)
'''

Monthly_income =  1100
rent = 500
Food = 300
Electricity = 40
Phone = 60
Cable_TV = 30

Expenses = rent + Food + Electricity + Phone + Cable_TV
Remainder = Monthly_income - Expenses
print('Monthly Expenses:')
print('Rent =',rent)
print('Food =',Food)
print("Electricity =", Electricity)
print('Phone =', Phone)
print('Cable TV =', Cable_TV)
print('Total Expenses =', Expenses)
print("Remainder (what's left over each month.) =", Remainder )
'''
Q.2)a  Modify the above program by inputting the income as well as values for expenses
   and calculate monthly expense. 
'''
Monthly_income = int(input('Enter the Monthly income:'))
rent = int(input('Enter the rent:'))
Food = int(input('Enter the Food:'))
Electricity = int(input('Enter the Electricity:'))
Phone = int(input('Enter the Phone:'))
Cable_TV = int(input('Enter the Cable TV :'))

Expenses = rent + Food + Electricity + Phone + Cable_TV
Remainder = Monthly_income - Expenses
print('Monthly Expenses:')
print('Rent =',rent)
print('Food =',Food)
print("Electricity =", Electricity)
print('Phone =', Phone)
print('Cable TV =', Cable_TV)
print('Total Expenses =', Expenses)
print("Remainder (what's left over each month.) =", Remainder )

'''
Q.2) b  Include a function to check wether  you will have savings or you
have to borrow money based on the monthly income and total expenses. The function
should print an appropriate message for each case. 

'''

Monthly_income =  1100
rent = 500
Food = 300
Electricity = 40
Phone = 60
Cable_TV = 30

Expenses = rent + Food + Electricity + Phone + Cable_TV
Remainder = Monthly_income - Expenses
print('Monthly Expenses:')
print('Rent =',rent)
print('Food =',Food)
print("Electricity =", Electricity)
print('Phone =', Phone)
print('Cable TV =', Cable_TV)
print('Total Expenses =', Expenses)
print("Remainder (what's left over each month.) =", Remainder )

if Remainder> 0:
    print(f"You have savings of {Remainder}'each month.")
elif Remainder == 0:
    print('You have no savings or no borrow.')
else:
    print(f'You need to borrow {-Remainder} each month ')

'''
Q.3  For a vehicle , it's on-road cost is calculated as SUM of Basic Price , Vehicle Tax
Weight Tax  and Insurance. There are two types of vehicle - Private (P) and 
Business (B) . 
Type of        Vehicle Tax       Weight Tax        Insurance Premium 
Vehicle:         (VT):             (WT):                 (IP):
 P         5% of basic price     1% of Weight       1% of basic price
 B        10% of basic price     3% of Weight       2% of basic price
 Input price, Type and Weight of the vehicle and calculate the on-road price.

a. Modify the above program to create a dictonary for each vehicle by including
all details - Type , Weight , Basic price , Vehicle tax , weight tax , Insurance
and on-road price.
'''

def OnRoad(baseprice, vtype,weight):
    onroadprice,vt,wt,ip = 0,0,0,0
    if vtype=="B":
        vt = baseprice *0.1
        wt = weight * 0.03
        ip = baseprice * 0.02
        onroadprice = baseprice + vt + wt + ip
    if vtype=="P":
        vt = baseprice *0.05
        wt = weight * 0.01
        ip = baseprice * 0.01
        onroadprice = baseprice + vt + wt + ip
    Vehicle = {"Type":vtype,"weight":weight, "Basic price":baseprice,
                    "Vehicle Tax":vt, "Weight Tax":wt, "Insurance":ip,
                    "Onroad Price":onroadprice}
    return Vehicle

all_record = {}
counter = 1
while True:
    vtype = input("Enter B for Business /P for Private /Anyother to stop: ")
    # A
    if vtype!="B" and vtype!="P":
        break
    key = "Vehicle "+ str(counter)
    counter+=1
    price = int(input("Enter the price of the vehicle: "))
    weight = int(input("Enter the weight of the vehicle: "))
    temp_dict =  OnRoad(baseprice=price, vtype=vtype,weight=weight)

    ## {"Vehicle 1":{}, "Vehicle 2: {}}
    all_record.update({key:temp_dict})

print("All the records are:\n",all_record)
# Q. b. With the help of appropriate data organizations , get the details of N different vehicles.
Vehicle = {'Vehicle 1': {'Type': 'B', 'weight': 1260, 'Basic price': 1500000,
                              'Vehicle Tax': 120000.0, 'Weight Tax': 37.8,
                              'Insurance': 24000.0, 'Onroad Price': 1344037.8},
                'Vehicle 2': {'Type': 'B', 'weight': 2500, 'Basic price': 2100000,
                              'Vehicle Tax': 210000.0, 'Weight Tax': 75.0,
                              'Insurance': 42000.0, 'Onroad Price': 2352075.0},
                'Vehicle 3': {'Type': 'P', 'weight': 1500, 'Basic price': 1400000,
                              'Vehicle Tax': 70000.0, 'Weight Tax': 15.0,
                              'Insurance': 14000.0, 'Onroad Price': 1484015.0},
                'Vehicle 4': {'Type': 'P', 'weight': 1000, 'Basic price': 900000,
                              'Vehicle Tax': 45000.0, 'Weight Tax': 10.0,
                              'Insurance': 9000.0, 'Onroad Price': 954010.0}}
Vehicle = {'Vehicle 1': {'Type': 'B', 'weight': 1260, 'Basic price': 1200000,
                              'Vehicle Tax': 120000.0, 'Weight Tax': 37.8,
                              'Insurance': 24000.0, 'Onroad Price': 1344037.8},
                'Vehicle 2': {'Type': 'B', 'weight': 2500, 'Basic price': 2100000,
                              'Vehicle Tax': 210000.0, 'Weight Tax': 75.0,
                              'Insurance': 42000.0, 'Onroad Price': 2352075.0},
                'Vehicle 3': {'Type': 'P', 'weight': 1500, 'Basic price': 1400000,
                              'Vehicle Tax': 70000.0, 'Weight Tax': 15.0,
                              'Insurance': 14000.0, 'Onroad Price': 1484015.0},
                'Vehicle 4': {'Type': 'P', 'weight': 1000, 'Basic price': 900000,
                              'Vehicle Tax': 45000.0, 'Weight Tax': 10.0,
                              'Insurance': 9000.0, 'Onroad Price': 954010.0}}

'''
Q.c
a. Highest on road-price
b. Least Weight
Q.d 
a. The average on-road price.
b. count of vehicles that has heighest on road price than the avg on-road price.
c. count of vehicles that have weight above a given value.
d. count the vehicles that have on road price les than or equal to a given budget.
'''
high_onroad, low_weight,total_onroad = -1, 99999, 0
for key in Vehicle.keys():
    if Vehicle[key]['Onroad Price'] > high_onroad:
        high_onroad = Vehicle[key]['Onroad Price']
    if Vehicle[key]['weight'] < low_weight:
        low_weight = Vehicle[key]['weight']
    total_onroad+=Vehicle[key]['Onroad Price']
##
print("Highest on-road price is: ",high_onroad)
print("Lowest Weight among given vehicles: ",low_weight)
print("Average on-road price is: ",total_onroad / len(Vehicle))

###
budget = 1400000
avg = total_onroad / len(Vehicle)
weight = 1300
num_wt, num_budget, num_avg = 0,0,0

for key in Vehicle.keys():
    if Vehicle[key]['Onroad Price'] <= budget:
        num_budget+=1
    if Vehicle[key]['Onroad Price'] > avg:
        num_avg+=1
    if Vehicle[key]['weight'] > weight:
        num_wt+=1

print("Number of vehicle less than or equal to On-road budget: ",num_budget)
print("Number of vehicle greater than Average value: ",num_avg)
print("Number of vehicle greater than given weight: ",num_wt)



def OnRoad(baseprice, vtype,weight):
    onroadprice,vt,wt,ip = -1,-1,-1,-1
    if vtype=="B":
        vt = baseprice *0.1
        wt = weight * 0.03
        ip = baseprice * 0.02
        onroadprice = baseprice + vt + wt + ip
    if vtype=="P":
        vt = baseprice *0.05
        wt = weight * 0.01
        ip = baseprice * 0.01
        onroadprice = baseprice + vt + wt + ip
    Vehicle = {"Type":vtype,"weight":weight, "Basic price":baseprice,
                    "Vehicle Tax":vt, "Weight Tax":wt, "Insurance":ip,
                    "Onroad Price":onroadprice}
    return Vehicle

all_record = []
while True:
    vtype = input("Enter B for Business /P for Private /Anyother to stop: ")
    # A
    if vtype!="B" and vtype!="P":
        break
    price = int(input("Enter the price of the vehicle: "))
    weight = int(input("Enter the weight of the vehicle: "))
    temp_dict =  OnRoad(baseprice=price, vtype=vtype,weight=weight)
    all_record.append(temp_dict)  ## [{}, {},{},{}]


print("All the records are:\n",all_record)

Vehicle = [{'Type': 'B', 'weight': 2200, 'Basic price': 2100000,
                 'Vehicle Tax': 210000.0, 'Weight Tax': 66.0,
                 'Insurance': 42000.0, 'Onroad Price': 2352066.0},
                {'Type': 'B', 'weight': 3000, 'Basic price': 2900000,
                 'Vehicle Tax': 290000.0, 'Weight Tax': 90.0,
                 'Insurance': 58000.0, 'Onroad Price': 3248090.0},
                {'Type': 'P', 'weight': 1203, 'Basic price': 1200000,
                 'Vehicle Tax': 60000.0, 'Weight Tax': 12.030000000000001,
                 'Insurance': 12000.0, 'Onroad Price': 1272012.03},
                {'Type': 'P', 'weight': 890, 'Basic price': 800000,
                 'Vehicle Tax': 40000.0, 'Weight Tax': 8.9,
                 'Insurance': 8000.0, 'Onroad Price': 848008.9}]


