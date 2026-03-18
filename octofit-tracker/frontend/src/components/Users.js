import React, { useState, useEffect } from 'react';

function Users() {
  const [data, setData] = useState([]);
  const codespaceHost = typeof window !== 'undefined' ? window.location.hostname : '';
  const codespaceBase = codespaceHost.endsWith('-3000.app.github.dev')
    ? `https://${codespaceHost.replace('-3000.app.github.dev', '-8000.app.github.dev')}`
    : null;
  const baseUrl = process.env.REACT_APP_CODESPACE_NAME
    ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev`
    : codespaceBase || 'http://localhost:8000';
  const apiUrl = `${baseUrl}/api/users/`;

  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const items = data.results || data;
        setData(items);
        console.log('Fetched data:', items);
      })
      .catch(err => console.error('Fetch error', apiUrl, err));
  }, [apiUrl]);

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {data.map(item => <li key={item.id}>{JSON.stringify(item)}</li>)}
      </ul>
    </div>
  );
}

export default Users;