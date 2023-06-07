$(document).ready(function() {
    
    // paginate();
  displayServices()
  generateDataTable();
  
   
   });



function displayServices(){
  $('.btn-show').click(function(event) {
    event.preventDefault();
    var id = $(this).attr('href');
    $('#displayPorts').modal('show');
    $.ajax({
      url: '/get_services/',
      method: 'GET',
      data: {'port_id': id},
      dataType: 'json',
      success: function(response) {
        
        console.log(response)
        var tableBody = $('#displayPorts .modal-body table tbody');
        tableBody.empty();
        $.each(response, function(index, service) {
          index = index+1
          tableBody.append(
          '<tr>'+
          '<td>' + index + '</td>'+
          '<td>' + service.key + '</td>'+
          '<td>' + service.value + '</td>'+
           '</tr>' 
           
           );
        });
      }
    });
  });
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




function emptyFormData() {
  $('#company').val(''),
  $('#network').val(''),
  $('#state').val(''),
  $('#description').val('')
}




function paginate(){
    $('.pagination li a').click(function(e){
      e.preventDefault()
      page = $(this).attr('href')
      console.log(page)
      var startTime = new Date().getTime();
      $.ajax({
              url: '/Ports/',
              data: {
                "page":page,  
              },
              success: function(response) {
                var endTime = new Date().getTime();
                var responseTime = (endTime - startTime) / 1000;
                  $('#accordion').empty()
                  $('#accordion').append(response.html)
                  $('#response-time').text(` (${responseTime.toFixed(2)} seconds) `);
              }
          });
    })
  }