---
id: spectrograms
title: Spectrograms
sidebar_label: Spectrograms
slug: /spectrograms
---

## Spectrograms

![](https://github.com/kingsleyzissou/nnssa/raw/main/img/kick_spec.png)

_A spectrogram of a kick drum hit. The intensity of each frequency is indicated by the colour. In this case, we can see the fundamental frequency for the kick drum is quite low_

Spectrograms are a time-frequency domain representation of a digital audio signal. Frequencies are depicted linearly on the y-axis and time is represented on the x-axis and the amplitude of each frequency is represented by the intensity of the colour, giving us information of the frequency over time. Figure 10 gives a clear visual representation of this.

## Mel Spectrograms

![](https://github.com/kingsleyzissou/nnssa/raw/main/img/kick_melspec.png)

_a log mel-spectrogram. The heatmap shows quite clearly that the fundamental frequency is low. Along the Y axis, we can see that the highest frequency marker is 8192 Hz compared to 10000 Hz from the regular spectrogram_

Mel-spectrograms use the same fundamental concept as regular spectrograms, but use the Mel scale for the y-axis of the graph. Mel spectrograms excel in the areas of audio classification, automatic mood recognition, music genre classification and instrument classification (The Sound of AI, 2020a). Mel spectrograms make use of the STFT and therefore give a time-frequency domain representation of a song.
