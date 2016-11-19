(function ($) {
	$('.spinner .btn:last-of-type').on('click', function() {
		var input = $(this).parent().parent().find('input');
		console.dir(input);

		if (input.data('like-disabled') != 'True') {
 			input.val(parseInt(input.val(), 10) + 1);

 			if (input.data('dislike-disabled') != 'True') {
 				input.data('like-disabled', 'True');
 			}

 			input.data('dislike-disabled', 'False');

 			// Todo: Ajax send voting query
 		}
	});

	$('.spinner .btn:first-of-type').on('click', function() {
		var input = $(this).parent().parent().find('input');

		if (input.data('dislike-disabled') != 'True') {
 			input.val(parseInt(input.val(), 10) - 1);

 			if (input.data('like-disabled') != 'True') {
 				input.data('dislike-disabled', 'True');
 			}

 			input.data('like-disabled', 'False');

 			// Todo: Ajax send voting query
 		}
	});
})(jQuery);

