$(document).ready(function() {
    getPermissions();
   
    assign_permissions();
  });


  function getPermissions(){
    $('#content_type').on('change', function() {
        var contentTypeId = $(this).val();
        var permissionsTable = $('#permissions_table tbody');
        var group_id = $('#select-group').val();
        permissionsTable.html('');
        $.ajax({
            url: '/get_permissions/',
            type: 'GET',
            data: {
              'content_type_id': contentTypeId,
              'group_id':group_id
            },
            success: function(response) {
                $('#permissionDiv').show()
                // $.each(response, function(index, obj) {
                //   permissionsTable.append(
                //     '<tr>'+
                //     '<td>' + obj.name +'</td>' + 
                //     '<td><input type="checkbox" name="group_permissions" value="' + obj.id + '"></td>'+
                //     '</tr>'
                //     );
                // }); 
              permissionsTable.html(response);
              console.log(group_id);
              group_permissions_select(contentTypeId,group_id);
              
            },
            error: function(xhr, status, error) {
              console.log(error);
            }
          });
      
      });
  }

  function assign_permissions(){
        $('input[name="view_permissions"]').change(function() {
          console.log("ok");
            var permission_id = $(this).val();
            var group_id = $('#select-group').val();
            var isChecked = $(this).is(':checked');
            $.ajax({
                url: '/assign_permissions_to_group/',
                type: 'POST',
                data: {
                  'group_id': group_id,
                  'permission_id': permission_id,
                  'is_checked': isChecked,
                  csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
                },
                success: function(response) {
                  if(isChecked){
                    swal({
                        title: "Success!",
                        text: "Permission Assigned.",
                        type:"success",
                        icon: "success",
                        timer: 2000,
                        showConfirmButton: false
                      });
                    
                  }
                  else{
                    swal({
                        title: "Success!",
                        text: "Permission Removed.",
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

function group_permissions_select(contentTypeId,group_id){
      $.ajax({
        url: '/get_group_permissions/',
        data: {
          group_id: group_id,
          content_type_id: contentTypeId
        },
        
        success: function(data) {
          // Do something with the permissions.
         
          group_permissions = data.permissions;
          $('input[name="view_permissions"]').each(function() {
            var str = $(this).val();
          
            permission_checkbox = parseInt(str);
            if(group_permissions.includes(permission_checkbox)){
                $(this).prop('checked', true);
            }else{
                $(this).prop('checked', false);
            }
            
            
          });

        }
      });
   

}
  