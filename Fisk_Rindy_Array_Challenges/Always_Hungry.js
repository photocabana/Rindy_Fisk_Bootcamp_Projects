
/* 1. Always Hungry
Write a function that is given an array and each time the value is "food" it should console log "yummy". If "food" was not present in the array console log "I'm hungry" once.*/


function alwaysHungry(arr) {
    var foodAmount = 0;
    for(var i = 0; i <= Arr.length; i++) {
        if(arr[i] == "food") {
            console.log("yummy");
            foodAmount++;
        }
    }
    if(foodAmount == 0) {
        console.log("I'm hungry")
    }
}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);
// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"
