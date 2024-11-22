const deleteForms = document.getElementsByClassName('deleteForm');

for (let i = 0; i < deleteForms.length; i++) {
    let form = deleteForms[i];
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        let id = event.target.id.slice(-1);
        console.log(id);
        fetch('/process', {
            method: 'POST',
            body: {'id': id}
        });
    });
}

// document.getElementsByClassName('deleteForm').addEventListener('submit', function(event) {
//     event.preventDefault();
//     console.log(this);
// });

// document.getElementById('deleteForm1').addEventListener('submit', function(event) {
//     event.preventDefault();
//     console.log(this);
//     const formData = new FormData(event.target);
//     console.log(formData);
//     fetch('/process', {
//         method: 'POST',
//         body: 'hello'
//     })
//     // .then(response => response.json())
//     // .then(data => {
//     //     document.getElementById('result').textContent = 'Result: ' + data.result;
//     // })
//     // .catch(error => console.error('Error:', error));
// });