function deleteGrade(button) {
    // Get grade_id of row
    const i = button.parent().parent().children()[2].innerHTML;
    console.log(i);
    fetch('/deleteGrade', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            id: i
        })
    })
    .then(response => response.json())
    .then(data => responseHandler(data))
    .catch(error => console.error('Error:', error));
}

document.getElementById('newGradeForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/addGrade', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => responseHandler(data))
});

function responseHandler(data) {
    console.log('RESPONSE HANDLER');
    console.log(data);
    location.reload();
}