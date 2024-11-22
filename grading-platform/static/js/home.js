document.getElementById('deleteForm').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log(event);
    const formData = new FormData(event.target);
    console.log(formData);
    fetch('/process', {
        method: 'POST',
        body: formData
    })
    // .then(response => response.json())
    // .then(data => {
    //     document.getElementById('result').textContent = 'Result: ' + data.result;
    // })
    // .catch(error => console.error('Error:', error));
});