AllowedVechiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']


def display_menu():
     print('********************************')
     print('AutoCountry Vehicle Finder v0.3')
     print('********************************')
     print('Please Enter the following number below from the following menu:')
     print('1. PRINT all Authorized Vehicles')
     print('2. SEARCH for Authorized Vehicle')
     print('3. ADD Auhtoirzed Vehicle')
     print('4. Exit')
   



def all_authorized_cars():
     print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
     for vehicle in AllowedVechiclesList:
          print(vehicle)

def smart_find():
    searching = input('PLease Enter the full Vehicle name: ')
    if searching in AllowedVechiclesList:
        print(f'{searching} is an authorized vehicle')
    else:
        print(f'{searching} is not an authorized vehicle, if you received this error please check the spelling and try again')

def add_authorized_vehicle():
    new_car = input('Please Enter the full Vehicle name you would like add: ')
    AllowedVechiclesList.append(new_car)
    print(f'You have added "{new_car}" as an authorized vehicle')


def main():
    while True:
        display_menu()
        pick = input('Enter your choice: ')
        if pick == '1':
            all_authorized_cars()
        elif pick == '2':
            smart_find()
        elif pick == '3':
            add_authorized_vehicle()
        elif pick == '4':
            print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
            input('Press any key to exit.')
        else:
            print('Invalid option. Please try again.')
    
       
        
if __name__ == '__main__':
    main()  

    


