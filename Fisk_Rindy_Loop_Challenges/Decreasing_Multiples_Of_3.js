
/* 2. Decreasing Multiples of 3
Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0. */

for(var i = 100; i >= 1; i--) {
    if(i % 3 == 0) {
        console.log(i);
    }
}