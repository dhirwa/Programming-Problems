function getdisc(total,perc){

    if(perc > 100 || perc < 0){
      console.log("invalid percentage");
    }
    else{
      return total * (perc*0.01);

    }
}
console.log("the discount is "+ getdisc(100,10));
