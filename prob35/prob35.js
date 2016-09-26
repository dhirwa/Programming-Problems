function exOh(str) {
  var arr = str.split('');
  var ex = filtered(arr, 'x');
  var oh = filtered(arr, 'o');
  if (ex.length === oh.length) {
    return true;
  } else {
    return false;
  }
}

function filtered(arr, value) {
  return arr.filter(function(char) {
    return char.toLowerCase() === value;
  });
}

console.log(exOh('xooxxo'));
console.log(exOh('x'));
console.log(exOh('XoOx'));
