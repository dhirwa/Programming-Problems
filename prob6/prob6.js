var randPrint=function(randomNumber){
  var list=[]
  if(randomNumber > 40){
    for(var i=40;i<randomNumber;i++){
          if (i % 2 !==0){
            list.push(i);
          }
    }
    return list.reverse();
  }

  else{
    for(var i=0;i<randomNumber;i++){
          if (i % 2 !==0){
            list.push(i);
          }
    }
    return list.reverse();
  }


};

var randomNumber=(Math.floor(Math.random()*100));

console.log("the number is "+randomNumber);
console.log("the list" + randPrint(randomNumber));
