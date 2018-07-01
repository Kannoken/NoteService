$(document).ready(function () {
    $('#form1').submit(function () {
// catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: "/newNote/", // the file to call
            success: function (response) { // on success..
                console.log('OKS')
            }
        });
        return false;
    });
    $('.delete-note').click(function () {
        $.ajax({ // create an AJAX call...
            data: {'id': $(this).attr('id')}, // get the form data
            type: "POST", // GET or POST
            url: "/deleteNote/", // the file to call
            success: function (response) { // on success..
                console.log('OKS')
            }
        });
    });
    $('#sortbycat').click(function () {
        let cards = $('#notes-container'), cont = cards.children('.card');
        cont.detach().sort(function (a, b) {
            // console.log(a)
            a = a.getElementsByTagName("span")[0];
            b = b.getElementsByTagName("span")[0];
            console.log(a, b);
            if (a.textContent <= b.textContent) {
                return -1;
            } else {
                return 1;
            }
        }).appendTo('#notes-container');
    });
    $('#sortbyeject').click(function () {
        let cards = $('#notes-container'), cont = cards.children('.card');
        let eject = cont.children('.eject').parent();
        let another = cont.not(eject);
        cont.detach();
        eject.appendTo('#notes-container');
        another.appendTo('#notes-container')
    });
    $('#findfilter').click(function () {
        let title = $('#titlefilter').val();
        let cat = $('#catfilter').val();
        let date = $('#datefilter').val();
        let cards = $('#notes-container'), cont = cards.children('.card');
        let result = [];

        if (title) {
            let cont_title = cont.children('.card-body');
            Array.from(cont_title).forEach(function (item) {
                if ($(item).children('.card-title')[0].innerHTML.startsWith(title)) {
                    result.push(item.parentElement)
                }
            })
        }

        if (cat) {
            let tmp = [];
            let arr = [];
            if (title)
                arr = result;
            else
                arr = Array.from(cont);
            Array.from(arr).forEach(function (item) {

                if ($(item).children('.card-cat')[0].innerHTML === cat) {
                    tmp.push(item);
                }
            });
            result = tmp;
        }
        if (date) {
            let tmp = [];
            let arr = [];
            let dat  = new Date(date);

            if (title || cat)
                arr = result;
            else
                arr = Array.from(cont);
            Array.from(arr).forEach(function (item) {
                let it = new Date($(item).children('.card-body').children('.card-date')[0].innerHTML);
                if (it.getDate() === dat.getDate()) {
                    console.log(it)
                    tmp.push(item);
                }
            });
            result = tmp;
        }
            $('#notes-container').children('.card').detach();
            result.forEach(function (item) {
                $('#notes-container').append(item)
            })

    });


});