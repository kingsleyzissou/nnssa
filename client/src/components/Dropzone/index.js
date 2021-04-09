import React, { useCallback, useContext } from 'react'
import { useDropzone } from 'react-dropzone'
import { Button } from 'reactstrap';
import { useHistory } from 'react-router';

import { DropContainer, ParentContainer } from './styled';
import { useGetPresignedUrl } from '../../hooks/getPresignedUrl';
import { useUploadFile } from '../../hooks/uploadFile';
import { useSubscribeToTopic } from '../../hooks/subscribeToTopic';
import { NotificationContext } from '../../contexts/NotificationContext';

export function Dropzone({ toggleLoading, loading, setLoading }) {

  const getPresignedUrl = useGetPresignedUrl();
  const uploadFile = useUploadFile();
  const history = useHistory();
  const { onMessage, subscribe, unsubscribe } = useSubscribeToTopic();
  const { notify } = useContext(NotificationContext);

  const handleResult = useCallback((message, type, topic) => {
    notify({ type, message });
    unsubscribe(topic);
    toggleLoading();
  }, [notify, unsubscribe, toggleLoading]);

  const updateLoader = useCallback((message, { status, step }) => {
    setLoading({
      loading: true,
      step,
      status,
      message,
    });
  }, [setLoading]);

  const messageHandler = useCallback((topic, payload) => {
    const response = JSON.parse(payload.toString());
    if (response.statusCode >= 400) {
      handleResult(response.message, 'danger', topic);
      return;
    }
    if (response.data.status !== 'Complete') {
      updateLoader(response.message, response.data);
      return;
    }
    handleResult(response.message, 'success', topic);
    history.push('/player', response.data);
  }, [handleResult, updateLoader, history]);

  const onDrop = useCallback(async ([file]) => {
    updateLoader(loading.message, loading);
    const { url, topic } = await getPresignedUrl(file);
    await subscribe(topic);
    onMessage(messageHandler);
    await uploadFile(url, file);
  }, [onMessage, subscribe, getPresignedUrl, messageHandler, uploadFile, updateLoader, loading])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: 'audio/*',
    multiple: false,
    onDrop,
  })

  const text = isDragActive ? 'Drop the files here ...' :
    'Drag and drop some files here, or click to select files';

  return (
    <ParentContainer {...getRootProps()} >
      <input {...getInputProps()} />
      <DropContainer isActive={isDragActive}>
        <i className="nc-icon x3 nc-layers-3" style={{ color: '#fff' }} />
        <p style={{ color: '#fff', margin: '1em' }}>{text}</p>
        <Button color="primary">Choose File</Button>
      </DropContainer>
    </ParentContainer>
  )
}