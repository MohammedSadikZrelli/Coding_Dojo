import java.util.ArrayList;

public class CafeUtil {

    public double getOrderTotal(double[] prices) {
        double total = 0;
        for (double price : prices) {
            total += price;
        }
        return total;
    }

    public void displayMenu(ArrayList<String> menuItems) {
        for (int i = 0; i < menuItems.size(); i++) {
            System.out.printf("%d %s\n", i, menuItems.get(i));
        }
    }

    public void addCustomer(ArrayList<String> customers) {
        System.out.println("Please enter your name:");
        String username = System.console().readLine();
        System.out.println("Hello, " + username + "!");
        int peopleAhead = customers.size();
        System.out.println("There are " + peopleAhead + " people in front of you.");
        customers.add(username);
        System.out.println(customers);
    }
}