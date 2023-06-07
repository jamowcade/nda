
$(document).ready(function() {

  $('#customFile').change(function() {
    var filename = $(this).val().split('\\').pop();
    $('#filenmaeDisplay').text(filename);
});

  $('.progress').hide();
  addScanDate();
  
    scan_case_fileUpload();
    generateDataTable();
   
});






function scan_case_fileUpload(){
  $('.file-upload').click(function(){
        
    var scan_case_id = $(this).data('id');
    $('#newfileUpload').modal('show')
    $('#scan_case_id').val(scan_case_id)

    $('#fileUploadForm').submit(function(e) {
      e.preventDefault(); // prevent the default form submission
      var formData = new FormData(this); // create a new FormData object from the form
      $('.progress-bar').width('0%'); // reset the progress bar
      $('.progress').show(); // show the progress bar
      $.ajax({
        url: '/uploadhosts/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        xhr: function() {
          var xhr = $.ajaxSettings.xhr();
          xhr.upload.onprogress = function(e) {
            if (e.lengthComputable) {
              var percentComplete = (e.loaded / e.total) * 100;
              $('.progress-bar').width(percentComplete + '%');
              $('.progress-bar').attr('aria-valuenow', percentComplete);
              $('.progress-bar').text(percentComplete.toFixed(2) + '%');
            }
          };
          return xhr;
        },
        success: function(data) {
          $('.progress').hide(); // hide the progress bar
          if (data.success) {
            swal("Form submitted!", data.message, "success").then(function(){
              location.reload();
            });
          } else {
            swal("Form submission failed!", data.error, "error");
          }
        }
      });
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


function addScanDate(){
  $('#scancase-form').submit(function (e){
    e.preventDefault();
    date = $('#date').val()
   $.ajax({
    method: 'POST',
    url: '/scan_case/',
    data : {
      'date':date,
       csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    success: function(data){
      if (data.success) {
        swal("Form submitted!", data.message, "success").then(function(){
          location.reload();
        });
      } else {
        swal("Form submission failed!", data.message, "error");
      }
    },
    error: function(){
      alert("error saving data")
    }
   })
})


}