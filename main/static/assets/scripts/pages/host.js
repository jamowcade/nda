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