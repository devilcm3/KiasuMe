$(document).ready(function(){
	$('.js_error').hide();
	CKEDITOR.replace('id_content');
	$('.dates input[name="date_started"]').datepicker({
		'dateFormat':'yy-mm-dd',
		'minDate':0
	});
	$('.dates input').datepicker('setDate', new Date());

	$(document).foundation('tooltips');
	categorize_subcategories();
	$('select#id_category_pk').change(function(){
		var cat_val = $(this).val();
		$( 'div.subcategory_row > select' ).attr('disabled','disabled');
		$( 'div.subcategory_row > select' ).hide();
		$( 'div.subcategory_row > select.category_'+cat_val ).removeAttr('disabled');
		$( 'div.subcategory_row > select.category_'+cat_val ).show()
	});
});
function dealValidation(){
	var allClear = true;
	$('input, div').removeClass('error_field');
	$('.js_error').hide();
	//REMOVE ALL ERROR BORDER FIRST, THEN APPLY LATER ON


	if ($('#id_title').val().length == 0) {
		allClear = false;
		$('#id_title').addClass('error_field');
	}

	if ($('#id_category_pk').val().length == 0) {
		allClear = false;
		$('#id_category_pk').addClass('error_field');
	}

	var dateError = false;
	if($('#id_date_ended').val().length != 0){
		var dateStart 	= $('#id_date_started').val().split('-');
		var dateEnd 	= $('#id_date_ended').val().split('-');

		if (dateStart[0] > dateEnd[0]){
			// CHECK YEAR 
			dateError = true;
			console.log('year error');
		} else {
			if (dateStart[1] > dateEnd[1]){
				//CHECK MONTH
				dateError = true;
				console.log('month error');
			} else {
				if (dateStart[1] >= dateEnd[1] && dateStart[2] > dateEnd[2]){
					dateError = true;
					console.log('day error');
				}
			}
		}
	}

	if (dateError == true){
		$('#id_date_started').addClass('error_field');
		$('#id_date_ended').addClass('error_field');
		allClear = false;
	}

	if (gCharCount > 2000){
		$('div#cke_id_content').addClass('error_field');
		allClear = false;
	}

	if (!allClear){
		$('.js_error').show();
	}

	return allClear;
}


function cancelEdit(url){
	var redirect = confirm("Cancel and discard all changes, are you sure?");
	if(redirect == true){
		window.location = url;
	}
}

function categorize_subcategories(){
	var subcats = JSON.parse($('p.subcategories').text());
	$('p.subcategories').remove();
	var subcats_array = new Array();
	for (var i = 0; i < subcats.length; i++) {
	    var cat_id = subcats[i].category;
	    var s_option = '<option value="'+subcats[i].id+'">'+subcats[i].name+'</option>';
	    if(subcats_array[cat_id] != undefined){
		   subcats_array[cat_id] += s_option;
		}else{
	        subcats_array[cat_id] = s_option;
		}
	};

	for (var i = 0; i < subcats_array.length; i++){
	    if (subcats_array[i] != undefined){
	        var tempStr = 
	        '<select name="subcategory_pk" id="id_subcategory_pk" class="category_'+i+'" disabled style="display:none">' +
	        '<option selected="selected" value="">---------</option>'+
	        subcats_array[i] +
	        '</select>';
	        
	        $('div.subcategory_row').append(tempStr);
	    };
	};

	var cat_val = $('select#id_category_pk').val();
	$( 'div.subcategory_row > select' ).attr('disabled','disabled');
	$( 'div.subcategory_row > select' ).hide();
	$( 'div.subcategory_row > select.category_'+cat_val ).removeAttr('disabled');
	$( 'div.subcategory_row > select.category_'+cat_val ).show();
}