function divide(n1,n2){
  try{
    if(n2 == 0){
      throw("Divide by zero error.");
    }else{
      return n1/n2;
    }
  }
  catch(e){
    alert("Error:" +e)
  }
}

var num1=200
var num2=2

document.write(divide(num1,num2))
