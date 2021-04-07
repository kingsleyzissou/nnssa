import { useCallback } from 'react';

export function useUploadFile() {
  return useCallback(async (url, file) => {
    try {
      const response = await fetch(
        new Request(url, {
          method: 'PUT',
          body: file,
          headers: new Headers({
            'Content-Type': file.type
          }),
        }),
      );
      return response;
    } catch (error) {
      console.log(error)
    }
  }, []);
}