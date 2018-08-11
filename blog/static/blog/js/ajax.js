$(function(){
	$('#search').keyup(function(){	
		if ($('#search').val().length > 0)
			$('#search-results').css('display', 'block');
		else
			$('#search-results').css('display', 'none');
		
		$.ajax({
			type: 'POST',
			url: '/search-title/',
			data: {
				'search_text': $('#search').val(),
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});

	var likes = document.getElementsByClassName('like-btn');
	
	for(var i = 0; i < likes.length; i++){
	   likes.item(i).click = new function() { like_post(likes.item(i), false) };	
	}
});

function searchSuccess(data, textStatus, jqXHR){
	$('#search-results').html(data);
}

function like_post(post, bool) {
    var post_id = post.getAttribute('data-post-id');
	
	$.ajax({
		type: 'POST',
		url: '/like-post/',
		data: {
			'post_id': post_id,
			'user_ip': user_ip,
			'update': bool,
			'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function(data, textStatus, jqXHR){
			$('#like-btn-' + post_id).html(data)
		},
		dataType: 'html'
	});
}