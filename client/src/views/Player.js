import { useHistory } from 'react-router';
import { WaveForm } from '../components/Waveform';
import { Layout } from '../layouts/Layout';

export function Player() {

  const history = useHistory();

  const {
    title, artist, album,
    tempo, url, result
  } = history.location.state;

  const bpm = Math.round(tempo, 0) + ' bpm';

  return (
    <Layout
      title={title}
      subtitle={<>{artist} | <b>{album}</b></>}
      text={bpm}
      Component={() => <WaveForm url={url} result={result} />}
    />
  )

}