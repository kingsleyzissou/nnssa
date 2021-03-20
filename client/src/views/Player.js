import { WaveForm } from '../components/Waveform';
import { Layout } from '../layouts/Layout';

export function Player() {

  return (
    <Layout
      title="Billionaire"
      subtitle={<>Travie McCoy feat. Bruno Mars | <b>Lazarus</b></>}
      text="87 bpm"
      Component={() => <WaveForm />}
    />
  )

}