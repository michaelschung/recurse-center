import React, { useEffect, useState } from 'react';

const App = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        fetch('/data')
            .then(response => response.json())
            .then(json => setData(json.val))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Database Value:</h1>
            <p>{data ? data : 'Loading...'}</p>
        </div>
    );
};

export default App;
