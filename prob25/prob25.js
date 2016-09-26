function time_difference(s,e) {
	return (e - s) / 1000 // sec
}

var start = new Date(2013, 1, 1,  16, 10);
var end = new Date(2013, 1, 1, 17, 10);

var dif = time_difference(start,end)


document.write(dif)
