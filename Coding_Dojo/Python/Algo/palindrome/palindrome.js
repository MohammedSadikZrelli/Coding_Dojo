const str1="a*a"
const expected1=true;

const str2="racecar"
const expected2=true;

const str3="ese";
const expected3=false;

function palindrome(str){
    let len=str.length
    for (var i=0;i<len/2;i++){
        if (str[i]!==str[len-1-i]){
            return false 
        }

    }

    return true

}

console.log(palindrome(str3))