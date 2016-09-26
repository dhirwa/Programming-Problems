function oneMissing(arr) {

  var sortedArray = arr.slice(0).sort(function(a, b) {return a - b;});

  var missing = sortedArray.filter(function(num, i){
    return sortedArray[i+1] - num > 1;
  }).map(function(num){
    return num +1;
  });

  return missing;


}
