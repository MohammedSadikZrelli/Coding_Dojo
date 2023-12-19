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
        console.log(" name:",this.name," strength: ",this.strength ,"speed : ", this.speed, 'health :',this.health)
    }
    drinkSake(){
        this.health+=10;
    }
}

const ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
ninja1.showStats();
ninja1.drinkSake();



// create my own ninjas


class Ninjas{
    constructor(name,health,speed,strength){
       this.name=name
       this.health= health
       this.speed=speed
       this.strength=strength


    }
    sayName(){
        console.log(this.name)
    }
    showStats(){
        console.log(" name:",this.name," strength: ",this.strength ,"speed : ", this.speed, 'health :',this.health)
    }
    drink(){
        this.health+=10
    }
}
const SamuraiSadikwitheBlackCaP= new Ninjas ("Zdig","365HP","Can't Catch Him","Thor")

SamuraiSadikwitheBlackCaP.sayName();
SamuraiSadikwitheBlackCaP.showStats();
