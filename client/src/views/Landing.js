import { useCallback, useState } from 'react';
import { Layout } from '../layouts/Layout';
import { Dropzone } from '../components/Dropzone';
import { Loading } from '../components/Loading';

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
      title="Title"
      subtitle="Lorem ipsum"
      text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
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