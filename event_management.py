from tabulate import tabulate

events = []
tickets = []

def create_event():
    name = input("Enter event name: ")
    date = input("Enter event date (DD/MM/YYYY): ")
    time = input("Enter event time (HH:MM): ")
    venue = input("Enter event venue: ")
    description = input("Enter event description: ")
    event = {
        "name": name,
        "date": date,
        "time": time,
        "venue": venue,
        "description": description
    }
    events.append(event)
    print("Event created successfully!")

def view_events():
    if not events:
        print("No events found.")
    else:
        event_table = [[i + 1, event['name'], event['date'], event['time'], event['venue'], event['description']]
                       for i, event in enumerate(events)]
        print(tabulate(event_table, headers=["#", "Name", "Date", "Time", "Venue", "Description"], tablefmt="grid"))

def edit_event():
    view_events()
    event_index = int(input("Enter the event number to edit: ")) - 1
    if 0 <= event_index < len(events):
        event = events[event_index]
        print("Current event details:")
        print(f"Name: {event['name']}")
        print(f"Date: {event['date']}")
        print(f"Time: {event['time']}")
        print(f"Venue: {event['venue']}")
        print(f"Description: {event['description']}")
        new_name = input("Enter new name (or press Enter to keep the same): ")
        new_date = input("Enter new date (or press Enter to keep the same): ")
        new_time = input("Enter new time (or press Enter to keep the same): ")
        new_venue = input("Enter new venue (or press Enter to keep the same): ")
        new_description = input("Enter new description (or press Enter to keep the same): ")
        event['name'] = new_name or event['name']
        event['date'] = new_date or event['date']
        event['time'] = new_time or event['time']
        event['venue'] = new_venue or event['venue']
        event['description'] = new_description or event['description']
        print("Event updated successfully!")
    else:
        print("Invalid event number!!")

def delete_event():
    view_events()
    event_index = int(input("Enter the event number to delete: ")) - 1
    if 0 <= event_index < len(events):
        del events[event_index]
        print("Event deleted successfully!")
    else:
        print("Invalid event number.")

def book_ticket():
    view_events()
    event_index = int(input("Enter the event number to book tickets for: ")) - 1
    if 0 <= event_index < len(events):
        name = input("Enter your name: ")
        ticket = {
            "event": events[event_index]['name'],
            "booked_by": name
        }
        tickets.append(ticket)
        print("Ticket booked successfully!")
    else:
        print("Invalid event number.")

def view_tickets():
    if not tickets:
        print("No tickets booked.")
    else:
        ticket_table = [[i + 1, ticket['event'], ticket['booked_by']] for i, ticket in enumerate(tickets)]
        print(tabulate(ticket_table, headers=["#", "Event", "Booked By"], tablefmt="grid"))

while True:
    print("\nEvent Management System")
    print("1. Create Event")
    print("2. View Events")
    print("3. Edit Event")
    print("4. Delete Event")
    print("5. Book Ticket")
    print("6. View Tickets")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_event()
    elif choice == '2':
        view_events()
    elif choice == '3':
        edit_event()
    elif choice == '4':
        delete_event()
    elif choice == '5':
        book_ticket()
    elif choice == '6':
        view_tickets()
    elif choice == '7':
        print("Exiting the Event Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
