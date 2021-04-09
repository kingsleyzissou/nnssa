import Loader from 'react-loader-spinner';

export function Loading({ status, step, message }) {
  const [first, second] = step;
  return (
    <>
      <div style={{ textAlign: 'center' }}>
        <Loader
          type="Audio"
          height={60}
          color='#2bffc6'
        />
        <h2 style={{ marginBottom: '0' }}>{status}...</h2>
        <b>{message}</b>
        <p>Step {first} of {second}</p>
      </div>
    </>
  );

}