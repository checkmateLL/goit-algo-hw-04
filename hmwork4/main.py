def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if phone.startswith('+'):
            if not phone[1:].isdigit():
                return"Only digits should be after +"
        elif not phone.isdigit():
            return"Only digits should be in the phone number"
        contacts[name] = phone
        return "Contact added."
        
    except ValueError:
        print("Incorrect format of input. Add name and phone number.")

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            if phone.startswith('+'):
                if not phone[1:].isdigit():
                    return"Only digits should be after +"
            elif not phone.isdigit():
                return"Only digits should be in the phone number"
            contacts[name] = phone
            return "Contact updated"
        else:
            return "Contact {name} is not found"
        
    except ValueError:
        print("Incorrect format of input. Add name and phone number.")

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"User's {name} phone number is {contacts[name]}"
        else:
            return f'User {name} not found'
    except Exception as e:
        return f'Error: {e}'
    
def all_contacts(args, contacts):
    if not contacts:
        return "Contact book is empty"
    contact_book = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return f"Contact book:\n{contact_book}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all_contacts(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
