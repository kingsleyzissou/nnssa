import { useCallback, useRef } from 'react';

/**
 * Custom React hook for displaying toast
 * notification alerts
 * 
 * @returns an object with a notifcation callback
 * and a ref to the toast alert
 */
export function useNotification() {
  const ref = useRef();

  /**
   * Check if alert is error or success
   */
  const getAlertType = useCallback((type) => {
    if (type === 'danger') return 'Error';
    if (type === 'success') return 'Success';
    return 'Update';
  }, []);

  /**
   * Error/Success icon
   */
  const getIcon = useCallback((type) => {
    if (type === 'danger') return 'tim-icons icon-alert-circle-exc';
    if (type === 'success') return 'tim-icons icon-check-2';
    return 'tim-icons icon-sound-wave';
  }, []);

  /**
   * Display the message
   */
  const getMessage = useCallback((type, message) => {
    const text = getAlertType(type);
    return (
      <span>
        <b>{text}</b><br />
        {message}
      </span>
    );
  }, [getAlertType]);

  /**
   * Set toast options
   */
  const getOptions = useCallback((type, message) => ({
    place: 'tr',
    message: getMessage(type, message),
    type,
    autoDismiss: 4,
    closeButton: false,
    icon: getIcon(type)
  }), [getMessage, getIcon]);

  /**
   * Notify callback for the toast alert
   */
  const notify = useCallback(({ type, message }) => {
    if (ref.current) {
      const options = getOptions(type, message);
      ref.current.notificationAlert(options);
    }
  }, [ref, getOptions]);

  return { ref, notify };
}
