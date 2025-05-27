var a = "外部引用";
document.getElementById("demo").innerHTML = a;

const myObj = {
  name:"John",
  age:30,
  myCars: {
    car1:"Ford",
    car2:"BMW",
    car3:"Fiat"
  }
}

document.getElementById("demo").innerHTML = myObj.name + " " + myObj.age + " " + myObj.myCars.car1 + " " + myObj.myCars.car2 + " " + myObj.myCars.car3;