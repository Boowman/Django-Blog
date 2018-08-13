/*
	Hiding the search box when clicking anywhere on the page
*/
$(document).on('click','body *',function(){
	var y = document.getElementById('search-results');
	if(y.style.display == 'block')
		y.style.display = 'none';
	else
		console.log('no visible');

});