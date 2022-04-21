var idnList = [];
$(document).ready(function() {
    
    $("input").click(function(){
        idnList = [];
        $.each($("input[name='risikoCheckId']:checked"), function(){
           
            idnList.push($(this).val());
        });
        console.log("ss");
        console.log(idnList.length);
        console.log(idnList)
        // alert("My favourite sports are: " + favorite.join(", "));
    });
});

$(document).ready(function () {
    // const csrftoken = $.Cookies.get('csrftoken');
    const csrftoken = Cookies.get('csrftoken');
    $('#insert-idn').click(function () {
        var RAid = $('#insert-idn').val();
        
        linkUrl = '/library/postRisikoRA/' + RAid + "/";
        userValue = $(this).prop('checked');
        alert(idnList);
        console.log(typeof(idnList))
        // event.preventDefault();
        $.ajax({
            headers: {
                contentType: "application/json",
                'X-CSRFToken': csrftoken
            },
            type: 'POST',
            url: linkUrl,
            data: {
                'idnList':idnList,
                'test':1,
            },
            dataType: "json",
            success: function (result) {
                location.reload();
            },
            error: function (e) {
                window.console.log(e);
            }
        });
        
    });
    
});