import { useCallback, useEffect, useRef, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';
import Markers from 'wavesurfer.js/dist/plugin/wavesurfer.markers';
import styled from 'styled-components';
import { Button } from 'reactstrap';

import { markers } from '../../variables/constants';

const Wave = styled.div`
  width: '100%';
  height: '100%';
  position: 'relative';
`;

export function WaveForm() {

  const waveform = useRef(null);
  const wavesurfer = useRef(null);
  const [playing, setPlaying] = useState(false);

  const create = useCallback(() => {
    wavesurfer.current = WaveSurfer.create({
      container: waveform.current,
      progressColor: '#fff',
      barWidth: 2,
      barHeight: 1,
      barGap: null,
      plugins: [Markers.create({ markers: [] })]
    });
  }, [wavesurfer])

  const load = useCallback(() => {
    markers.forEach(marker => wavesurfer.current.addMarker(marker));
    wavesurfer.current.load('/0024_billionaire.wav');
  }, [wavesurfer]);

  useEffect(() => {
    if (waveform && waveform.current) {
      create();
    }
  }, [waveform, create])

  useEffect(() => {
    if (wavesurfer && wavesurfer.current) {
      load()
    }
  }, [wavesurfer, load])

  const togglePlayer = () => {
    const action = playing ? 'pause' : 'play';
    wavesurfer.current[action]()
    setPlaying(!playing)
  }

  return (
    <>
      <Wave ref={waveform} id="waveform" />
      <Button color="primary" onClick={togglePlayer}>
        {
          playing
            ? 'Pause'
            : 'Play'
        }
      </Button>
    </>
  )
}