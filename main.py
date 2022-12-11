import pandas as pd
from ticket import Ticket
from show import Show
from seatmanage import SeatManage
from seat import Seat
from termcolor import colored


while True:
    print("1. Buy Ticket\n2. Check Ticket\n3. Sync Ticket & Seat Status\n4. Exit")
    option = input("Select an option: ")
    if option == "1":
        # Get Show List And Select A Show
        Show().getshowlist()
        showid = input("Select a show: ")
        
        # Get Avaliable Seats and Select A Seat
        SeatManage(showid).getavaliableseats()
        print(f"Avaliable Seats ({colored('Common Seat', 'green')} | {colored('VIP Seat', 'yellow')}):")
        seatid = input("Select a seat: ").upper()
        
        # Prompt Owner Name
        ownername = input("Enter buyer name: ")
        ownername = ownername.split()
        if len(ownername) < 2:
            print("Invalid name. Please enter your first and last name with a space.")
            while len(ownername) < 2:
                ownername = input("Enter buyer name: ")
                ownername = ownername.split()
        ownername = " ".join(ownername)

        # Create Ticket
        ticket = Ticket()
        ticket.showid = showid
        ticket.seatid = seatid
        ticket.ownerName = ownername
        ticket.create()

    elif option == '2':
        print("1. Check Ticket from ID\n2. Check Ticket from Owner's Name")
        option = input("Select an option: ")
        if option == '1':
            ticketid = input("Enter ticket ID: ")
            t = Ticket(ticketid)
            t.getdetails()
        elif option == '2':
            ownername = input("Enter owner's name: ")
            t = Ticket(None, ownername)
            t.getdetails()

    elif option == '3':
        print("Syncing Ticket & Seat Status...")
        df = pd.read_csv('./tickets.csv')
        df = df.astype(str)
        ticketids = df['ticketID'].values
        reserved_list = []
        for ticketid in ticketids:
            print(f"Syncing Ticket #{ticketid}")
            # get reserved list from ticket
            t = Ticket(ticketid)
            t.getdata()
            t.seat = Seat(t.seatid, t.showid)
            print(f"Seat {t.seatid} from show {t.showid} is reserved")
            reserved_list.append(t.seat)
        
        seatmanage = SeatManage()
        for seat in seatmanage.getallseats():
            if seat not in reserved_list:
                print(f"Updating unreserved seat {seat.seatid} from show {seat.showid}")
                seat.reserved = False
            else:
                print(f"Updating reserved seat {seat.seatid} from show {seat.showid}")
                seat.reserved = True
            seat.update()

        print("Syncing Completed")
    elif option == '4':
        exit()
