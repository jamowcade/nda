$(document).ready(function() {

  uploadfiles()
  displayPorts()
   
   });


function uploadfiles(){
  const form = document.getElementById('my-form');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetch('/uploadhosts/', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        console.log('JSON data saved successfully');
      } else {
        console.error('Error saving JSON data:', data.error);
      }
    })
    .catch(error => {
      console.error('Error saving JSON data:', error);
    });
  });
  
}


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
          '<tr><td>' + index + '</td><td>' + 
           + port.port + '</td><td>' + 
           port.protocol + '</td><td>' + 
           
           port.state + '</td></tr>');
        });
      }
    });
  });
}