'use strict';

const { getSignedUrl } = require("@aws-sdk/s3-request-presigner");
const { S3Client, PutObjectCommand } = require("@aws-sdk/client-s3");
const path = require('path');

const client = new S3Client({
  region: 'eu-west-1'
});

const getPresignedUploadUrl = async (bucket, directory, filename, mime) => {
  const key = `${directory}/${filename}`;
  const command = new PutObjectCommand({
    Bucket: bucket,
    Key: key,
    ContentType: mime,
    ACL: 'public-read',
  });
  return getSignedUrl(client, command, { expiresIn: 3600 });
}

const sendResponse = (statusCode, body, callback) => {
  callback(null, {
    statusCode,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Credentials': true
    },
    body,
  });
};

module.exports.upload = async (event, context, callback) => {
  const body = JSON.parse(event.body);
  const mime = body.type;
  const { name: songname, base: filename } = path.parse(body.name);

  if (!mime.startsWith('audio/')) {
    console.error('Validation Failed');
    sendResponse(400, 'File upload is not audio.', callback)
    return;
  }

  try {
    const url = await getPresignedUploadUrl('nnssa-songs', 'songs', filename, mime);
    const body = JSON.stringify({
      filename,
      mime,
      url,
      topic: `nnssa/${songname}`,
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