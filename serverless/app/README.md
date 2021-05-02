# Getting Started

Ensure you have setup `serverless` and the AWS cli first. For insructions on how to do this [follow this link](https://www.serverless.com/framework/docs/getting-started/).

## Install dependencies
```
yarn
```

## Set up secrets

Update the `example.secrets.yml` file. Rename it to `secrets.dev.yml` and then run:

```
serverless encrypt --stage dev --password <choose-a-password>  
```

## Deploy

To upload to AWS Lambda run

```
serverless deploy
```