
import java.util.List;

public class Booking {

    public List<Events> events;
    public List<Movies> movies;
    private String seats;
    private double price;
    private int quantity;

    public Booking(List<Events> events, List<Movies> movies, double price, int quantity, String seats) {
        this.events = events;
        this.movies = movies;
        this.price = price;
        this.quantity = quantity;
        this.seats = seats;
    }

    
    public List<Events> getEvents() {
        return events;
    }
    public void setEvents(List<Events> events) {
        this.events = events;
    }
    public List<Movies> getMovies() {
        return movies;
    }
    public void setMovies(List<Movies> movies) {
        this.movies = movies;
    }
    public String getSeats() {
        return seats;
    }
    public void setSeats(String seats) {
        this.seats = seats;
    }
    public double getPrice() {
        return price;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "Purchase History: \nEvents: " + events + "\nMovies: " + movies + "\nSeats: " + seats + "\nPrice: " + price + "\nQuantity: " + quantity;
    }







}
