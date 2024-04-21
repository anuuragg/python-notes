class Address:
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
    
    def full_address(self):
        return f"{self.street}, {self.city}, {self.state} {self.zipcode}"

class ContactInfo:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email
    
    def get_contact_info(self):
        return f"Phone: {self.phone}, Email: {self.email}"

class Person:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
    
    def get_details(self):
        details = f"Name: {self.name}\n"
        details += f"Address: {self.address.full_address()}\n"
        details += f"Contact Info: {self.contact_info.get_contact_info()}"
        return details

address = Address(street="123 Main St", city="New York", state="NY", zipcode="10001")
contact_info = ContactInfo(phone="123-456-7890", email="person@example.com")

person = Person(name="John Doe", address=address, contact_info=contact_info)

print(person.get_details())

