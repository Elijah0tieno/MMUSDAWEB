let eventBox = document.querySelector(".event-box")

let moreBtn = document.querySelectorAll(".more-details")
moreBtn.forEach(item => {
    item.addEventListener("click", () => {
        // item.parentElement.classList.toggle("showMoreDetails")
        firstParent = item.parentElement
        secondParent = firstParent.parentElement
        secondParent.classList.toggle("showMoreDetails")
        // let btnText = document.querySelector(".btnText")
        let btnText = item.firstElementChild;
        // console.log(btnText)

        if(btnText.innerText === "More"){
            btnText.innerText = "Less"
        }
        else{
            btnText.innerText = "More"
        }
    })
})
console.log(moreBtn)