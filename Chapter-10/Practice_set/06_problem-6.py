# Q-6  Can you change the self-parameter inside a class to something else (say “raja”). Try changing self to “slf” or “raja” and see the effects.

from random import randint


class Train:
    def __init__(raja, train_no):
        raja.train_no = train_no

    def book_ticket(raja, departure, arrival):
        print(f"Ticaket is booked in {raja.train_no} from {departure} to {arrival}")

    def status(raja, departure, arrival):
        print(f"{raja.train_no} from {departure} to {arrival} is running on time.")

    def fare(raja, departure, arrival):
        print(
            f"Ticket fare in {raja.train_no} from {departure} to {arrival} is {randint(250, 500)}"
        )


travel = Train(112)
travel.book_ticket("Kathmandu", "Pokhara")
travel.status("Kathmandu", "Pokhara")
travel.fare("Kathmandu", "Pokhara")

# change the self-parameter inside a class to something else works.
