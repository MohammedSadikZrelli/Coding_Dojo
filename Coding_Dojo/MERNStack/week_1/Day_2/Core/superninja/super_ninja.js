class Ninja{
    constructor(name,health,speed,strength){
       this.name=name
       this.health= 90
       this.speed=3
       this.strength=3


    }
    sayName(){
        console.log(this.name)
    }
    showStats(){
        console.log("name;", this.name, "strength;" ,this.strength , "speed;"  , this.speed, 'health; ',this.health)
    }
    drinkSake(){
        this.health+=10;
    }
}

const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.showStats();
ninja1.drinkSake();


class Sensei extends Ninja {
    constructor(name,wisdom = 10) {
        super(name);
        this.wisdom=wisdom
    }
    speakWisdom(){
        console.log("What one programmer can do in one month, two programmers can do in two months.", this.wisdom)
    }
}
const superSensei = new Sensei("Master Splinter");
superSensei.speakWisdom();
superSensei.showStats();