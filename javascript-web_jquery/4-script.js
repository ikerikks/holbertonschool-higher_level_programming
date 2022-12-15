const toggleHeader = $('#toggle_header');
const header = $('header');

toggleHeader.click( () => {
    if (header.hasClass('green')) {
        header.removeClass('green')
        header.toggleClass('red');
    } else {
        header.removeClass('red')
        header.toggleClass('green');
    }
   
})