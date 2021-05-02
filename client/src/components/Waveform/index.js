import { useCallback, useEffect, useRef, useState, useContext } from 'react';
import WaveSurfer from 'wavesurfer.js';
import Markers from 'wavesurfer.js/dist/plugin/wavesurfer.markers';
import styled from 'styled-components';
import classNames from 'classnames';
import { Button } from 'reactstrap';

import xhr from '../../config/xhr';
import { useCreateMarkers } from '../../hooks/createMarkers';
import { ThemeContext } from '../../contexts/ThemeContext';

const Wave = styled.div`
  width: '100%';
  height: '100%';
  position: 'relative';
`;

/**
 * Waveform display component for displaying and playing
 * back the audio from an S3 bucket
 * 
 */
export function WaveForm({ url, result }) {

  const waveform = useRef(null);
  const wavesurfer = useRef(null);
  const [playing, setPlaying] = useState(false);
  const createMarkers = useCreateMarkers();
  const { theme } = useContext(ThemeContext);

  // create the waveform
  const create = useCallback(() => {
    wavesurfer.current = WaveSurfer.create({
      container: waveform.current,
      progressColor: '#fff',
      barWidth: 2,
      barHeight: 1,
      barGap: null,
      plugins: [Markers.create({ markers: [] })],
      hideScrollbar: true,
      xhr,
    });
  }, [wavesurfer])

  // load the song
  const load = useCallback(async () => {
    wavesurfer.current.load(url);
    const markers = createMarkers(result);
    markers.forEach(marker => wavesurfer.current.addMarker(marker));
  }, [wavesurfer, url, result, createMarkers]);

  // check if the component has been mounted first
  useEffect(() => {
    if (waveform && waveform.current) {
      create();
    }
  }, [waveform, create])

  // check if the component has been mounted first
  useEffect(() => {
    if (wavesurfer && wavesurfer.current) {
      load();
    }
  }, [wavesurfer, load])

  // play/pause
  const togglePlayer = useCallback(() => {
    const action = playing ? 'pause' : 'play';
    wavesurfer.current[action]()
    setPlaying(!playing)
  }, [wavesurfer, playing, setPlaying])

  return (
    <>
      <Wave ref={waveform} id="waveform" />
      <Button
        className='mt-4'
        color={classNames({
          'primary': (theme === ''),
          'success': (theme !== '')
        })}
        onClick={togglePlayer}
      >
        {
          playing
            ? 'Pause'
            : 'Play'
        }
      </Button>
    </>
  )
}