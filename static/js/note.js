    $(document).ready(function() {

        $('#noteInfo').submit(function () {
// catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: "POST", // GET or POST
                url: window.location.href, // the file to call
                success: function (response) { // on success..
                    console.log('OKS')
                }
            });
            return false;
        });

    })