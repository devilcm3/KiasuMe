function registerValidation(){
	var all_good = true;

	$('input[id^=id_]').each(function(){
		if($(this).val() == '' ){
			$(this).addClass('error_field');
			all_good = false;
		}else{
			$(this).removeClass('error_field');
		}
	});

	var p1 = $('input#id_password').val();
	var p2 = $('input#id_password2').val();
	if( p1 != '' && p2 != ''){
		if( p1 != p2 ){
			$('input#id_password').addClass('error_field');
			$('input#id_password2').addClass('error_field');
			$('div.register_password_form').append('<p>Passwords Do Not Match</p>');
			all_good = false;
		}else{
			$('input#id_password').removeClass('error_field');
			$('input#id_password2').removeClass('error_field');
			$('div.register_password_form p').remove();
		}
	}

	return all_good;
}