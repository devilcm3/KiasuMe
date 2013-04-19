$(document).ready(function(){
	CKEDITOR.replace('id_content');
	$('.dates input').datepicker({
		'dateFormat':'yy-mm-dd'
	});
});