var mySidebar = document.getElementById("mySidebar");
var overlayBg = document.getElementById("myOverlay");
function w3_open() {
    if (mySidebar.style.display === 'block' & myOverlay.style.display === 'block') {
        myOverlay.style.display = 'none';
        mySidebar.style.display = 'none';
    } else {
        mySidebar.style.display = 'block';
        myOverlay.style.display = "block";
    }
}
// Close the sidebar with the close button
function w3_close() {
    mySidebar.style.display = "none";
    myOverlay.style.display = "none";
}
