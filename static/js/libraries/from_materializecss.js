$(document).ready(function () {
    $(".sidenav").sidenav();
    $(".dropdown-trigger").dropdown();
    $("select").formSelect();
    $("textarea#message").characterCounter();
});
document.addEventListener("DOMContentLoaded", function () {
    var elems = document.querySelectorAll(".fixed-action-btn");
    var instances = M.FloatingActionButton.init(elems, {
        direction: "up",
        hoverEnabled: false,
    });
});