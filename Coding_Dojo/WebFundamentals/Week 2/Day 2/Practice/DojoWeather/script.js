y=document.querySelector(".cookie-box")
function x(){

y.remove();

}

function convertTemperature() {
    // Get the selected temperature scale (Celsius or Fahrenheit)
    var degreeSelect = document.getElementById("degree");
    var selectedOption = degreeSelect.options[degreeSelect.selectedIndex].value;

    // Get all the temperature elements with class "f" or "s"
    var temperatureElements = document.querySelectorAll(".f, .s");

    // Loop through the temperature elements and convert the temperature
    temperatureElements.forEach(function(element) {
        var temperature = parseFloat(element.innerText);
        if (!isNaN(temperature)) {
            if (selectedOption === "fa") {
                // Convert from Celsius to Fahrenheit
                temperature = (temperature * 9/5) + 32;
            }
            else {
                // Convert from Fahrenheit to Celsius
                temperature = (temperature - 32) * 5/9;
            }
            element.innerText = temperature.toFixed(2); // Update the temperature text
        }
    });
}

// Function to be called when the "Accept" button is clicked
function accept() {
    // Your code to handle cookie acceptance
    // ...

    // Convert temperatures based on the selected temperature scale
    convertTemperature();
}

function ale(){
    alert("Loading Weather Report...")
}