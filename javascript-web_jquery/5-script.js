const addItem = $('#add_item');
const ulClass = $('ul.my_list');

addItem.click( ()=> {
    ulClass.append('<li>Item</li>');
})