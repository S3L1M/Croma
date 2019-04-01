function getSuccessOutput() {
    $.ajax({
        url:'/echo/js/?js=hello%20world!',
        complete: function (response) {
        console.log(response);
        var resp = JSON.parse(response);
        console.log(resp);
            $('#output').html(response.responseText);
        },
        error: function () {
            $('#output').html('Bummer: there was an error!');
        },
    });
    return false;
}

