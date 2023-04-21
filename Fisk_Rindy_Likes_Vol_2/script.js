console.log("page loading...");

var likes_Count1 = 9;
var likeSpan1 = document.querySelector("#post1");

function like1() {
    likes_Count1++;
    likeSpan1.innerHTML = likes_Count1 + "like(s)";
}

var likes_Count2 = 12;
var likeSpan2 = document.querySelector("#post2");

function like2() {
    likes_Count2++;
    likeSpan2.innerHTML = likes_Count2 + "like(s)";
}

var likes_Count3 = 9;
var likeSpan3 = document.querySelector("#post3");

function like3() {
    likes_Count3++;
    likeSpan3.innerHTML = likes_Count3 + "like(s)";
}

var likes_Count4 = 9;
var likeSpan4 = document.querySelector("#post4");

function like4() {
    likes_Count4++;
    likeSpan4.innerHTML = likes_Count4 + "like(s)";
}