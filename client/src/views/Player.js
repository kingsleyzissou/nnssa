import { useHistory } from 'react-router';
import { WaveForm } from '../components/Waveform';
import { Layout } from '../layouts/Layout';

/**
 * Results page view
 * 
 */
export function Player() {

  const history = useHistory();

  let {
    title, artist, album,
    tempo, url, result
  } = history.location.state;

  title = title ? title : 'Untitled';
  artist = artist ? artist : 'Unknown Artist';
  album = album ? album : 'Unknown Album';
  tempo = tempo ? tempo : 0;

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