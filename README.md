# speech-sep-eval
Speech separation evaluation (speech-sep-eval) enables the evaluation of any method for speech separation. 

The speech-sep-eval evaluates a speech separation models ability to process a mixture signal, consisting of a target speech signal and interferring signals, and output a single target speech signal. The considered interference can be e.g. other speakers (speaker separation) or classic examples of stationary noise (speech enhancement). The comprehensive evaluation seeks to address issues with limited evaluation by enabling an easy-to-use pipeline that enables a multi-dimensional evaluation on e.g. unseen data in reverberent environments.

After having run an setup script, you setup a pipeline: (a) choose datasets to evaluate on, (b) choose which pre-processings to compare, (c) you provide the models, (d) choose post-processing, (e) choose which metrics to calculate, and (f) choose how to report the results. 

![](./resources/speech-sep-eval.png)
