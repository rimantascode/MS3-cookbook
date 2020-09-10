var val;
var z;
$("#recipe_name").keyup(function () {
    val = $("#recipe_name").val();
    var x = val.length;
    z = 20 - x;

    if (z >= 0) {
        $("#add_recipe").prop("disabled", true);
        $("#update").prop("disabled", true);
        $("#count")
            .css({ color: "red" })
            .text("Characters left " + z)
            .show(1000);
    } else {
        $("#add_recipe").prop("disabled", false);
        $("#update").prop("disabled", false);
        $("#count").css({ color: "green" }).text("Thank You").hide(1000);
    }
});
