$(document).ready(function(){
	CKEDITOR.replace('id_content');
	$('.dates input').datepicker({
		'dateFormat':'yy-mm-dd'
	});

	categorize_subcategories();
	$('select#id_category_pk').change(function(){
		var cat_val = $(this).val();
		$( 'div.subcategory_row > select' ).attr('disabled','disabled');
		$( 'div.subcategory_row > select' ).hide();
		$( 'div.subcategory_row > select.category_'+cat_val ).removeAttr('disabled');
		$( 'div.subcategory_row > select.category_'+cat_val ).show()
	});
});
function cancelEdit(url){
	var redirect = confirm("Cancel and discard all changes, are you sure?");
	if(redirect == true){
		window.location = url;
	}
}

function categorize_subcategories(){
	var subcats = JSON.parse($('p.subcategories').text());
	$('p.subcategories').remove();
	console.log(subcats);
	var subcats_array = new Array();
	for (var i = 0; i < subcats.length; i++) {
	    var cat_id = subcats[i].category;
	    console.log(cat_id);
	    var s_option = '<option value="'+subcats[i].id+'">'+subcats[i].name+'</option>';
	    if(subcats_array[cat_id] != undefined){
		   subcats_array[cat_id] += s_option;
		}else{
	        subcats_array[cat_id] = s_option;
		}
	};
	console.log(subcats_array);

	for (var i = 0; i < subcats_array.length; i++){
	    if (subcats_array[i] != undefined){
	        var tempStr = 
	        '<select name="subcategory_pk" id="id_subcategory_pk" class="category_'+i+'" disabled style="display:none">' +
	        subcats_array[i] +
	        '</select>';
	        
	        $('div.subcategory_row').append(tempStr);
	    };
	};
}