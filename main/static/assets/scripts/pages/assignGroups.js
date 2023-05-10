$(document).ready(function() {
    getUserGroups()
    assignGroup();
  });

  function assignGroup(){
    $('input[name="groups"]').change(function() {
        var groupId = $(this).val();
        var user_id = $('#user-select').val();
        var isChecked = $(this).is(':checked');
        
        $.ajax({
          url: '/assign_user_to_groups/',
          type: 'POST',
          data: {
            'group_id': groupId,
            'user_id': user_id,
            'is_checked': isChecked,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
          },
          success: function(response) {
            if(isChecked){
                swal({
                    title: "Success!",
                    text: "Group Assigned.",
                    type:"success",
                    icon: "success",
                    timer: 2000,
                    showConfirmButton: false
                  });
            }
            else{
                swal({
                    title: "Success!",
                    text: "Group Removed.",
                    type:"success",
                    icon: "success",
                    timer: 2000,
                    showConfirmButton: false
                  });
                
            }
           
          },
          error: function(xhr, status, error) {
            alert("error assigning")
          }
        });
      });
  }

// get user groups and select the checkbox

function getUserGroups(user_id){

    $('#user-select').change(function() {
        var user_id = $(this).val();
        $.ajax({
          url: '/get_user_groups/',
          type: 'GET',
          data: {
              "user_id": user_id
          } ,
          success: function(response) {
            $('#user_groups').show()
            var userGroups = response.groups;
            console.log(userGroups)
           
            $('input[name="groups"]').each(function() {
                var checkbox_value = $(this).val();
                
                myvalue = parseInt(checkbox_value);
                if(userGroups.includes(myvalue)){
                    $(this).prop('checked', true);
                }else{
                    $(this).prop('checked', false);
                }
                
                
              });
          },
          error: function(xhr, status, error) {
            console.log(error);
          }
        });
  
      });

}



 
