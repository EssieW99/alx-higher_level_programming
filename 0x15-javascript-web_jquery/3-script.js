// adds a class 'red' to the <header> element when the user clicks on the tag DIV#red_header
$(function () {
    $('DIV#red_header').click(function () {
        $('header').addClass('red');
    });
});