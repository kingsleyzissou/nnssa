import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom';
import { Landing } from './views/Landing';
import { Player } from './views/Player';

const style = {
  'height': '100vh',
  'width': '100vw',
  'display': 'flex',
  'justifyContent': 'center',
  'alignItems': 'center'
};

export default function App() {
  return (
    <div style={style}>
      <div style={{ display: 'block', width: '50%' }}>
        <Router>
          <Switch>
            <Route path="/player">
              <Player />
            </Route>
            <Route path="/">
              <Landing />
            </Route>
          </Switch>
        </Router>
      </div>
    </div>
  )
}
