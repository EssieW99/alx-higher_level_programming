//  updates the color of the <header> when the user clicks on the tag DIV#red_header
$(function () {
    $('DIV#red_header').click(function () {
        $('header').css('color', '#FF0000');
    });
});