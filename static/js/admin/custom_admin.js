$(document).ready(function(){
	var editorInterval = setInterval(function(){
	if(CKEDITOR.instances['id_content'] == undefined){
		CKEDITOR.replace('id_content');
	}else{
		clearInterval(editorInterval);
	}
	},1000);
});