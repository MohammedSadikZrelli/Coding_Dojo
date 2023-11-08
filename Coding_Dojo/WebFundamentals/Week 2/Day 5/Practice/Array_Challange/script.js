// exercice 1

var x="yummy "
var count=0;
function alwaysHungry(arr) {
    for (var i=0;i<arr.length;i++){
    if(arr[i]=="food"){
      count++
    }
        
}
if (count>0){


console.log(x.repeat(count)) }
else {
    console.log("i am hungry")
}

}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);

alwaysHungry([4, 1, 5, 7, 2]);

// exercise 2 


function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i=0;i<arr.length;i++)
    if (arr[i]>cutoff){
        filteredArr.push(arr[i])
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); 


// exerice 3

function betterThanAverage(arr) {
    var sum = 0;
    var aver=0;
    for(var i=0;i<arr.length;i++){
        sum+=arr[i] 
    }
    var avg=sum/arr.length
    var count = 0
    for(var i=0;i<arr.length;i++){
        if (arr[i]>avg){
            count++;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4

// 

// exerice 4 

function reverse(arr) {
    
        arr.reverse()

    
    return arr;
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]



//exercice 5 
function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for (var i = 2; i <= n; i++) {
        var nextFib = fibArr[i - 1] + fibArr[i - 2];
        fibArr.push(nextFib);
}
return fibArr;
}
var result = fibonacciArray(10);
console.log(result); 
