$(document).ready(function() {
    readNetwork();
    createNetwork();
    // EditNetwork();
})

function createNetwork(){
    $('#registerForm').submit(function (e){
        e.preventDefault();
        
        company
        network
        state
        description

        if($Name != null && $Tell != null && $MartialStatus != null && $status == 0) {
            
            // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
            $.ajax({
                url: '',
                type: "POST",
                data: {
                    'name': $Name,
                    'tell': $Tell,
                    'martial_status': $MartialStatus,
                    'status': $status,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()                    
                },
                success: function(data) {
                    swal({
                        title: "Success !",
                        text: "You have successfully Created",
                        icon: "success",
                        timer: 1000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })
                    .then(function(){

                        $('#newNetwork').hide();
                        readNetwork()
                        location.reload();
                    })

                },
                error:function(data){
                    swal({
                        title: "Error !",
                        text: "There was an error: "+data,
                        icon: "error",
                        timer: 4000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })
                }
            })

            
        }
        else{
            swal({
                title: "Error !",
                text: "There was an error for Saving",
                icon: "error",
                timer: 4000, // time in milliseconds
                timerProgressBar: true,
                showConfirmButton: false
            })
        }


    })
}

function readNetwork(){

    $.ajax({
        url: "network/",
        type: "POST",
        async: false,
        data:{
            res : 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#tbody_data').html(response)
        }
    })

}

// function EditNetwork(){

//     $('#NetworkEdit').click(function(){
//         $id=$(this).attr('name');
//         alert($id)
//         // $('#updateNetwork').modal('show');
//         // $('#udistrict').val($id)


//     })

// }