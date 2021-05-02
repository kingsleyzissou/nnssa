import { useCallback } from 'react';

/**
 * Custom React hook for a helper function
 * that makes the request to Lambda function
 * to receive a presigned URL for an S3 bucket
 * upload 
 * 
 * @returns callback function that makes the request
 * to AWS Lambda function for pre-signed URL
 */
export function useGetPresignedUrl() {
  return useCallback(async ({ name, type }) => {
    try {
      const url = 'https://k4w7a5clng.execute-api.eu-west-1.amazonaws.com/dev/upload';
      // make XHR request
      const response = await fetch(
        new Request(url, {
          method: 'POST',
          body: JSON.stringify({ name, type }),
          headers: new Headers({
            'Content-Type': 'application/json'
          }),
        })
      );
      return response.json();
    } catch (error) {
      console.log(error)
    }
  }, []);
}