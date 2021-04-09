import { useCallback, useEffect, useRef, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';
import Markers from 'wavesurfer.js/dist/plugin/wavesurfer.markers';
import styled from 'styled-components';
import { Button } from 'reactstrap';

import xhr from '../../config/xhr';
import { useCreateMarkers } from '../../hooks/createMarkers';

const Wave = styled.div`
  width: '100%';
  height: '100%';
  position: 'relative';
`;

export function WaveForm({ url, result }) {

  const waveform = useRef(null);
  const wavesurfer = useRef(null);
  const [playing, setPlaying] = useState(false);
  const createMarkers = useCreateMarkers();

  const create = useCallback(() => {
    wavesurfer.current = WaveSurfer.create({
      container: waveform.current,
      progressColor: '#fff',
      barWidth: 2,
      barHeight: 1,
      barGap: null,
      plugins: [Markers.create({ markers: [] })],
      xhr,
    });
  }, [wavesurfer])

  const load = useCallback(async () => {
    wavesurfer.current.load(url);
    const markers = createMarkers(result);
    markers.forEach(marker => wavesurfer.current.addMarker(marker));
  }, [wavesurfer, url, result, createMarkers]);

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

  const togglePlayer = useCallback(() => {
    const action = playing ? 'pause' : 'play';
    wavesurfer.current[action]()
    setPlaying(!playing)
  }, [wavesurfer, playing, setPlaying])

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