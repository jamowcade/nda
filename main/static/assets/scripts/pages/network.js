$(document).ready(function() {
    readNetwork();
    createNetwork();
    EditNetwork();
})

function createNetwork(){
    $('#registerForm').submit(function (e){
        e.preventDefault();
        
        const formData = $(this).serialize();
        console.log(formData)

       
            
            // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
            $.ajax({
                url: '/addnetwork/',
                type: "POST",
                data: {
                    company: $('#company').val(),
                    network: $('#network').val(),
                    state: $('#state').val(),
                    description: $('#description').val(),
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
                    console.log(data)
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



function EditNetwork(){
        $('.networkEdit').click(function(){
            var id = $(this).data('id');
            var network = $(this).data('network');
            var description = $(this).data('description');
            var state = $(this).data('state');
            // alert('The ID of this row is: ' + id+network+description+state);
            $('#updateNetwork').modal('show')
            $('#unetwork').val(network)
            $('#udescription').val(description)
            $('#ustate').val(state)


            $('#UpdateForm').submit(function (e){
                e.preventDefault();
       
                    // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
                    $.ajax({
                        url: '/updateNetwork/',
                        type: "POST",
                        data: {
                            id: id,
                            network: $('#unetwork').val(),
                            state: $('#ustate').val(),
                            description: $('#udescription').val(),
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
                        },
                      
                        success: function(data) {
                          
                            swal("Success", data, "success")
                            .then(function(){
                                $('#updateNetwork').hide();
                                readNetwork()
                                location.reload();
                            })
        
                        },
                        error: function(data){
                           
                            swal("Error", data, "error");
                            // swal({
                            //     title: "Error !",
                            //     text: "There was an error: "+data,
                            //     icon: "error",
                            //     timer: 4000, // time in milliseconds
                            //     timerProgressBar: true,
                            //     showConfirmButton: false
                            // })
                        }
                    })
        
        
            })



            
        })
  

}