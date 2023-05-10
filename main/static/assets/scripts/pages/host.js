$(document).ready(function() {
  
  
  displayPorts()
  
   
   });


// function uploadfiles(){
//   const form = document.getElementById('my-form');
//   form.addEventListener('submit', (event) => {
//     event.preventDefault();
//     const formData = new FormData(form);
//     fetch('/uploadhosts/', {
//       method: 'POST',
//       body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//       if (data.success) {
//         console.log('JSON data saved successfully');
//       } else {
//         console.error('Error saving JSON data:', data.error);
//       }
//     })
//     .catch(error => {
//       console.error('Error saving JSON data:', error);
//     });
//   });
  
// }

// function scan_case_fileUpload(){
//   $('#my-form').on('submit', function(e) {
//     e.preventDefault(); // prevent the default form submission
//     var formData = new FormData(this); // create a new FormData object from the form
//     $('.progress-bar').width('0%'); // reset the progress bar
//     $('.progress').show(); // show the progress bar
//     $.ajax({
//       url: '/uploadhosts/',
//       type: 'POST',
//       data: formData,
//       processData: false,
//       contentType: false,
//       xhr: function() {
//         var xhr = $.ajaxSettings.xhr();
//         xhr.upload.onprogress = function(e) {
//           if (e.lengthComputable) {
//             var percentComplete = (e.loaded / e.total) * 100;
//             $('.progress-bar').width(percentComplete + '%');
//             $('.progress-bar').attr('aria-valuenow', percentComplete);
//             $('.progress-bar').text(percentComplete.toFixed(2) + '%');
//           }
//         };
//         return xhr;
//       },
//       success: function(data) {
//         $('.progress').hide(); // hide the progress bar
//         if (data.success) {
//           swal("Form submitted!", "The form has been submitted successfully.", "success");
//         } else {
//           swal("Form submission failed!", "There was an error while submitting the form.", "error");
//         }
//       }
//     });
//   });
// }




function displayPorts(){
  $('.btn-show').click(function(event) {
    event.preventDefault();
    var id = $(this).attr('href');
    $('#displayPorts').modal('show');
    $.ajax({
      url: '/host_ports/',
      method: 'GET',
      data: {'host_id': id},
      dataType: 'json',
      success: function(response) {
        
        console.log(response)
        var tableBody = $('#displayPorts .modal-body table tbody');
        tableBody.empty();
        $.each(response, function(index, port) {
          index = index+1
          tableBody.append(
          '<tr>'+
          '<td>' + index + '</td>'+
          '<td>' + port.port + '</td>'+
          '<td>' + port.protocol + '</td>'+
          '<td>' + port.state + '</td>'+
          '<td>'+ port.service + '</td>'+
           '</tr>' 
           
           );
        });
      }
    });
  });
}