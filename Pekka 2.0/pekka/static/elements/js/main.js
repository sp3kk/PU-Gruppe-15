$(document).ready(function() {
	// clickable row i tabell
	$(".clickable_row").click(function() {
		window.location = $(this).data("href");
	})
});