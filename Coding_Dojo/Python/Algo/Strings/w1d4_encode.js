const str1="aaaabbcddd"
const expected1="a4b2cd3"
var  count=0

for (var i=1;i<str1.length;i++){
    if (str1[0]==str1[i]){
        count++
    }
    
}
console.log(str1[0]+count)


function encodeStr(str){
    // 1) declare & intialize variables
    // ? count =1
    //* look though the string (start i=0; i<len ; i++)
    // on each iteration : 
    // if the current char is equal to the next
    //! increment the count
    var new_str=""
    var count=1
    for (var i=0;i<str.length;i++){
        if (str[i]===str[i+1]){
            count+=1;

        }else{
            if (count===1){
                new_str+=str[i]
            }else {
                new_str+=str[i]+count
            }l
            count=1;
        }
    }

if (new_str.length>str.length){


return str}else{
    return new_str
}l
}
console.log(encodeStr("bbcc"))

