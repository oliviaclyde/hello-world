// Javascript file for index.html
// Using the dog API : https://dog.ceo/dog-api/documentation


// List all breeds: get a list of all the breeds from the Dog API and output to the page






//Retrieve random dog picture and display on webpage
function GetRandomDog() {
    $.ajax({
        type: 'GET',
        url: 'https://dog.ceo/api/breeds/image/random',
        success: function(response) {
            //Logged to console for debugging to validate connection
            // console.log(response);
            $('#dog').attr("src", response.message);
        },
        error: function(data) {
            let errorMessage = ("No connection. Please check the url and try again.");
            alert(errorMessage);    
        } 

    });
}

function RateDog() {
    let myMessage = ("Stay tuned! This feature coming soon!");
    alert(myMessage);
//Add'l development needed. Save dog rating to local storage and display on Dashboard page w/ rating
// POST request w/ my local url?
}

$(document).ready(function() {
    //This will give an inital picture on page load but will also give new picture on page refresh. 
    GetRandomDog();
});
