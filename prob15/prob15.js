function createTriangle(num) {
  var line = '';
  var i = 0;
  while (i < num) {
    line += "#";
    console.log(line);
    i++;
  }
}

console.log(createTriangle(10));
