import React, { useCallback, useContext } from 'react'
import { useDropzone } from 'react-dropzone'
import { Button } from 'reactstrap';
import { useHistory } from 'react-router';
import classNames from 'classnames';

import { DropContainer, ParentContainer } from './styled';
import { useGetPresignedUrl } from '../../hooks/getPresignedUrl';
import { useUploadFile } from '../../hooks/uploadFile';
import { useSubscribeToTopic } from '../../hooks/subscribeToTopic';
import { NotificationContext } from '../../contexts/NotificationContext';
import { ThemeContext } from '../../contexts/ThemeContext';

/**
 * DropZone component for dragging and dropping files
 * and then uploading to Amazon S3 bucket
 *  
 */
export function Dropzone({ toggleLoading, loading, setLoading }) {

  const getPresignedUrl = useGetPresignedUrl();
  const uploadFile = useUploadFile();
  const history = useHistory();
  const { onMessage, subscribe, unsubscribe } = useSubscribeToTopic();
  const { notify } = useContext(NotificationContext);
  const { theme } = useContext(ThemeContext);

  const handleResult = useCallback((message, type, topic) => {
    // send toast notification
    notify({ type, message });
    // unsubscribe from MQTT topic
    unsubscribe(topic);
    toggleLoading();
  }, [notify, unsubscribe, toggleLoading]);

  // set loader to active
  const updateLoader = useCallback((message, { status, step }) => {
    setLoading({
      loading: true,
      step,
      status,
      message,
    });
  }, [setLoading]);

  // handle update/error/result message
  const messageHandler = useCallback((topic, payload) => {
    const response = JSON.parse(payload.toString());
    if (response.statusCode >= 400) {
      // send error toast if there was an error
      handleResult(response.message, 'danger', topic);
      return;
    }
    if (response.data.status !== 'Complete') {
      // handle the result and exit
      updateLoader(response.message, response.data);
      return;
    }
    // send update
    handleResult(response.message, 'success', topic);
    history.push('/player', response.data);
  }, [handleResult, updateLoader, history]);

  // handle the drag and drop event
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
        <i
          className={classNames(
            'nc-icon x3 nc-layers-3',
            {
              'text-dark': (theme !== ''),
              'text-white': (theme === '')
            }
          )}
        />
        <p
          className={classNames('m-4', {
            'text-dark': (theme !== ''),
            'text-white': (theme === '')
          })}
        >
          {text}
        </p>
        <Button
          color={classNames({
            'primary': (theme === ''),
            'success': (theme !== '')
          })}
        >
          Choose File
        </Button>
      </DropContainer>
    </ParentContainer>
  )
}