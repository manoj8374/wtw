$(document).ready(function () {
let styleMeNow = document.getElementById("styleMeNow")
let home = document.getElementById("homeSection")
let formPart = document.getElementById("formPart")
let SubmitButton = document.getElementById("SubmitTheForm");
let wadrobeButton = document.getElementById("wadrobeButton");
let wadrobeSection = document.getElementById("wadrobeSection");
// let nextButton = document.getElementById("nextButton");
let suggestionSection = document.getElementById("suggestionSection");
let back = document.getElementById("back");


SubmitButton.addEventListener("click", (event) => {
    event.preventDefault()
    console.log("clicked");
    formPart.classList.add("formSection")
    suggestionSection.classList.remove("hideSection");
    fetch('http://')
})

wadrobeButton.addEventListener("click", () => {
    home.classList.add("hideSection");
    wadrobeSection.classList.remove("hideSection");
})

styleMeNow.addEventListener("click", () => {
    home.classList.add("hideSection");
    wadrobeSection.classList.remove("hideSection");
    formPart.classList.remove("formSection")
    wadrobeSection.classList.add("hideSection")
})

// back.addEventListener("click", ()=>{
//     window.location.reload();
// })
});