
$(document).ready(function() {

  $('.progress').hide();
  
    scan_case_fileUpload();
   
});






function scan_case_fileUpload(){
  $('.file-upload').click(function(){
        
    var date = $(this).data('date');
    $('#newfileUpload').modal('show')
    $('#scan_case_date').val(date)

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