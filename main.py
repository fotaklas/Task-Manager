# Task Manager

# Λίστα για αποθήκευση των tasks
tasks = []

# Προσθήκη νέου task
def add_task(name, goal_time):
    tasks.append({"name": name, "goal_time": goal_time, "time_spent": 0})
    print(f"Το task '{name}' προστέθηκε με στόχο {goal_time} ώρες.")

# Ενημέρωση χρόνου για task
def update_task(name, time):
    for task in tasks:
        if task["name"] == name:
            task["time_spent"] += time
            print(f"Προστέθηκαν {time} ώρες στο task '{name}'.")
            return
    print(f"Το task '{name}' δεν βρέθηκε.")

# Αναφορά στο τέλος της ημέρας
def daily_summary():
    print("\n--- Αναφορά Ημέρας ---")
    for task in tasks:
        print(f"{task['name']}: {task['time_spent']} ώρες από {task['goal_time']} στόχο.")
        if task['time_spent'] >= task['goal_time']:
            print("✅ Ολοκληρώθηκε!")
        else:
            print("❌ Δεν ολοκληρώθηκε.")
    print("------------------------")

# Κεντρικό πρόγραμμα
def main():
    while True:
        print("\n1. Προσθήκη Task")
        print("2. Ενημέρωση Task")
        print("3. Αναφορά Ημέρας")
        print("4. Έξοδος")
        choice = input("Διάλεξε επιλογή: ")

        if choice == "1":
            name = input("Όνομα Task: ")
            goal_time = float(input("Στόχος (σε ώρες): "))
            add_task(name, goal_time)
        elif choice == "2":
            name = input("Όνομα Task: ")
            time = float(input("Χρόνος που δούλεψες (σε ώρες): "))
            update_task(name, time)
        elif choice == "3":
            daily_summary()
        elif choice == "4":
            print("Έξοδος...")
            break
        else:
            print("Μη έγκυρη επιλογή!")

if __name__ == "__main__":
    main()
    
