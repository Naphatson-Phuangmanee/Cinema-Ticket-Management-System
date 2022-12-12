# Cinema-Ticket-Management-System
This program is a part of the 01219114 & 01219115 Computer Programming 1 course. Cinema-Ticket-Management-System is for cinema staffs that in charge of buying/selling and checking information or deploying it to ticket vending or robots.

## Overview 
The program is mainly designed for staffs or cinema staffs or ticket vending and robots. This program can work together with all parts, especially the ticket system,show time and the seats, each part is retrieved from each other.


# Classes
## Ticket Class
* Ticket classes are used to store seating information and show time. It also used for selling tickets or checking tickets when walking into the theater by pulling objects from Show class to work with.
### Attributes
* ticketID: int 
* ownerName: str - Enter the name of the ticket purchaser
* showid: int - For reference to call the object Show
* seatid: str - For reference to call the object Seat
* show: object show time
* seat: object Indicates the ticket's cinema seating position.
### Functions
* getData(): get data by ticketID from csv file
* getDetails() - Retrieve cinema ticket details, work with Show class to retrieve show schedule information as well. 
* create(): for ticket issuing

## Show class
Show is use to store Show time data. Also used to work with class Tickets.

### Attributes
* showID: int - Show time ID
* theater: int - Theater number
* movieName: str - Name of the movie
* showTime: str - Show time of the movie
* duration: int - Duration of the movie
### Functions
* getData(): Get data by showID from csv file
* getshowlist() Returns all available "show" data

## Seat Class
### Attributes
* seatID: str (A1,B1,C1) - Indicates the ticket's cinema seating position.
* showID: int - Show time ID
* type; str - seat type
* reserved: boolean - Reserve status
### Functions
* getData(): Get data by seatID from csv file
* update(): Modify the reserve status.
* __eq_(): Fixed object equality check method so that objects with seatID and showID are equal.

## SeatManage Class
### Attributes
* showID: int
### Functions
* getAvailableSeats(): Restore empty seats for use in issuing tickets
* getallseats(): Returns all seats in the system for use in syncing data.

And here is class diagram of the program.

![Class Diagram Cinema Ticket Management System](/Class-Diagram-Cinema-Ticket-Management-System.png)


## Code structure
* [main.py](main.py): Retrieve data from database to display when ticket issuing and manage to call objects of each class to work together.
* [Seatmanage](seatmanage.py): Get avaliable seats from the showid.csv file and get all of the showid.csv file.
* [Show.py](show.py): Get show data by showid from the csv file and get all shows avaliable from the csv file.
* [Tickets.py](ticket.py): Get ticket data by ticketid or ownername from the csv file, get ticket details by ticketid from the csv file and create a new ticket generate new ticket id, add record to the csv file and update seat reserved status.

## Function of Cinema Ticket Management System
1. Option "1": Get Show List And Select A Show, Get Avaliable Seats and Select A Seat , Prompt Owner Name and Create Ticket.
2. Option "2": Check Ticket
3. Option "3": Syncing Ticket & Seat Status
4. Option "4": Exit the program
