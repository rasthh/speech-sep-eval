# speech-sep-eval
Speech separation evaluation (speech-sep-eval) enables the evaluation of any method for speech separation. 

The speech-sep-eval evaluates a speech separation models ability to process a mixture signal, consisting of a target speech signal and interferring signals, and output a single target speech signal. The considered interference can be e.g. other speakers (speaker separation) or classic examples of stationary noise (speech enhancement).

The comprehensive evaluation seeks to address issues with limited evaluation by enabling an easy-to-use pipeline that enables a multi-dimensional evaluation on e.g. unseen data in reverberent environments.

After having run an setup script, the idea is to be provide (a) a list of models, (b) a series of metrics, (c) pre-processing, and (d) a series of datasets. The repo will then report and visualize the results. 

## TODO
- [ ] Evaluation interface (supply models, choose metrics/preprocessing/datasets)
- [ ] Class to wrap metrics
- [ ] Class to wrap preprocessing
- [ ] Class to wrap dataset
- [ ] Class to wrap "input model to be evaluated"
- [ ] Class to wrap evaluation report
- [ ] Setup simple testing of code as a starting point.
- [ ] Metric: SI-SNR
- [ ] Metric: SDR
- [ ] Metric: Waveform MSE
- [ ] Metric: Spectrogram MSE
- [ ] Metric: PESQ
- [ ] Metric: STOI
- [ ] Preprocess: Identity-mapping
- [ ] Preprocess: Additive mixture
- [ ] Preprocess: Random RIR mixture
- [ ] Preprocess: Noise addition parametrized by desired SNR(-ranges)
- [ ] Setup: Download and setup script for LibriSpeech and one other dataset with (splits)
- [ ] Setup: Download and setup script for classic noise datasets (publicly available, but like ICRA)
- [ ] Setup: Specify pip requirements
- [ ] Reporting: Export of results in table
- [ ] Reporting: Visualize examples of waveforms, spectrograms, MFCCs
- [ ] Reporting: Auralize examples of best/worst performance

## Various ideas/considerations
- Metric: ASR improvement based on ESPNet/Kaldi
- How much of this can we get from existing repos? How much should we simply wrap those, if they are available? https://github.com/espnet/espnet and http://kaldi-asr.org/doc/about.html.
- Download and setup script for music datasets (publicly available), television, something like AudioSet, or even examples of various acoustics scenes from a scene classification task. 
- Should this be dockerized?
- Should simple baselines be a part of this repo? Like Conv-TasNet or spectral subtraction?
- Impose characteristics for different hardware through filtering (somewhat like RIR)
- Use more advanced metrics than PESQ/STOI, e.g. [DESQ](https://ieeexplore.ieee.org/document/8682754), or [Helia's measure](https://asa.scitation.org/doi/abs/10.1121/1.5129114).
- Impose a heaing impaired characteristics through a model; is it meaningful to add a simplistic "hearing impairment" simulation by filtering based on audiogram? - (chat with Abbie/Torsten/Raul)
- Stratification of performance/fairness through datasets with labelled demographics such as vox-celeb - chat with Pola
- Simple interpretability considerations on DL systems in this? - chat with Laura/Lars
- Interactive demo notebook that records an audio snippet and runs with that in pipeline
- Metric: MFCC MSE, or other known acoustic features and their change; e.g. F0
- Interface for simple MOS-evaluation and SRT-evaluation, for illustration.
