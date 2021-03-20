import React, { useCallback } from 'react'
import { useDropzone } from 'react-dropzone'
import { Button } from 'reactstrap';

import { DropContainer, ParentContainer } from './styled';

export function Dropzone({ setLanding }) {
  const onDrop = useCallback(async ([file]) => {
    // Do something with the files
    // setLanding(false);

    const presignedUploadUrl = '';
    try {
      const response = await fetch(
        new Request(presignedUploadUrl, {
          method: 'PUT',
          body: file,
          headers: new Headers({
            'Content-Type': 'audio/mp3'
          }),
        }),
      );
      console.log(response)
    } catch (error) {
      console.log(error)
    }
    setLanding(false)
  }, [setLanding])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: 'audio/*',
    onDrop
  })

  const text = isDragActive ? 'Drop the files here ...' :
    'Drag \'n\' drop some files here, or click to select files';

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