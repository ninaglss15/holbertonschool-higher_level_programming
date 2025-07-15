const element = document.getElementById("toggle_header");
const header = document.querySelector("header");

function toggleClass() {
    if (header.classList.contains("green")) {
        header.classList.remove("green");
        header.classList.add("red");
    } else {
        header.classList.remove("red");
        header.classList.add("green");
    }
}

element.addEventListener("click", toggleClass);