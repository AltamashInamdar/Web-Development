// Hosting = 
//          Variable Hosting
//          Function Hosting


// Function Call Back Stack=(stack=Data Structure)
function MyGreed(Greed,FullName){
    console.log("Hellow",FullName)
    Greed()
}
 function Greed (){
    console.log("Kese Hoo")
}
MyGreed(Greed,"Altamash")