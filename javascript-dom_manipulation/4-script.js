const element = document.getElementById("add_item");
const myList = document.getElementsByClassName("my_list")[0];

function addLi() {
    myList.innerHTML += "<li>Item</li>";
}
element.addEventListener("click",addLi);