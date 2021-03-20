import { useState } from 'react';
import { Landing } from './views/Landing';
import { Player } from './views/Player';

function App() {

  const [landing, setLanding] = useState(true);

  if (landing) return <Landing setLanding={setLanding} />;

  return <Player />;
}

export default App;
