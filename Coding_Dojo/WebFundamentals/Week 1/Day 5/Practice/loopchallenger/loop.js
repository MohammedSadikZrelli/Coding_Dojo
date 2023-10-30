//Using a loop write code that will console.log all of the odd values from 1 up to 20.
function log(){
    for(var i=1;i<=20;i++){
      console.log(i)

    }
}
log();

//Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0.
function div3(){
    for(var i=100;i=>0;i--){
     if (i%3==0){
        console.log(i);
     }

    }
}

// Using a loop write code that will console.log the values in this sequence 4, 2.5, 1, -0.5, -2, -3.5.
function seq(){
    for (var i=4;i>=-3,5;i-=1.5){
        console.log(i)

}

}

// Write code that will add all of the values from 1-100 onto some variable sum and at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100. We should get back 5050 at the end.
 function some(){
  var some=0;
    for (var i=1;i<101;i++){
   som+=i;

  }

 }
 // Write code that will multiply all of the values from 1-12 onto some variable product and at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end.
 function mult(){
    var some=1;
      for (var i=1;i<13;i++){
     som*=i;
      }
    }