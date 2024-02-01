public class BankAccount {
    // MEMBER VARIABLES
    private double checkingBalance;
    private double savingsBalance;

    private static int accounts;
    private static double totalMoney; // refers to the sum of all bank account checking and savings balances

    // CONSTRUCTOR
        public int addAccounts() {
            return this.accounts=accounts+1;
        }
    // GETTERS
    // for checking, savings, accounts, and totalMoney
    public double getCheckingBalance() {
        return this.checkingBalance;
    }
    public double getSavingsBalance() {
        return this.savingsBalance;
    }
    public int getAccounts() {
        return this.accounts;
    }
    public double getTotalMoney() {
        return this.totalMoney;
    }


    // METHODS
    // deposit
    public double deposit(double amount) {
        return this.totalMoney+=amount;

    }


    // - users should be able to deposit money into their checking or savings account


    public double depositUserChechking (double ammount){
        return this.checkingBalance+=ammount;

    }

    public double depositUserSaving (double ammount){
        return this.savingsBalance+=ammount;
    }
    // withdraw 
    public double withdraw(double amount) {
        return this.totalMoney-=amount;

    }


    // - users should be able to withdraw money from their checking or savings account


    public double withdrawUserChecking(double amount) {
        if (amount > checkingBalance) {
            System.out.println("Insufficient funds");
            return -1; // Indicate failure to withdraw due to insufficient funds
        } else {
            checkingBalance -= amount;
            totalMoney-=amount;
            return checkingBalance; // Return the updated balance after withdrawal

        }
    }
    

    public double withdrawUserSavin(double amount) {
        if (amount > checkingBalance) {
            System.out.println("Insufficient funds");
            return -1; // Indicate failure to withdraw due to insufficient funds
        } else {
            savingsBalance -= amount;
            totalMoney-=amount;
            return savingsBalance; // Return the updated balance after withdrawal

        }
    }

    // - do not allow them to withdraw money if there are insufficient funds


    // - all deposits and withdrawals should affect totalMoney
    // getBalance
    // - display total balance for checking and savings of a particular bank account
}