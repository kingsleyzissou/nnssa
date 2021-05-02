---
id: fourier-transforms
title: Fourier Transforms
sidebar_label: Fourier Transforms
slug: /fourier-transforms
---

## Fourier Transform

![](https://miro.medium.com/max/942/1*uL4gqMutokf5r-M8P7bG7w.png)

_A visual representation of waveforms being split by their frequency and converted using the Fourier transform (Dubey, 2018)_

Taking an audio signal representation from the time-domain to the frequency-domain is not a trivial task. It requires a complex mathematical algorithm known as the Fourier transform to achieve this (Mu ̈ller, 2016). Since digital audio signals are a discrete representation of a continuous analogue signal, the underlying transform that will be used is the Discrete Fourier Transform (Chaudhary, 2020). Due to computational complexity of the Discrete Fourier transform, a slightly modified ver- sion, known as the Fast Fourier transform (FFT), is more frequently used used (Dubey, 2018).

## Short-time Fourier Transform (STFT)

In order to calculate an SFTF, an audio signal is split up into equal size, overlapping windows and a Fast Fourier transform is then applied to each window. Rather than reporting the frequency
averaged over time, the STFT reports the frequency variation over time, giving us a time-frequency domain representation of a signal (Kehtarnavaz, 2008). The STFT is used the underlying transform used to generate spectrograms and mel spectrograms.
