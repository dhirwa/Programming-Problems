function spiral(array){
  test=[];
  for(var i=1;i<=array.length;i++){
    for(var j=1; j<=i;j++){
      test.push(j);
    }
  }
  return test;
}

var arr=[[1,2,4],[3,9,8],[5,7,6]];
document.write(spiral(arr));
