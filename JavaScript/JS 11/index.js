// Object And Cloning

//  1) Spread Operator

let src={
    age:10,
    wt:30,
    ht:120
}

let dest = {...src}

src.age=90

console.log(src)
console.log(dest)


//  2) Assign Method
let Scr ={
    age:20,
    wt:50,
    ht:1234
}

let Dest = Object.assign({},Scr)
 Scr.age=100;



console.log(Scr)
console.log(Dest)

