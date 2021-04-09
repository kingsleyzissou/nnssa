import { useCallback } from 'react';

export function useCreateMarkers() {
  return useCallback((results) => {
    return results.map((time, index) => {
      const position = (index % 2 === 0) ? 'top' : 'bottom'
      return {
        time,
        color: '#2bffc6',
        position
      }
    })
  }, []);
}