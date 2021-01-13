---
id: compression-analysis
title: Compression Analysis
sidebar_label: Compression Analysis
slug: /compression-analysis
---

![Waveform comparison][wave]

YouTube compresses the audio for videos quite heavily using Lossy Compression. This essentially means that the compression is applied in a destructive manner and can’t be reversed. It is unclear what effect this might have on the training of the neural network. To investigate this, I took a high quality audio file, uploaded it to YouTube and then downloaded the compressed audio file. I then did a side-by-side comparison of the YouTube file with the original using 2 mel-spectrograms. I then leveraged phase cancellation to try to get a more quantifiable measure of the difference in the audio. I inverted the phase of the compressed file and lined it up with the audio from the original quality audio. The phase cancellation results in an audio file that reveals the differences in the two audio files. This process is the backbone of active noise-cancellation used in noise-cancelling headphones for example (Triggs, 2020).

![Mel Spectrogram comparison][mel]

Both images in this section show that the difference between the original audio and the compressed audio is small enough that I would be satisfied working with the YouTube quality audio. Additionally, in a survey published in the New Review in Hypermedia Multimedia journal in 2014, it was found that compressed audio was sufficient for music information retrieval, with the added benefit of reducing costs (Zampoglou and Malamos, 2014).

[wave]: https://github.com/kingsleyzissou/nnssa/raw/main/img/wav_comparison.png "Waveform comparison"
[mel]: https://github.com/kingsleyzissou/nnssa/raw/main/img/mel_comparison.png "Mel Spectrogram Comparison"
