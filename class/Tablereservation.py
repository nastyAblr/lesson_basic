class Customer: # посетитель
    def __init__(self, customer_id, name, phone, email):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

class Table:
    def __init__(self, table_number, seats): # номер столика, места
        self.table_number = table_number
        self.seats = seats
        self.is_available = True # Доступен

    def change_status(self, status):
        self.is_available = status

class Reservation:
    def __init__(self, reservation_id, customer, table, date, time, comment=""):
        self.reservation_id = reservation_id
        self.customer = customer
        self.table = table
        self.date = date
        self.time = time
        self.comment = comment
        self.status = "активно"

    def cancel(self): # отмена
        self.status = "отменено"
        self.table.change_status(True)

    def confirm(self): # подтверждение
        self.status = "подтверждено"
        self.table.change_status(False)

class CafeBookingSystem:
    def __init__(self):
        self.customers = []
        self.tables = []
        self.reservations = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_table(self, table):
        self.tables.append(table)

    def find_available_table(self, seats_required):
        for table in self.tables:
            if table.seats >= seats_required and table.is_available:
                return table
        return None

    def create_reservation(self, customer, seats_required, date, time, comment=""):
        table = self.find_available_table(seats_required)
        if table:
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(reservation_id, customer, table, date, time, comment)
            self.reservations.append(reservation)
            reservation.confirm()
            print(f"Бронирование успешно! Столик {table.table_number}, дата: {date}, время: {time}")
            return reservation
        else:
            print("Нет доступных столиков на выбранное время.")
            return None

# Пример использования
system = CafeBookingSystem()
system.add_table(Table(1, 2))
system.add_table(Table(2, 4))
system.add_table(Table(3, 6))

customer = Customer(1, "Иван", "+79991112233", "ivan@example.com")
system.add_customer(customer)

reservation = system.create_reservation(customer, 2, "2024-06-20", "19:00")
