public class Cafe {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly";
        String readyMessage = ", your order is ready";
        String displayTotalMessage = "Your total is $";
        
        // Menu variables (add yours below)
        double mochaPrice = 3.5;
        // Drink Place
        double dipCoffe=2.5;
        int latte=5;
        int cappuchino = 10;

        // Customer name variables (add yours below)
        String customer1 = "Cindhuri";
        String customer2 = "Sam";
        String customer3 = "Jimmy";
        String customer4 = "Noah";

        // Order completions (add yours below)
        boolean isReadyOrder1 = true;
        boolean isReadyOrder2 = false;
        boolean isReadyOrder3 = false;
        boolean isReadyOrder4 = false;

        // APP INTERACTION SIMULATION (Add your code for the challenges below)
        // Example:
        System.out.println(generalGreeting + customer1); // Displays "Welcome to Cafe Java, Cindhuri"
    	if(isReadyOrder1) {
            System.out.println(dipCoffe+"\n enjoy");
            System.out.println("total "+dipCoffe);
        }
        System.out.println(generalGreeting + customer2);
        if(isReadyOrder2) {
            System.out.println(cappuchino+"\n enjoy");
            System.out.println("total "+cappuchino);
        }
        System.out.println(generalGreeting + customer3);
        if(isReadyOrder3) {
            System.out.println(latte*2"\n enjoy");
            System.out.println("here is ur price total "+latte*2);
        }
        System.out.println(generalGreeting + customer4);
        if(isReadyOrder4) {
            System.out.println(dipCoffe+"\n enjoy");
            System.out.println("total "+dipCoffe);
        }
        // else {
        //     System.out.println("Have fun!");
        // }
        
        
        // ** Your customer interaction print statements will go here ** //
    }
}
