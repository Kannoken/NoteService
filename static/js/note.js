    $(document).ready(function() {

        $('#noteInfo').submit(function () {
            $.ajax({
                data: $(this).serialize(),
                type: "POST",
                url: window.location.href,
                success: function (response) {
                    console.log('OKS')
                }
            });
            return false;
        });

    })