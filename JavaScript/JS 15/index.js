// function changeText(){
//     let fpara = document.getElementById("fpara");
//     fpara.textContent="inamdar1"
// }
// let fpara = document.getElementById("fpara");
// fpara.addElement.listener('click',changeText);


// function changeText(event){
//     console.log(event)
// }

let anchorElement = document.getElementById("fanchor");
anchorElement.addEventListener("click",function(event){
    event.preventDefault();
    anchorElement.textContent="click done"
});

