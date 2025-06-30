#smart_scheduler

exam_schedule = []

def add_exam():
    name = input("Enter the exam name: ")
    date = input("Enter the exam date (YYYY-MM-DD): ")
    time = input("Enter the exam time (HH:MM): ")
    room = input("Enter the exam room: ")
    exam_schedule.append({
        'name': name,
        'date': date,
        'time': time,
        'room': room
    })
    print("Exam added successfully!\n")

def view_exams():
    if not exam_schedule:
        print("No exam schedule available.\n")
        return
    print("All Scheduled Exams:")
    for index, exam in enumerate(exam_schedule, start=1):
        print(f"{index}. {exam['name']} on {exam['date']} at {exam['time']} in {exam['room']}")   
    print()

def edit_exam():
    view_exams()
    if not exam_schedule:
        return     
    try:
        index = int(input("Enter the exam number to edit: ")) - 1
        if 0 <= index < len(exam_schedule):
            print("Leave blank if no change.")
            name = input("Enter the new exam name: ")
            date = input("Enter the new exam date (YYYY-MM-DD): ")
            time = input("Enter the new exam time (HH:MM): ")
            room = input("Enter the new exam room: ")

            if name: exam_schedule[index]['name'] = name
            if date: exam_schedule[index]['date'] = date
            if time: exam_schedule[index]['time'] = time
            if room: exam_schedule[index]['room'] = room

            print("Exam updated successfully!\n")
        else:
            print("Invalid exam number.\n") 
    except ValueError:
        print("Please enter a valid number.\n")

def delete_exam():
    view_exams()
    if not exam_schedule:
        return
    try:
        index = int(input("Enter the exam number to delete: ")) - 1
        if 0 <= index < len(exam_schedule):
            remove = exam_schedule[index]
            del exam_schedule[index]
            print(f"Exam '{remove['name']}' deleted successfully!\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main_menu():
    while True:
        print("Smart Exam Scheduler")
        print("1. Add Exam")
        print("2. View Exams")  
        print("3. Edit Exam")
        print("4. Delete Exam") 
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_exam()  
        elif choice == '2':
            view_exams()    
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()   
        elif choice == '5':
            print("Have a nice a day. Goodluck to your exams!:")
            break
        else:
            print("Invalid choice. Please try again.\n")    

if __name__ == "__main__":
    main_menu()

