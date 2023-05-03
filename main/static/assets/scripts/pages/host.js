let form = document.querySelector('#upload');
let file = document.querySelector('#file');

form.addEventListener('submit', handleSubmit);

function handleSubmit (event) {

	// Stop the form from reloading the page
	event.preventDefault();

	// If there's no file, do nothing
	if (!file.value.length) return;


    let reader = new FileReader();

    // Setup the callback event to run when the file is read
	reader.onload = logFile;
    // Read the file
	reader.readAsText(file.files[0]);


}


function logFile (event) {
	let str = event.target.result;
	let json = JSON.parse(str);
	// console.log('string', str);
	// console.log('json', json);


   
    // console.log(json.length)
  
    // ports = []
    for(let i = 0; i < json.length; i++){
        console.log(json[i].ip)
        
        for(let x = 0; x < json[i].ports.length; x++){
            $.ajax({
                url: "/uploadhosts/",
                type: "POST",
                data: {
                    host_ip:    json[i].ip,
                    portid:     json[i].ports[x].portid,
                    state:      json[i].ports[x].state,
                    protocol:   json[i].ports[x].protocol,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        
                },
        
                success: function(response){
                    console.log("1 host saved")
                },
                error: function(response){
                                   
                    console.log(response)
                }
            })
            
            // console.log("portID: " ,portid, "state: ", state, "protocol: ",protocol)
           
           
        }
        // console.log(host,totall_ports)
        
        
        
    }
}