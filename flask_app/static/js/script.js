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