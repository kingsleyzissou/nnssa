import React from 'react';
import ReactDOM from 'react-dom';

import reportWebVitals from './reportWebVitals';

import '@fortawesome/fontawesome-free/css/all.min.css';
import 'react-loader-spinner/dist/loader/css/react-spinner-loader.css';
import './assets/css/black-dashboard-react.min.css';
import './assets/demo/demo.min.css';
import './assets/css/nucleo-icons.min.css';
import './assets/css/nucleo-public.min.css';
import './index.css';

import App from './App';
import { ThemeContextWrapper } from './contexts/ThemeContext';
import { NotificationContextWrapper } from './contexts/NotificationContext';

ReactDOM.render(
  <ThemeContextWrapper>
    <NotificationContextWrapper>
      <App />
    </NotificationContextWrapper>
  </ThemeContextWrapper>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
