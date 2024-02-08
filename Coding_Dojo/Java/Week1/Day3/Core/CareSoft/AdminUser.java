import java.util.ArrayList;
import java.util.Date;

public class AdminUser extends User implements HIPAACompliantUser, HIPAACompliantAdmin {
    private Integer employeeID;
    private String role;
    private ArrayList<String> securityIncidents;
    private int pin;

    public AdminUser(Integer id, String role) {
        this.employeeID = id;
        this.role = role;
        this.securityIncidents = new ArrayList<>();
    }

    @Override
    public boolean assignPin(int pin) {
        if (String.valueOf(pin).length() >= 6) {
            this.pin = pin;
            return true;
        } else {
            return false;
        }
    }

    @Override
    public boolean accessAuthorized(Integer confirmedAuthID) {
        if (!confirmedAuthID.equals(this.employeeID)) {
            authIncident();
            return false;
        } else {
            return true;
        }
    }

    @Override
    public ArrayList<String> reportSecurityIncidents() {
        return this.securityIncidents;
    }

    public void authIncident() {
        String report = String.format("Datetime: %s\n", new Date());
        report += String.format("Id: %s\n", this.employeeID);
        report += "Notes: Authorization failed for this user\n";
        securityIncidents.add(report);
    }

    public Integer getEmployeeID() {
        return this.employeeID;
    }

    public void setEmployeeID(Integer id) {
        this.employeeID = id;
    }

    public String getRole() {
        return this.role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public ArrayList<String> getSecurityIncidents() {
        return this.securityIncidents;
    }

    public void setSecurityIncidents(ArrayList<String> securityIncidents) {
        this.securityIncidents = securityIncidents;
    }
}
