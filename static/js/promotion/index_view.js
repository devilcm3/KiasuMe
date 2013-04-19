$(document).ready(function(){
	$('.thumbs_wrapper > a').click(function(){
		promo_id = parseInt($(this).parent().attr('promo_id'));
		promo_vote = parseInt($(this).attr('promo_vote'));
		if ($.cookie('vote_'+promo_id)){
			
		}else{
			$.post('/promotion/vote/',{'promo_id':promo_id, 'promo_vote':promo_vote});
			$.cookie('vote_'+promo_id, promo_vote);
			vote_points = $(this).siblings('.vote_display');
			points = parseInt(vote_points.text()) + parseInt(promo_vote);
			vote_points.text(points);
			$(this).addClass('color');
			$(this).siblings('a').css({'opacity':0});
			color_points(vote_points);
		}
	});

	$('.thumbs_wrapper').each(function(){
		var p_id = $(this).attr('promo_id');
		var cookie = $.cookie('vote_'+p_id);
		console.log(cookie);
		var active, inactive;
		if(cookie == 1){
			active = 'a.like_promotion';
			inactive = 'a.dislike_promotion';
		}else if(cookie == -1){
			active = 'a.dislike_promotion';
			inactive = 'a.like_promotion';
		}else{
			active = '-';
			inactive = '-';
		}
		$(this).children(active).addClass('color');
		$(this).children(inactive).css({'opacity':0,'visibility':'hidden'});
		var vote_points = $(this).children('h4');
		if(parseInt(vote_points.text()) > 0){
			vote_points.addClass('like_promotion color');
		}else if(parseInt(vote_points.text()) < 0){
			vote_points.addClass('dislike_promotion color');
		}
	});
});

function color_points(element){
	var points = parseInt(element.text());
	console.log(points);
	if(points > 0){
		element.addClass('like_promotion');
		element.removeClass('dislike_promotion');
	}else if(points == 0 ){
		element.removeClass('like_promotion dislike_promotion');
	}else if(points < 0){
		element.removeClass('like_promotion');
		element.addClass('dislike_promotion');
	}
}