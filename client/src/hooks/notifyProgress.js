import { useCallback, useRef } from 'react';

export function useNotification() {
  const ref = useRef();

  const getAlertType = useCallback((type) => {
    if (type === 'danger') return 'Error';
    if (type === 'success') return 'Success';
    return 'Update';
  }, []);

  const getIcon = useCallback((type) => {
    if (type === 'danger') return 'tim-icons icon-alert-circle-exc';
    if (type === 'success') return 'tim-icons icon-check-2';
    return 'tim-icons icon-sound-wave';
  }, []);

  const getMessage = useCallback((type, message) => {
    const text = getAlertType(type);
    return (
      <span>
        <b>{text}</b><br />
        {message}
      </span>
    );
  }, [getAlertType]);

  const getOptions = useCallback((type, message) => ({
    place: 'tr',
    message: getMessage(type, message),
    type,
    autoDismiss: 4,
    closeButton: false,
    icon: getIcon(type)
  }), [getMessage, getIcon]);

  const notify = useCallback(({ type, message }) => {
    if (ref.current) {
      const options = getOptions(type, message);
      ref.current.notificationAlert(options);
    }
  }, [ref, getOptions]);

  return { ref, notify };
}
