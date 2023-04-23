
    var crustType =  ["Chicago Style", "Hand Tossed", "St. Louis Style/Cracker", "New York Style", "Cornmeal Crust"];
    var sauceType =  ["Robust Tomato", "Olive Oil", "BBQ", "Cream"];
    var cheese =    ["Mozzarella", "Feta", "Feet Cheese/Rubber (Provel)", "Parmesan Reggiano"];
    var toppings =  ["Mushrooms", "Sausage", "Basil", "Tomato", "Pepperoni", "Chicken", "Spinach"];

function pizzaOven(crustType, sauceType, cheese, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheese = cheese;
    pizza.toppings = toppings;
    return pizza;
}

var pizza1 = pizzaOven("Chicago Style", "Robust Tomato", "Mozzarella", ["Sausage", "Mushroom", "Basil"]);
console.log(pizza1);

var pizza2 = pizzaOven("Hand Tossed", "Olive Oil", ["Mozzarella", "Feta"], ["Pepperoni", "Sausage"]);
console.log(pizza2);

var pizza3 = pizzaOven("St. Louis Style/Cracker", "Robust Tomato", "Feet Cheese/Rubber (Provel)", ["Pepperoni", "Mushroom"]);
console.log(pizza3);

var pizza4 = pizzaOven("New York Style", "Cream", ["Mozzarella", "Parmesan Reggiano"], ["Chicken", "Tomato", "Basil", "Mushroom"]);
console.log(pizza4);


function randomRange(max, min) {
    return Math.floor(Math.random() * max - min) + min;
}

function randomPick(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomPizza() {
    var pizza = {};
    pizza.crustType = randomPick(crustType);
    pizza.sauceType = randomPick(sauceType);
    pizza.cheese = [];
    pizza.toppings = [];
    for(var i=0; i<randomRange(5, 1); i++) {
        pizza.cheese.push(randomPick(cheese));
    }
    for(var i=0; i<randomRange(4, 0); i++) {
        pizza.toppings.push(randomPick(toppings));
    }
    return pizza;
}

console.log(randomPizza());