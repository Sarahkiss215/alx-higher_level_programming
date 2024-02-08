/**
 * Script which adds the red class to the <header>
 * element when the user clicks on the tag DIV#red_header
 */
$('DIV#red_header').click(() => {
    $('header').addClass('red');
});
