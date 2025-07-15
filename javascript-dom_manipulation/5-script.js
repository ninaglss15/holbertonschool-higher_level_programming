const element = document.getElementById("update_header");
const header = document.querySelector("header");

function updateText() {
    header.textContent = "New Header!!!";
}

element.addEventListener("click", updateText);