$(document).ready(function(){
    // adduser()
    activeAccount()
    disableAccount()
    editAccount()
    generateDataTable();
    
})


function activeAccount(){
    $('.activeAccount').click(function(){
        $id = $(this).data('id');
       
        $('#generateModal').modal('show');
        $('#userid').val($id)
        $('#activeAccountForm').submit(function (e){
            e.preventDefault()
            $userid = $('#userid').val()
            $password = $('#password').val()

            $.ajax({
                url : '/activeAccount/',
                type : 'POST',
                data : {
                    'id' : $userid,
                    'password' : $password,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()  
                },
                success : function(response){
                    if(response.success){
                        swal({
                            title: "Success !",
                            text: response.message,
                            icon: "success",
                            timer: 4000, // time in milliseconds
                            timerProgressBar: true,
                            showConfirmButton: false
    
                        })
                        .then(function(){
                            location.reload();
                        })

                    }
                },
                error: function(error){
                    swal({
                        title: "Error !",
                        text: "There was an error: "+error,
                        icon: "error",
                        timer: 4000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })

                }
            })

        });
    })
}


function disableAccount(){

    $('.disableAccount').click(function (){
        $id= $(this).data('id');
        // alert($id)
        swal({
            title: "Are you sure?",
            text: "Do you really want to delete this record?",
            icon: "warning",
            buttons: ['No', 'Yes'],
            dangerMode: true,
        })
        .then((willDelete) => {
            if(willDelete){
                // alert($id)
                $status = 1

                $.ajax({
                    url: '/disableAccount/',
                    type: "POST",
                    data: {
                        'id': $id,
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
                    },
                    success : function(response){
                        if(response.success){
                            swal({
                                title: "Success !",
                                text: response.message,
                                icon: "success",
                                timer: 4000, // time in milliseconds
                                timerProgressBar: true,
                                showConfirmButton: false
        
                            })
                            .then(function(){
                                location.reload();
                            })
    
                        }
                    },
                    error: function(error){
                        swal({
                            title: "Error !",
                            text: "There was an error: "+error,
                            icon: "error",
                            timer: 4000, // time in milliseconds
                            timerProgressBar: true,
                            showConfirmButton: false
                        })
    
                    }
                })


            }
            else {
                swal({
                    title: "Canceled !",
                    text: "You have successfully Cancelled",
                    icon: "error",
                    timer: 3000, // time in milliseconds
                    timerProgressBar: true,
                    showConfirmButton: true
                }).then(function () {
                    location.reload()

                })
            }
        })

    })

}




function editAccount(){
    $('.editAccount').click(function(){
        var id = $(this).data('id');
        var first_name = $(this).data('first_name');
        var last_name = $(this).data('last_name');
        var username = $(this).data('username');
        var email = $(this).data('email');
        // alert('The ID of this row is: ' + id+network+description+state);
        $('#editModal').modal('show')
        // alert(id)
        $('#user-info').text(first_name+' '+last_name)
        $('#userid').val(id)
        $('#up_first_name').val(first_name)
        $('#up_last_name').val(last_name)
        $('#up_username').val(username)
        $('#up_email').val(email)


        $('#updateForm').submit(function (e){
            e.preventDefault();
   
                // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
                $.ajax({
                    url: '/editAccount/',
                    type: "POST",
                    data: {
                        id: id,
                        first_name: $('#up_first_name').val(),
                        last_name: $('#up_last_name').val(),
                        email: $('#up_email').val(),
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
                    },
                  
                    
                success : function(response){
                    if(response.success){
                        swal({
                            title: "Success !",
                            text: response.message,
                            icon: "success",
                            timer: 4000, // time in milliseconds
                            timerProgressBar: true,
                            showConfirmButton: false
    
                        })
                        .then(function(){
                            location.reload();
                        })

                    }
                },
                error: function(error){
                    swal({
                        title: "Error !",
                        text: "There was an error: "+error,
                        icon: "error",
                        timer: 4000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })

                }
                })
    
    
        })



        
    })


}

function generateDataTable(){
    $('#myTableExport').dataTable({
        dom: 'Bfrtip',
        buttons: [
            // 'copy', 
            'csv', 
            // 'excel', 
            'pdf', 
          'print'
        ]
      });
}
