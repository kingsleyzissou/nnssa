import { useCallback } from 'react';

/**
 * Custom react hook that provides the ability
 * to create dynamic song boundary markers.
 * 
 * @returns a callback function for creating 
 * song boundary markers
 */
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