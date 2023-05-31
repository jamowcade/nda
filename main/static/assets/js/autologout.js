var inactivityTimeout;

// Define a function to reset the inactivity timeout
function resetInactivityTimeout() {
  // Clear the existing timeout, if any
  clearTimeout(inactivityTimeout);

  // Set a new timeout for 30 seconds
  inactivityTimeout = setTimeout(function() {
    // This code will be executed after 30 seconds of inactivity
  //   swal({
     
  //   title: 'Ops',
  //   text: 'Your Session Has Been Expaired',
  //   icon: 'info',
  //   timer: 4000,
  //   buttons: 'Stay',
  // })

  // iziToast.info({
  //   title: 'Session Expired !',
  //   message: 'Please Login System Again',
  //   position: 'topRight'
  // })
  //   .then((willDelete) => {
  //     if (willDelete) {
        
  //     } else {
  //       $.ajax({
  //         url: '/logout/',
  //         type: 'GET',
  //         success:function(){

  //           window.location.href = '/login/';
  //           iziToast.info({
  //             title: 'Session Expired !',
  //             message: 'Please Login System Again',
  //             position: 'topRight'
  //           })

  //         }
  //       })
  //     }
  //   });


  $.ajax({
    url: '/logout/',
    type: 'GET',
    success:function(){

      iziToast.info({
        title: 'Session Expired !',
        message: 'Please Login System Again',
        position: 'topRight'
      })
      setTimeout(function() {
        window.location.href = '/login/';
      }, 4000);

    }
  })
  }, 600 * 1000);  // 10 minutes in milliseconds
}

// Add event listeners to reset the inactivity timeout on user activity
document.addEventListener('mousemove', resetInactivityTimeout);
document.addEventListener('keypress', resetInactivityTimeout);
document.addEventListener('mousedown', resetInactivityTimeout);
document.addEventListener('scroll', resetInactivityTimeout);
document.addEventListener('resize', resetInactivityTimeout);
document.addEventListener('touchstart', resetInactivityTimeout);
document.addEventListener('touchmove', resetInactivityTimeout);
document.addEventListener('touchend', resetInactivityTimeout);
document.addEventListener('focus', resetInactivityTimeout);
document.addEventListener('blur', resetInactivityTimeout);
document.addEventListener('input', resetInactivityTimeout);

// Start the inactivity timeout
resetInactivityTimeout();