class FlightTable:
    def __init__(self):
        self.data = []

    def add_entry(self, p_id, process, start_time, priority):
        self.data.append({
            'P_ID': p_id,
            'Process': process,
            'Start Time (ms)': start_time,
            'Priority': priority
        })

    def print_table(self):
        for entry in self.data:
            print(f"{entry['P_ID']} | {entry['Process']} | {entry['Start Time (ms)']} | {entry['Priority']}")

    def sort_by_pid(self):
        self.data.sort(key=lambda x: int(x['P_ID'][1:])) 

    def sort_by_start_time(self):
        self.data.sort(key=lambda x: x['Start Time (ms)'])
    def custom_priority_key(self, entry):
        priority_order = {"High": 0, "MID": 1, "Low": 2}
        return priority_order[entry['Priority']]

    def sort_by_priority(self):
        self.data.sort(key=self.custom_priority_key)

  
if __name__ == "__main__":
    flight_table = FlightTable()

    flight_table.add_entry("P1", "VSCode", 100, "MID")
    flight_table.add_entry("P23", "Eclipse", 234, "MID")
    flight_table.add_entry("P93", "Chrome", 189, "High")
    flight_table.add_entry("P42", "JDK 9", 9, "High")
    flight_table.add_entry("P9", "CMD", 7, "High")
    flight_table.add_entry("P87", "NotePad", 23, "Low")

    while True:
        print("Choose a sorting option:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_table.sort_by_pid()
            print("\nFlight Table Sorted by P_ID:")
            flight_table.print_table()
        elif choice == '2':
            flight_table.sort_by_start_time()
            print("\nFlight Table Sorted by Start Time:")
            flight_table.print_table()
        elif choice == '3':
            flight_table.sort_by_priority()
            print("\nFlight Table Sorted by Priority:")
            flight_table.print_table()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")
