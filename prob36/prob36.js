function countZeros(array) {
	var count = 0;
	for (var i = 0; i < array.length; i++) {
		array[i] === 0 ? count++ : null;
	}
	return count;
}

console.log(countZeros([0,1,0,2,3]))
console.log(countZeros([0,1,0,0,0]))
console.log(countZeros([0]))
