'use strict';

const { getSignedUrl } = require("@aws-sdk/s3-request-presigner");
const { S3Client, PutObjectCommand } = require("@aws-sdk/client-s3");

const client = new S3Client({
  region: 'eu-west-1'
});

const getPresignedUploadUrl = async (bucket, directory, filename) => {
  const key = `${directory}/${filename}`;
  const command = new PutObjectCommand({
    Bucket: bucket,
    Key: key,
    ContentType: 'audio/mp3',
  });
  return getSignedUrl(client, command, { expiresIn: 3600 });
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