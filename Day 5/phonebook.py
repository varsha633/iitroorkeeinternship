def add_contact(name, number):
    phonebook[name] = number

def search_contact(name):
    return phonebook.get(name, "Not found")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        return f"{name} deleted"
    return "Contact not found"

    
add_contact("Alice", "12345")
add_contact("Bob", "67890")
print(search_contact("Alice"))
print(delete_contact("Bob"))
print(phonebook)
