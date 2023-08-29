// Play Heroes and Villains
var h_and_v = document.getElementById("h_and_v");

function play_h_and_v() {
    h_and_v.play();
}

function pause_h_and_v() {
    h_and_v.pause();
}
// End of Play Heroes and Villains

// Play Game Vault
var game_vault = document.getElementById("game_vault");

function play_game_vault() {
    game_vault.play();
}

function pause_game_vault() {
    game_vault.pause();
}
// End of Play Game Vault

// Hover event
function scale(element, value) {
    element.style.transform = "scale(" + value + ")";
}

// Clock
function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() +
      new Date().getMinutes() * 60 +
      new Date().getHours() * 3600;
}

function getHourHandAngle(s) {
    s %= 43200; // seconds in 12 hours
    return ((360 * s / 43200) + 180) % 360;
}

function getMinuteHandAngle(s) {
    s %= 3600; // seconds in an hour
    return ((6 * s / 60) + 180) % 360;
}

function getSecondHandAngle(s) {
    s %= 60; // seconds in a minute
    return ((6 * s) + 180) % 360;
}

const hour = document.getElementById("hour");
const minutes = document.getElementById("minutes");
const seconds = document.getElementById("seconds");

setInterval( () => {
    let s = getSecondsSinceStartOfDay();
    hour.style.transform = `rotate(${getHourHandAngle(s)}deg)`;
    minutes.style.transform = `rotate(${getMinuteHandAngle(s)}deg)`;
    seconds.style.transform = `rotate(${getSecondHandAngle(s)}deg)`;
}, 1000);
// End of Clock


// Calculator
const display = document.getElementById("display");
let num1 = "";
let num2 = "";
let op = "";


function press(num) {
    num1 += num;
    display.innerHTML = num1;
}

function setOP(key) {
    op = key;
    num2 = num1;
    num1 = "";
}

function clr() {
    num1 = "";
    num2 = "";
    op = "";
    display.innerHTML = "0";
}

function calculate() {
    let a = parseFloat(num2);
    let b = parseFloat(num1);
    let res = 0;
    switch(op) {
    case "+":
        res = a + b;
        break;
    case "-":
        res = a - b;
        break;
    case "*":
        res = a * b;
        break;
    case "/":
        res = a / b;
        break;
}
    num1 = res;
    op = "";
    display.innerHTML = res;
}
// End of Calculator