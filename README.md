# speech-sep-eval
Speech separation evaluation (speech-sep-eval) enables the evaluation of any method for speech separation. 

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
- [ ] Preprocess: Random RIR preprocess
- [ ] Setup: Download and setup script for LibriSpeech and one other dataset with (splits)
- [ ] Setup: Specify requirements
- [ ] Reporting: Export of results in table
- [ ] Reporting: Visualize examples of waveforms, spectrograms, MFCCs
- [ ] Reporting: Jupyter with best and worst audio files

## Various ideas/considerations
- How much of this can we get from existing repos? How much should we simply wrap those, if they are available?
- Should this be dockerized?
- Should simple baselines be a part of this repo? Like Conv-TasNet or spectral subtraction?
- Impose characteristics for different hardware through filtering (somewhat like RIR)
- Use more advanced metrics than PESQ/STOI, e.g. DESQ, or Helia's measure.
- Impose a heaing impaired characteristics through a model; is it meaningful to add a simplistic "hearing impairment" simulation by filtering based on audiogram? - (chat with Abbie/Torsten/Raul)
- Stratification of performance/fairness through datasets with labelled demographics such as vox-celeb - chat with Pola
- Simple interpretability considerations on DL systems in this? - chat with Laura/Lars
- Interactive demo notebook that records an audio snippet and runs with that in pipeline
- Metric: MFCC MSE?
