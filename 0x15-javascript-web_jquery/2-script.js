/**
 * Script which updates the colour of text at the <header>
 * element to red (#FF0000) when the user clicks on the
 * tag DIV#red_header:
 */
$('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
});