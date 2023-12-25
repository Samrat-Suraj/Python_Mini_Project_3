class Train :
    def __init__(self , train_name , total_seats ,Seats_INR):
        self.train_name= train_name
        self.total_seats= total_seats
        self.available_seats= total_seats
        self.Seats_INR= Seats_INR
    
    def book_ticket (self,seats_number):
        if seats_number<=self.available_seats:
            self.available_seats -= seats_number
            print(f"Successfully booked {seats_number} seat(s) in {self.train_name}.")
        else :
            print("SORRY ! All Seats booked")

    def Check_status(self):
        print(f"available sets in {self.train_name} {self.available_seats}/{self.total_seats}")
    
    def get_Ticket_price(self):
        print(f"Ticket Price is train {self.train_name} is : {self.Seats_INR} INR")

train_datails= Train("Indain Express", 200 , 500)

train_datails.get_Ticket_price()
train_datails.Check_status()
train_datails.book_ticket(5)
train_datails.Check_status()
