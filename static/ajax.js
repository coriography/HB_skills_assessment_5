// add event listener
//In the event handler (the callback function), retrieve the ID number that the user selected

// Use that ID number to send a GET request to /api/human/<human_id>

// Use data from the server to update the contents of #fname, #lname, and #email with their appropriate values

$('#get_human').on('submit', (evt) => {
    evt.preventDefault();

    // get form input 
    const formData = {
        'human_id': $('#human_id').val()
    }
    $('#fname').text(formData);
    console.log(formData);

    // send data to server.py
    $.post('/api/human/<human_id>', formData, function (res) {
        // display response
        if (res.status === 'success') {
            alert(res.status);
            $('#fname').text(res.fname);
            $('#lname').text(res.lname);
            $('#email').text(res.email);
        } else if (res.status === 'error') {
            alert(res.status);
        } else {
            alert('mega fail');
        }
    });
});