$(document).ready(function(){
	$('.thumbs_wrapper a').click(function(){
		promo_id = parseInt($(this).parents('.thumbs_wrapper').attr('promo_id'));
		promo_vote = parseInt($(this).attr('promo_vote'));
		if ($.cookie('vote_'+promo_id)){
			
		}else{
			console.log(promo_id+promo_vote);
			$.post('/deal/vote/',{'promo_id':promo_id, 'promo_vote':promo_vote});
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
	console.log(points);
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