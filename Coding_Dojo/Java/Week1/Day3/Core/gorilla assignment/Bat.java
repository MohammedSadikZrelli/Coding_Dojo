public class Bat extends Mammal {
    public Bat(int energy) {
        this.energy = 300; // Set Bat's energy level to the provided value
    }

    public void fly() {
        this.energy -= 50;
        System.out.println("Bat is flying so high");
    }

    public void eatHuman() {
        this.energy += 25;
        System.out.println("Bat: Tasty human! I love it.");
    }

    public void attackTown() {
        this.energy -= 100;
        System.out.println("Bat: Wooah, the town got destroyed! Damn!");
    }
}
