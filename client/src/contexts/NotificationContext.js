import { createContext } from 'react';
import NotificationAlert from 'react-notification-alert';
import { useNotification } from '../hooks/notifyProgress';

export const NotificationContext = createContext({
  notify: () => { },
});

export function NotificationContextWrapper({ children }) {
  const { ref, notify } = useNotification();

  return (
    <NotificationContext.Provider value={{ notify }}>
      <NotificationAlert ref={ref} />
      {children}
    </NotificationContext.Provider>
  );
}