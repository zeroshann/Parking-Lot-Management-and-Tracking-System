def menu():
    print("\n=====Parking Lot=====")
    print("1. Set Vehicle.")
    print("2. Vehicle Entry.")
    print("3. Vehicl exit.")
    print("4. View Status.")
    print("5. Report.")
    print("6. Exit.")
    
def set_capacity():
    capacity = int(input("Enter Parking Capacity: "))
    print("Capacity Set! ")
    return capacity

def vehicle_entry(capacity, vehicle):
    if capacity == 0:
        print("Set capacity first!")
    elif len(vehicle) >= capacity:
        print("Parking Lot is currently full.")
    else:
        plate = input("Enter the Vechile plate number: ")
        vehicle.append(plate)
        print("Vehicle entered!")
    return vehicle

def vehicle_exit(vehicle):
    plate = input("Enter the plate number: ")
    if plate in vehicle:
        vehicle.remove(plate)
        print("Vehicle exited!")
    else:
        print("Vehicle was not found")
    return vehicle

def view_status(capacity, vehicle):
    print(f"\nCapacity: {capacity}")
    print(f"Occupied: {len(vehicle)}")
    print(f"Available: {capacity - len(vehicle)}")
    
def report(capacity, vehicle):
    print(f"\n===PArking Lot===")
    print(f"Capacity: {capacity}")
    print(f"Occupied Lot: {len(vehicle)}")
    print("Plate number of the vehicles")
    
    for v in vehicle:
        print(f"- {v}")
        
def main():
    capacity = 0
    vehicle = []
    
    while True:
        menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            capacity = set_capacity()
            
        elif choice == "2":
            vehicle = vehicle_entry(capacity, vehicle)
            
        elif choice == "3":
            vehicle = vehicle_exit(vehicle)
            
        elif choice == "4":
            view_status(capacity, vehicle)
            
        elif choice == "5":
            report(capacity, vehicle)
            
        elif choice == "6":
            print("Program Ended.")
            break
        
        else:
            print("invalid choice.")    
            
main()        