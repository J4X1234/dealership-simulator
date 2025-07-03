from Car import Car

bank_account = 50000
cars = []


def importFromFile():
    filename = input('File Name: ')
    infile = open(filename)
    fileText = infile.read()
    fileLines = fileText.split('\n')
    bank_account = float(fileLines.pop(0))
    for i in range(0,len(fileLines),3):
        name = fileLines[i]
        color = fileLines[i+1]
        cost = float(fileLines[i+2])
        car = Car(name, color, cost)
        cars.append(car)

def exportToFile():
    filename = input("File Name: ")
    outFile = open(filename, 'w')
    outFile.write(str(bank_account) + '\n')
    for i in range(len(cars)):
        car = cars[i]
        outFile.write(car.name+'\n'+car.color+'\n'+str(car.cost))
        if i < len(cars) -1:outFile.write('\n')
    outFile.close()

def displayCars():
    print('Current Cars:')
    for car in cars:
        print(f"| {car.name} - {car.color} - ${car.cost}")
        print('-----------------', '\n')

def buyCar():
    global bank_account
    cost = float(input('Cost Of Car: '))
    if cost > bank_account:
        print('Insufficient Funds')
        return
    else:
        name = input('Name: ')
        color = input('Color: ')
        car = Car(name, color, cost)
        cars.append(car)
        bank_account -= cost
        cars[-1].cost = cars[-1].cost*1.2

def sellCar():
    global bank_account
    for i in range(len(cars)):
        print(f'{i}: {cars[i].name} {cars[i].color} ${cars[i].cost}')
    index = int(input('Enter Car To Sell: '))
    carToSell = cars.pop(index)
    bank_account += carToSell.cost

def paintCar():
    for i in range(len(cars)):
        print(f'{i}: {cars[i].name} {cars[i].color} ${cars[i].cost}')
    index = int(input('Enter Car To Paint: '))
    color = input('Enter New Color')
    cars[index].paint(color)

while True:
    print("Choose an option")
    print("1 - View Bank Account")
    print("2 - Load New Inv From File")
    print("3 - Write Current Inv To File")
    print("4 - View All Cars")
    print("5 - Buy A Car")
    print("6 - Sell A Car")
    print("7 - Paint A Car")
    choice = input('- ')
    
    if choice == '1':print(f'Bank Balance: ${bank_account}')
    elif choice == '2':importFromFile()
    elif choice == '3':exportToFile()
    elif choice == '4':displayCars()
    elif choice == '5':buyCar()
    elif choice == '6':sellCar()
    elif choice == '7':paintCar()