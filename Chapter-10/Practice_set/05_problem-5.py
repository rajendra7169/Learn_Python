# Q-5 Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint


class Train:
    def __init__(self, train_no):
        self.train_no = train_no

    def book_ticket(self, departure, arrival):
        print(f"Ticaket is booked in {self.train_no} from {departure} to {arrival}")

    def status(self, departure, arrival):
        print(f"{self.train_no} from {departure} to {arrival} is running on time.")

    def fare(self, departure, arrival):
        print(
            f"Ticket fare in {self.train_no} from {departure} to {arrival} is {randint(250, 500)}"
        )


travel = Train(112)
travel.book_ticket("Kathmandu", "Pokhara")
travel.status("Kathmandu", "Pokhara")
travel.fare("Kathmandu", "Pokhara")
