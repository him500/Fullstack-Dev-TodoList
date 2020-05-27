// import {MDCDrawer} from "@material/drawer";
// const drawer = MDCDrawer.attachTo(document.querySelector('.mdc-drawer'));
// mdc.ripple.MDCRipple.attachTo(document.querySelector('.foo-button'));
new MDCRipple(document.querySelector('.cancel'));
new MDCRipple(document.querySelector('.next'));
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
