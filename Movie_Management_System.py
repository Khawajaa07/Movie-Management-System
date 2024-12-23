#              Movie Management System

import os
import numpy as np

#MOVIES

#function to add movie
def addmovie(id, title, genre, language, duration, ticketprice):
    movie_details = f"{id}, {title}, {genre}, {language}, {duration}, {ticketprice}"
    lines = []
    with open("movies.txt","r") as file:
        lines = file.readlines()
        for line in  lines:
            if str(id) in line:
                return f" Movie with id:{id} already exists."
            else:
                with open("movies.txt", "a"):
                    file.write(str(movie_details)+"\n")
                    return "Movie Added Successfully"


#function to view movie
def viewmovies():
    if os.path.exists("movies.txt"):
        with open("movies.txt", "r") as file:
            movies = file.read()
            if movies:
                return movies
            else: 
                return "No movies available"

    else:
        return "No Movies File"


#function to  search for a movie
def searchmovie(id):
    if os.path.exists("movies.txt"):
        with open("movies.txt", "r") as file:
            for line in file:
                if str(id) in line:
                    a =  line.strip()
                else:
                    a =  "Movie Not Found"
            return a
    else: 
        return "No Movies File"


#function to update a movie
def updatemovie(id, title, genre, language , duration, ticketprice):
    lines = []
    if os.path.exists("movies.txt"):
        with open("movies.txt", "r") as file:
            lines = file.readlines()

        for line in range(len(lines)):
            if str(id) in lines[line]:
                lines[line] = f"{id}, {title}, {genre}, {language}, {duration}, {ticketprice}"
                with open("movies.txt", "w") as file:
                    file.writelines(lines)
                    return "Movie Updated"
            else: 
                return "Movie Not Found"
    else:
        return "No Movies File"


#function to delete a movie
def deletemovie(id):
    lines = []
    movie_found = False
    if os.path.exists("movies.txt"):
        with open("movies.txt", "r") as file:
            lines = file.readlines()

        with open("movies.txt", "w") as file:
            for line in lines:
                if str(id) not in line:
                    file.write(line)
                else:
                    movie_found = True
        
            if movie_found:
                return "Movie deleted"
            else: 
                return "Movie not Found"
    else:
        return "No Movies File"



#SHOWS

