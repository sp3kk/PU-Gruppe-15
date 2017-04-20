$(document).ready(function() {
	// clickable row in table
	$(".clickable_row").click(function() {
		window.location = $(this).data("href");
	})
});