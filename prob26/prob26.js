function TimeConvert(num) {
	hours = Math.floor(num / 60);
	minutes = num % 60;
	return hours + ":" + minutes;
}

document.write(TimeConvert(103) + "<br>")
document.write(TimeConvert(516) + "<br>")
