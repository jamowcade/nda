$(document).ready(function() {

    search_user();
    getPermissions();
    assign_permissions();
     
     });
   
   function search_user(){
      // Attach change event handler to search input
      $('#search-input').on('input', function() {
     
       // Get the search input value
       var searchValue = $(this).val();
   
       // Only make the AJAX request if the search value is at least 3 characters long
       if (searchValue.length >= 3) {
   
         // Make an AJAX request to get the user's info
         $.ajax({
           url: '/get-user-info/',
           type: 'POST',
           data: { search_value: searchValue },
           success: function(data) {
             // Populate user info
             $('#user-list').empty();
             $.each(data, function(index, user){
               var listItem = $('<li>').text(user.name + ' (' + user.email + ')');
               listItem.css('cursor', 'pointer');
               listItem.css('list-style', 'none');
               listItem.hover(function() {
                 $(this).css('background-color', '#f5f5f5');
                 $(this).css('font-size', '16px');
               }, function() {
                 $(this).css('background-color', 'transparent');
                 $(this).css('font-size', '14px');
               });
             
               listItem.on('click', function() {
   
                 // Fill the search input with the selected user's nam
                 $('#search-input').val(user.name);
                 $('#content_typeDiv').show()
                 // Clear the user list
                 $('#user-list').empty();
               })
               $('#user-list').append(listItem);
             });
           }
         });
   
       } else {
         // Clear the user info container if the search value is less than 3 characters
         $('#user-list').empty();
       }
   
     });
   }
   
     
     function getPermissions(){
       $('#content_type').on('change', function() {
           var contentTypeId = $(this).val();
           var permissionsTable = $('#permissions_table tbody');
           var user_id = $('#search-input').val()
           permissionsTable.html('');
           $.ajax({
               url: '/get_permissions_user/',
               type: 'GET',
               data: {
                 'content_type_id': contentTypeId
                 
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
                 user_permissions_select(contentTypeId, user_id)
               },
               error: function(xhr, status, error) {
                 console.log(error);
               }
             });
         
         });
     }
   
     
   function user_permissions_select(contentTypeId,user_id){
     $.ajax({
       url: '/get_user_permissions/',
       data: {
         user_id: user_id,
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
   
   // assign permission to user
   function assign_permissions(){
     $('input[name="view_permissions"]').change(function() {
       console.log("ok");
         var permission_id = $(this).val();
         var user_id = $('#search-input').val()
         var isChecked = $(this).is(':checked');
         $.ajax({
             url: '/assign_permissions_to_user/',
             type: 'POST',
             data: {
               'user_id': user_id,
               'permission_id': permission_id,
               'is_checked': isChecked,
               csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() 
             },
             success: function(response) {
               if(isChecked){
                 console.log(response);
                 alert("Permission added to user!")
                 
               }
               else{
                   alert("Permission removed from user!")
               }
              
             },
             error: function(xhr, status, error) {
               alert("error assigning")
             }
           });
   
       });
   
   }
   
   
   