#function to add show
def addshow(MovieId, ShowId, Date, time, Screen, Seats):
    show_details = f"{ShowId}, {MovieId}, {Date}, {time}, {Screen}, {Seats}\n"
    lines = []
    with open("shows.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if str(ShowId) in line:
                return f"Show with id:{ShowId} already exists."
            else:
                with open("shows.txt", "a") as file:
                    file.write(show_details)
                    return "Show Added Successfully"

#function to view shows
def viewshows():
    if os.path.exists("shows.txt"):
        with open("shows.txt", "r") as file:
            shows = file.read()
            if shows:
                return shows
            else: 
                return "No shows available"

    else:
        return "No Shows File"
    
#function to search show
def searchshow(MovieId):
    if os.path.exists("shows.txt"):
        with open("shows.txt", "r") as file:
            for line in file:
                if str(MovieId) in line:
                    b = line.strip()
                else:
                    b = "Show Not Found"
            return b    
    else: 
        return"No Shows File"

#function to Update show
def updateshow(ShowId, MovieId, Date, Time, Screen, Seats):
    lines = []
    if os.path.exists("shows.txt"):
        with open("shows.txt", "r") as file:
            lines = file.readlines()

        for line in range(len(lines)):
            if str(MovieId) in lines[line] and str(ShowId) in lines[line]:
                lines[line] = f"{ShowId}, {MovieId}, {Date}, {Time}, {Screen}, {Seats}"                  
                with open("shows.txt", "w") as file:
                    file.writelines(lines)
                    return "Show Updated"
            else:
                return "Show Not Found"
    else:
        return "No Shows File"


#function to delete a show
def delestshow(id):
    lines = []
    show_found = False
    if os.path.exists("shows.txt"):
        with open("shows.txt", "r") as file:
            lines = file.readlines()

        with open("shows.txt", "w") as file:
            for line in lines:
                if str(id) not in line:
                    file.write(line)
                else:
                    show_found = True 
        
            if show_found:
                return "Show Deleted"
            else:
                return "show not Found"
    else:
        return "No Shows File"
    


# BOOKINGS

#function to book a ticket
def bookticket(BookingId, ShowId, Customer_Name, Customer_Contact, Tickets):
    lines = []
    lines1 = []
    if os.path.exists("shows.txt"):
        with open("shows.txt", "r+") as file:
            lines = file.readlines()
            for line in lines:
                if str(ShowId) in line:
                    MovieId = line.split(",")[1].split(" ")
                    Date = line.split(",")[2].split(" ")
                    Time = line.split(",")[3].split(" ")
                    Screen = line.split(",")[4].split(" ")
                    seat_update = line.split(",")[5].split(" ")
                    seat_update = int(seat_update)
                    if seat_update >= int(Tickets):
                        with open("bookings.txt", "r") as file1:
                            lines1 = file1.readlines()
                            for line1 in lines1:
                                if str(BookingId) in line1:
                                    return f"Booking with id: {BookingId}already exists"
                                else:
                                    with open("bookings.txt", "a") as file1:
                                        file1.write(f"{BookingId}, {ShowId}, {Customer_Name}, {Customer_Contact},{Tickets}")
                                        seats = seat_update - Tickets
                                        updateshow(ShowId, MovieId, Date, Time, Screen, seats)
                                        return "Tickets Booked"
                    else:
                        return "Seats Not Available"
                
            return "Show Not Available"
                    
    else:
        return "No Shows File"

#function to view bookings
def viewbookings():
    if os.path.exists("bookings.txt"):
        with open("bookings.txt", "r") as file:
            bookings = file.read()
            if bookings:
                return bookings
            else:
                return "No Bookings"
            
    else:
        return "No Bookings File"
#function to cancel bookings
def cancelbooking(BookingId):
    lines = []
    booking_found = False
    if os.path.exists("bookings.txt"):
        with open("bookings.txt", "r") as file:
            lines = file.readlines()
        
        with open("bookings.txt", "w") as file:
            for line in lines:
                if str(BookingId) not in line:
                    file.write(line)
                else:
                    booking_found = True

            if booking_found:
                return "Booking Cancelled"
            else:
                return "Booking Not Found"
    else:
        return "No Bookings File"
#function to view seats
def viewseats():
    shows = []
    if os.path.exists("shows.txt"):
        with open("shows.txt", "r") as file:
            shows = file.read()
            num = 0
            for show in shows:
                seats = show.split(",")[5].split(" ")
                num += 1
                return f"Seats in Movie {num}: {seats}"
    else:
        return "No Shows File"
    

def admin(password):
    admin_p = "admin123"
    if password == admin_p:
        return True
    else:
        return False


def main():
    print("Are you a user or admin:\n For user enter 1 \n For admin enter 2\n")
    role = int(input("Enter your choice(1 or 2):"))
    if role == 2:
        pw = input("Enter admin password:")
        login_status = admin(pw)
        if login_status == True:
            print(f'''What do you want? 
            1-Add a Movie      2-View a Movie
            3-Update a Movie   4-Delete a Movie
            5-Search a Movie   6-Add show 
            7-View show        8-Search Show
            9-Update a Show    10-Delete a Show
            11-Book a ticket   12-View Booking
            13-Cancel Booking  14-View  seats
            15-Exit ''')
            while(True):
                choice =int(input("Enter your choice:"))
                if choice == 1:
                    print(addmovie(input("Enter movie id:"),input("Enter movie title:"),input("Enter movie genre:"),input("Enter movie language:"),input("Enter movie duration:"),int(input("Enter movie ticket:"))))
                elif choice == 2:
                    print(viewmovies())
                elif choice == 3:
                    print(updatemovie(input("Enter movie id:"),input("Enter movie title:"),input("Enter movie genre:"),input("Enter movie language:"),input("Enter movie duration:"),int(input("Enter movie ticket:"))))
                elif choice ==4:
                    print(deletemovie(input("Enter movie id:")))
                elif choice == 5:
                    print(searchmovie(input("Enter movie id:")))
                elif choice == 6:
                    print(addshow(input("Enter movie id:"),input("Enter movie title:"),input("Enter a Data:"),input("Enter a time :"),input("Enter a screen :"),int(input("Enter a seats:"))))
                elif choice ==7:
                    print(viewshows())
                elif choice == 8:
                    print(searchshow(input("Enter movie id:")))
                elif choice == 9:
                    print(updateshow(input("Enter Show Id:"), input("Enter Movie Id:")), input("Enter Date:"), input("Enter Time:"), input("Enter Screen:"), int(input("Enter Seats:")))
                elif choice == 10:
                    print(delestshow(input("Enter Show Id:")))
                elif choice == 11:
                    print(bookticket(
                        input("Enter Booking Id:"),
                        input("Enter Show Id:"),
                        input("Enter Customer Name:"),
                        input("Enter Customer Contact:"),
                        int(input("Enter Number of Tickets:"))
                    ))
                elif choice == 12:
                    print(viewbookings())
                elif choice == 13:
                    print(cancelbooking(input("Enter Booking Id:")))
                elif choice == 14:
                    print(viewseats())
                elif choice == 15:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Wrong password")
    if role == 1:
        print(f'''What do you want? 
            1-View a Movie  2-Search a Movie
            3-View show     4-Search Show   
            5-Book a ticket 6-Cancel Booking 
            7-View  seats   8-Exit 
                 ''')
        while True:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print(viewmovies())
            elif choice == 2:
                print(searchmovie(input("Enter movie ID:")))
            elif choice == 3:
                print(viewshows())
            elif choice == 4:
                print(searchshow(input("Enter movie ID:")))
            elif choice == 5:
                print(bookticket(
                    input("Enter booking ID:"),
                    input("Enter show ID:"),
                    input("Enter customer name:"),
                    input("Enter customer contact:"),
                    int(input("Enter number of tickets:"))
                ))
            elif choice == 6:
                print(cancelbooking(input("Enter booking ID:")))
            elif choice == 7:
                print(viewseats())
            elif choice == 8:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

main()