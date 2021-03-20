'use strict';

const AWS = require('aws-sdk');

AWS.config.update({
  region: 'eu-west-1'
});

const s3 = new AWS.S3();

const getPresignedUploadUrl = async (bucket, directory, filename) => {
  const key = `${directory}/${filename}`;
  return s3
    .getSignedUrl('putObject', {
      Bucket: bucket,
      Key: key,
      ContentType: 'audio/mp3',
    });
}

const sendResponse = (statusCode, body, callback) => {
  callback(null, {
    statusCode,
    headers: { 'Content-Type': 'text/plain' },
    body,
  });
};

module.exports.upload = async (event, context, callback) => {
  const body = JSON.parse(event.body);
  const filename = body.filename;
  const mimeType = body.mimeType;

  if (!mimeType.startsWith('audio/')) {
    console.error('Validation Failed');
    sendResponse(400, 'File upload is not audio.', callback)
    return;
  }

  try {
    const url = await getPresignedUploadUrl('nnssa-songs', 'songs', filename);
    const body = JSON.stringify({
      filename,
      mimeType,
      url,
      message: 'Successfully generated pre-signed S3 upload url'
    });
    sendResponse(200, body, callback);
  } catch (error) {
    const body = JSON.stringify({
      error,
      message: 'There was some kind of error.',
    })
    sendResponse(400, body, callback)
  }
};