const deleteForms = document.getElementsByClassName('deleteForm');

for (let i = 0; i < deleteForms.length; i++) {
    let form = deleteForms[i];
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        let id = event.target.id.slice(-1);
        console.log(formData);
        fetch('/process', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: id
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('RESPONSE HANDLER');
            console.log(data);
            location.reload();
        })
        .catch(error => console.error('Error:', error));
    });
}

document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    fetch('/process', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = 'Result: ' + data.result;
    })
    .catch(error => console.error('Error:', error));
});