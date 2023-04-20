$(document).ready(function() {
    readCompany();
    creatCompany();
    // EditHouse();
})

function creatCompany(){
    $('#registerForm').submit(function (e){
        e.preventDefault();

        $case = $('#case').val();
        $owner = $('#owner').val();
        $asn = $('#asn').val();
        var currentTime = new Date();
        var formattedTime = currentTime.toLocaleTimeString();
        // alert(`The current time is ${formattedTime}`);
        // $timing = formattedTime


        
        if($case != null && $owner != null && $asn != null && formattedTime != null ) {
            
            // alert(`Option Value: ${$District}\ndata-foo: ${$DistrictApr}\nHouseNumer: ${$HouseNumber}`);
       
     
            console.log($case + " " + $owner + " " + $asn+ " " + formattedTime)
            $.ajax({
                url: '',
                type: "POST",
                data: {
                    'case': $case,
                    'owner': $owner,
                    'asn': $asn,
                    'formattedTime': formattedTime,
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

                        $('#newUser').hide();
                        readCompany()
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
                    // console.log("Erro is "+data)
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

function readCompany(){

    $.ajax({
        url: "house/",
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

// function EditHouse(){

//     $('#houseEdit').click(function(){
//         $id=$(this).attr('name');
//         alert($id)
//         // $('#updateHouse').modal('show');
//         // $('#udistrict').val($id)


//     })

// }