class Contact:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone


class Tenant:
    def __init__(self, name, contact_info, lease_start_date):
        self.name = name
        self.contact_info = contact_info
        self.lease_start_date = lease_start_date


class Owner:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
