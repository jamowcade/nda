$(document).ready(function() {
    createCompany();
    EditCompany();
    generateDataTable();
 
})

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


function createCompany(){
    $('#registerForm').submit(function (e){
        e.preventDefault();
        
        const formData = $(this).serialize();
        console.log(formData)
            // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
            $.ajax({
                url: '/newCompany/',
                type: "POST",
                data: {
                    name: $('#name').val(),
                    description: $('#description').val(),
                    asn: $('#asn').val(),
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
                        
                        $('#name').val(''),
                        $('#description').val(''),
                        $('#asn').val(''),
                        window.location.reload();
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

function EditCompany(){
    $('.companyEdit').click(function(){
        
        var id = $(this).data('id');
        var name = $(this).data('name');
        var description = $(this).data('description');
        var asn = $(this).data('asn');
        // alert('The ID of this row is: ' + id+network+description+state);
        $('#updateCompany').modal('show')
        $('#uname').val(name)
        $('#udescription').val(description)
        $('#uasn').val(asn)


        $('#UpdateForm').submit(function (e){
            e.preventDefault();
   
                // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
                $.ajax({
                    url: '/editCompany/',
                    type: "POST",
                    data: {
                        id: id,
                        name:  $('#uname').val(),
                        asn:  $('#uasn').val(),
                        description: $('#udescription').val(),
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
                    },
                  
                    success: function(data) {
                      
                        swal("Success", data, "success")
                        .then(function(){
                            $('#updateCompany').hide();
                            // readNetwork()
                            location.reload();
                        });
    
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