# MT Exercise 3: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-03
    cd mt-exercise-03

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

Various parameters can be altered in this script, e.g. to change the dropout rate please change the value after `--dropout`.

If you wish to produce a log file containing the training and validation perplexities for each epoch of training, please add the `--log-ppl` flag to the command line arguments. In this case, you will also need to indicate a filepath to store the results using the `--results` argument.

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh

# Modifications for Part 1

All major modifications for this part of the exercise were made in `download_data.sh`.

Firstly, I changed all the file names to reflect the name of the new dataset (from `grimm` to `dante`).

I then edited the `wget` command to fetch Dante’s Divine Comedy from Project Gutenberg.

For the raw processing, I input the entire original text file taken from Project Gutenberg to `preprocess_raw.py`, and generated a cleaned file of 14442 lines. Since the final preprocessed data set should contain between 5000 and 10000 segments (lines), I then edited the script so that only the first 10133 lines were input to `preprocess.py`. I chose this number because the first 133 lines of the cleaned text were preamble, meaning that after skipping these I would have 10000 lines to distribute between the training, validation and testing datasets.

I also edited the command to run `preprocess.py` to remove the `--sent-tokenize` flag, since my chosen text is a poem and so sentences are intentionally split across different lines. In order for the model-generated content to reflect the original text, I wanted to preserve these line breaks in the preprocessed data.

This data split is then created in the final three lines of the code, where testing and validation receive 1000 lines each and training receives 8000.

The only other minor modifications I made were to the filenames (`grimm` > `dante`) in `train.sh` and `generate.sh`.

# Modifications for Part 2

I edited `/tools/pytorch-examples/word language model/main.py` by adding two new parser arguments: `--log-ppl` (a flag indicating that the training and validation perplexities should be saved in a log CSV file as they are calculated during training) and `--results` (the path to save the log file to).

The necessary amendments were then made to the rest of the script to create and populate this log file, storing the training and validation perplexities at each epoch.

In light of these changes to the training script, I also edited `/scripts/train.sh` in order to create log files for the models I trained. Namely, I added the new flag `--log-ppl` to the command line arguments and also my desired log file name in `--results`. I also edited the dropout value for each of the 5 models I trained (models were trained for the following dropout values: 0, 0.2, 0.4, 0.6, 0.8) - trained models can be found in the `models` folder.


