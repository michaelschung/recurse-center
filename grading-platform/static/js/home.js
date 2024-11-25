function deleteGrade(button) {
    // Get grade_id of row
    const i = button.parent().parent().children()[2].innerHTML;
    fetch('/process', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            id: i
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('RESPONSE HANDLER');
        console.log(data);
        location.reload();
    })
    .catch(error => console.error('Error:', error));
}