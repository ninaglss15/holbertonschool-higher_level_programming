const element = document.getElementById("red_header");
const header = document.querySelector("header");

function addClass() {
    header.classList.add("red")
}
element.addEventListener("click",addClass);