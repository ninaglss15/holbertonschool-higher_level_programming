const element = document.getElementById("red_header");
element.addEventListener("click",updateColor);

function updateColor() {
    element.style.color = "#FF0000"
}