new MDCRipple(document.querySelector('.cancel'));
new MDCRipple(document.querySelector('.next'));


const buttonRipple = new MDCRipple(document.querySelector('.mdc-button'));
function togglearchive(){
    console.log("AU");
    document.getElementById("archives").classList.toggle('gold');
    document.getElementById("archive_display").classList.toggle('active');
    console.log("AU-pt2");
    document.getElementById("input_form").classList.toggle('hide');
}
function toggleSidebar(){
    console.log("FU");
    document.getElementById("sidebar").classList.toggle('active');
   
}
