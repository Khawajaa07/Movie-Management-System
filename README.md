# Movie Management System

This Movie Management System with functionalities for both users and admins. The system manages movies, shows, and bookings using text files to store data.

## Features

### Admin Functions:
- **Add a Movie**: Add a new movie to the system.
- **View Movies**: View all movies in the system.
- **Update a Movie**: Update movie details such as title, genre, language, etc.
- **Delete a Movie**: Remove a movie from the system.
- **Search a Movie**: Search for a movie by ID.
- **Add a Show**: Add a new show for a specific movie.
- **View Shows**: View all available shows.
- **Search a Show**: Search for a show based on movie ID.
- **Update a Show**: Update show details such as date, time, screen, and available seats.
- **Delete a Show**: Remove a show from the system.
- **Book a Ticket**: Admin can book tickets for customers.
- **View Bookings**: View all bookings made by customers.
- **Cancel Booking**: Cancel an existing booking.
- **View Seats**: View available seats for all shows.

### User Functions:
- **View Movies**: Users can view a list of all available movies.
- **Search a Movie**: Users can search for a movie by its ID.
- **View Shows**: Users can view all available shows.
- **Search a Show**: Users can search for shows based on movie ID.
- **Book a Ticket**: Users can book tickets for a specific show.
- **Cancel Booking**: Users can cancel an existing booking.
- **View Seats**: Users can check available seats for shows.

## Requirements

- Python 3.x
- Text files (`movies.txt`, `shows.txt`, `bookings.txt`) should be present in the same directory as the script to store data.

## How to Use

1. **Run the Program**: Execute the script. It will ask if you're a user or admin.
   
2. **Login as Admin**: If you choose to log in as an admin, you'll be prompted to enter the admin password (`admin123`).
   
3. **Login as User**: If you're a user, you can interact with movie listings, shows, and bookings.

4. **Choose an Option**: After logging in, select the action you want to perform by entering the corresponding number.

5. **Exit**: You can exit the program anytime by selecting the exit option.


### Admin Options:
- **Add a movie**: Add a new movie with its details (ID, title, genre, language, duration, ticket price).
- **View Movies**: List all movies stored in the system.
- **Update a Movie**: Update movie details.
- **Delete a Movie**: Remove a movie from the system.
- **Search a Movie**: Search for a movie by its ID.
- **Add a Show**: Create a new show for a specific movie with details such as date, time, screen, and available seats.
- **View Shows**: List all shows.
- **Update Show**: Modify show details (date, time, seats).
- **Delete Show**: Remove a show from the system.
- **Book a Ticket**: Admin can book tickets for customers.
- **View Bookings**: View all bookings made.
- **Cancel Booking**: Cancel a booking.
- **View Seats**: Check available seats for shows.


### User Options:
- **View Movies**: View a list of available movies.
- **Search a Movie**: Search for a movie by its ID.
- **View Shows**: View a list of all available shows.
- **Search a Show**: Search for shows by movie ID.
- **Book a Ticket**: Book tickets for a show.
- **Cancel Booking**: Cancel an existing booking.
- **View Seats**: View available seats for shows.


## Code Structure

1. **Movie Management**:
   - Add, view, update, search, and delete movies.

2. **Show Management**:
   - Add, view, update, search, and delete shows.

3. **Booking Management**:
   - Book tickets, view bookings, cancel bookings.

4. **Admin Authentication**:
   - Simple password check (`admin123`) to access admin functions.

## Notes

- The system doesn't currently handle edge cases such as invalid data types or empty file scenarios. Consider adding further validation and error handling for production use.




