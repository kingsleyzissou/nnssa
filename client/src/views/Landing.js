import { useCallback, useState } from 'react';
import { Layout } from '../layouts/Layout';
import { Dropzone } from '../components/Dropzone';
import { Loading } from '../components/Loading';

/**
 * Landing page view
 * 
 */
export function Landing() {

  const [loading, setLoading] = useState({
    loading: false,
    status: 'Uploading',
    message: 'Uploading file to Amazon S3',
    step: [1, 7]
  });

  const toggleLoading = useCallback(() => {
    setLoading({
      ...loading,
      loading: false,
    });
  }, [loading, setLoading]);

  if (loading.loading) return (
    <Loading
      status={loading.status}
      message={loading.message}
      step={loading.step}
    />
  )

  return (
    <Layout
      title="NNSSA"
      subtitle="Welcome"
      text="NNSSA is a convolutional neural network based algortithm that aims to predict \n the transition points, or boundaries, in a song. Upload a song on the dropzone below"
      Component={() => (
        <Dropzone
          loading={loading}
          toggleLoading={toggleLoading}
          setLoading={setLoading}
        />
      )}
    />
  )

}