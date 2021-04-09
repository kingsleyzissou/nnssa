import { useCallback } from 'react';

export function useGetPresignedUrl() {
  return useCallback(async ({ name, type }) => {
    try {
      const url = 'https://k4w7a5clng.execute-api.eu-west-1.amazonaws.com/dev/upload';
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