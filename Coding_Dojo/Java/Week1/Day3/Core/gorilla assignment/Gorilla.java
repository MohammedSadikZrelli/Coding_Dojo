public class Gorilla extends Mammal {
    public Gorilla(int energy) {
        this.energy = energy; // Set Gorilla's energy level
    }

    public void throwSomething() {
        this.energy -= 5;
        System.out.println("Gorilla has thrown something");
    }

    public void eatBananas() {
        this.energy += 10;
        System.out.println("Gorilla: Oh baby, that feels good!");
    }

    public void climb() {
        this.energy -= 10;
        System.out.println("Gorilla: Climbing a tree");
    }
}
