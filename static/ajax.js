// event handler
$('#get-human').on('submit', (evt) => {
    evt.preventDefault();

    // get form input 
    const formData = {
        'human_id': $('#human-id').val()
    }

    // send data to server.py
    $.get(`/api/human/${formData.human_id}`, formData, (res) => {
        // display response
        if (res.status === 'success') {
            $('#fname').text(res.fname);
            $('#lname').text(res.lname);
            $('#email').text(res.email);
        } else if (res.status === 'error') {
            alert(res.status);
        } 
    });
});