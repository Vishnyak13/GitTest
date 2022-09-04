class AddressBook:
    def __init__(self):
        self._contacts = []
    def add_contact(self, contact):
        self._contacts.append(contact)
    def get_contacts(self):
        return self._contacts