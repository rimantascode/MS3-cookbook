$('#b4').click(function (event) {
    event.preventDefault();
    swal({
        title: "Are you sure?",
        text: "Once deleted, you will not be able to recover the recipe!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((willDelete) => {
            if (willDelete) {
                swal("Your recipe has been deleted!", {
                    icon: "success",
                });
                window.location = $(this).attr('href');
            } else {
                swal("Your recipe is safe!");
            }     
        });
});