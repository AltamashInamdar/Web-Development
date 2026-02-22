// Class 

class human {
    // Properties
    age=10;
    #name="Altamash"
    ht=110

    // Behavior
    Walk(){
        console.log("I Am A Walk:", this.#name)
    }
    Run(){
        console.log("I Am A Run")
    }
}

let obj = new human();
console.log(obj.age)
obj.Walk()