
public class Test{

    public static void main(String []args){
        Mammal mami = new Mammal();

        mami.displayEnergy();
        Gorilla GadGoud = new Gorilla(150); // Create a Gorilla object with energy level 150
        GadGoud.throwSomething();
        GadGoud.displayEnergy();
        GadGoud.eatBananas();
        GadGoud.displayEnergy();
        Bat sousou = new Bat(300);
        sousou.eatHuman();
        sousou.displayEnergy();
        sousou.attackTown();
        sousou.displayEnergy();

    }
    
}