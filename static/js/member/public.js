$(document).ready(function(){
	$('.member_deal_wrapper .vote > *').each(function(){
		var total_vote = parseInt($(this).text());
		if(total_vote > 0){
			console.log('yup');
			$(this).children('.foundicon-thumb-down').hide();
			$(this).addClass('like_deal color');
		}else if(total_vote < 0){
			$(this).children('.foundicon-thumb-up').hide();
			$(this).addClass('dislike_deal color');
		}else{
			$(this).text('-');
		}
	})
});