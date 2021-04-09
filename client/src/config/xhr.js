const xhr = {
  cache: 'no-cache',
  mode: 'cors',
  method: 'GET',
  headers: new Headers({
    'Content-Type': 'text/plain',
    'Accept': '*/*',
    'Origin': window.location.origin,
  })
};

export default xhr;