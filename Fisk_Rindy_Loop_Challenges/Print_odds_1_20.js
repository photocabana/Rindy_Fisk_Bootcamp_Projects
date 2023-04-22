
/* 1. Print odds 1-20
Using a loop write code that will console.log all of the odd values from 1 up to 20.*/

for(i = 0; i <= 20; i++) {
    if(i % 2 != 0) {
        console.log(i);
    }
}

for(var i = 1; i <= 20; i += 2) {
    console.log(i);
}