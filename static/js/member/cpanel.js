$(document).ready(function(){
	$('a.delete_deal').click(function(){
		var cnf = confirm("Are you sure you want to delete this deal?");
		if (cnf){
			window.location = $(this).attr('link-href');
		}
	});
});