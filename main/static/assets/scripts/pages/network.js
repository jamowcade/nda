$(document).ready(function() {
    readNetwork();
    createNetwork();
    EditNetwork();
})

function createNetwork(){
    $('#registerForm').submit(function (e){
        e.preventDefault();
        network = $('#network').val()
        const input_network = $('#network')
        const error_input = $('#error-message')
        console.log(isValidIpAddress(network))
        errorMessage = isValidIpAddressWithSubnet(network)
        if (errorMessage) {
            input_network.addClass('invalid')
            error_input.text(errorMessage);

        }
        else{
            error_input.text('');
            // alert("network is okd")
            sendRequest();
        }

        function sendRequest(){
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
                    if (data.success) {
                        swal("success", data.message, "success").then(function(){
                          location.reload();
                        });
                    }else 
                    {
                        swal("ERROR", data.error, "error");
                    }

                },
                error:function(data){
                    console.log(data)
                    swal({
                        title: "Error !",
                        text: "There was an error: "+data.error,
                        icon: "error",
                        timerProgressBar: true,
                        showConfirmButton: false
                    })
                }
            })
        }
            // console.log($District + " " + $Type + " " + $NetworkNo+ " " + $status)
    


    })
}

function isValidIpAddress(ipAddress) {
    const ipAddressRegex = /^(\d{1,3}\.){3}\d{1,3}\/(0|[1-2][0-9]|3[0-2])$/;
    return ipAddressRegex.test(ipAddress);
  }

function isValidIpAddressWithSubnet(ipAddress) {
    const ipAddressRegex = /^(\d{1,3}\.){3}\d{1,3}\/(0|[1-2][0-9]|3[0-2])$/;
    if (!ipAddressRegex.test(ipAddress)) {
      return 'Invalid IP address or subnet mask';
    }
    const [address, subnet] = ipAddress.split('/');
    const octets = address.split('.').map(octet => parseInt(octet));
    if (octets.some(octet => octet > 255)) {
      return 'Invalid IP address';
    }
    const prefixLength = parseInt(subnet);
    if (prefixLength < 0 || prefixLength > 32) {
      return 'Invalid subnet mask';
    }
    return '';
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