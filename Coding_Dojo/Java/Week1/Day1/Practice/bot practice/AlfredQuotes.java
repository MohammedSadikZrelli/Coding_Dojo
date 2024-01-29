import java.util.Date;

public class AlfredQuotes {

    public String basicGreeting() {
        // You do not need to code here, this is an example method
        return "Hello, lovely to see you. How are you?";
    }

    public String guestGreeting(String name) {
        return "hi" + name + "how you doing";
    }

    public String dateAnnouncement() {
        Date currentDate = new Date();
        return "it is currently " + currentDate;
    }

    public String respondBeforeAlexis(String conversation) {
        int index = conversation.indexOf("Alexis");
        int indexAlfred = conversation.indexOf("Alfred");
        if (index != -1) {
            return "Right away, sir. She certainly isn't sophisticated enough for that" + index;
        } else if (indexAlfred !=-1) {
           return "At your service. As you wish, naturally";
        }
        return "Right. And with that I shall retire";
    }

    // NINJA BONUS
    // See the specs to overload the guestGreeting method
    // SENSEI BONUS
    // Write your own AlfredQuote method using any of the String methods you have
    // learned!
}
