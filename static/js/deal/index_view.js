$(document).ready(function(){
	$('.thumbs_wrapper a').click(function(){
		promo_id = parseInt($(this).parents('.thumbs_wrapper').attr('promo_id'));
		promo_vote = parseInt($(this).attr('promo_vote'));
		if ($.cookie('vote_'+promo_id) == undefined){			
		// }else{
			var elem = $(this);
			$.ajax({
				url: '/deal/vote/',
				type: 'POST',
				datatype:'jsonp',
				data: {'promo_id':promo_id, 'promo_vote':promo_vote},
				success: function(data, status){
					$.cookie('vote_'+promo_id, promo_vote);
					vote_points = elem.siblings('.vote_display');
					points = parseInt(vote_points.text()) + parseInt(promo_vote);
					vote_points.text(points);
					elem.addClass('color');
					elem.siblings('a').css({'opacity':0});
					color_points(vote_points);
				},
				error: function(){
					$('a.vote_login_prompt').hide();
					if(elem.siblings('a.vote_login_prompt').length == 0){
						elem.parent('div').append('<a href="/login/" class="vote_login_prompt">login here to vote</a>');
					}else{
						elem.siblings('a.vote_login_prompt').show();
					}
				}
			});
		}
	});

	$('.thumbs_wrapper').each(function(){
		var p_id = $(this).attr('promo_id');
		var cookie = $.cookie('vote_'+p_id);
		var active, inactive;
		if(cookie == 1){
			active = 'a.like_deal';
			inactive = 'a.dislike_deal';
		}else if(cookie == -1){
			active = 'a.dislike_deal';
			inactive = 'a.like_deal';
		}else{
			active = '-';
			inactive = '-';
		}
		$(this).find(active).addClass('color');
		$(this).find(inactive).css({'opacity':0,'visibility':'hidden'});
	});
});

function color_points(element){
	var points = parseInt(element.text());
	if(points > 0){
		element.addClass('like_deal');
		element.removeClass('dislike_deal');
	}else if(points == 0 ){
		element.removeClass('like_deal dislike_deal');
	}else if(points < 0){
		element.removeClass('like_deal');
		element.addClass('dislike_deal');
	}
}