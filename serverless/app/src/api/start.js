'use strict';
const AWS = require('aws-sdk');
const stepfunctions = new AWS.StepFunctions();

module.exports.start = (event, context, callback) => {
  const stateMachineArn = process.env.statemachine_arn;
  const bucket = event.Records[0].s3.bucket.name;
  const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
  const params = {
    stateMachineArn,
    input: JSON.stringify({ bucket, key })
  };

  return stepfunctions.startExecution(params).promise().then(() => {
    callback(null, `Statemachine ${stateMachineArn} executed successfully`);
  }).catch(error => {
    callback(error.message);
  });
}