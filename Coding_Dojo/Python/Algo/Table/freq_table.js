function duplicate(str) {
    var charCount = make(str);
    var result = "";

    for (var i = 0; i < charCount.length; i++) {
        if (charCount[i].value > 1) {
            charCount[i].value = 1;
            result += charCount[i].key;
        }
    }

    return result;
}

function make(str) {
    var charCount = {};

    for (var i = 0; i < str.length; i++) {
        var char = str[i];
        charCount[char] = (charCount[char] || 0) + 1;
    }

    var result = [];

    for (var key in charCount) {
        result.push({ key: key, value: charCount[key] });
    }

    return result;
}

console.log(duplicate("aabbcc"));

str=""
