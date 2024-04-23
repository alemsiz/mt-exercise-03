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

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh

# Modifications for Part 1

All major modifications for this part of the exercise were made in `download_data.sh`.

Firstly, I changed all the file names to reflect the name of the new dataset (from `grimm` to `dante`).

I then edited the `wget` command to fetch Dante’s Divine Comedy from Project Gutenberg.

For the raw processing, I input the entire original text file taken from Project Gutenberg to `preprocess_raw.py`, and generated a cleaned file of 14442 lines. Since the final preprocessed data set should contain between 5000 and 10000 segments (lines), I then edited the script so that only the first 10133 lines were input to `preprocessing.py`. I chose this number because the first 133 lines of the cleaned text were preamble, meaning that after skipping these I would have 10000 lines to distribute between the training, validation and testing datasets.

I also edited the command to run `preprocess.py` to remove the `--sent-tokenize` flag, since my chosen text is a poem and so sentences are intentionally split across different lines. In order for the model-generated content to reflect the original text, I wanted to preserve these line breaks in the preprocessed data.

This data split is then created in the final three lines of the code, where testing and validation receive 1000 lines each and training receives 8000.

The only other minor modifications I made were to the filenames (`grimm` > `dante`) in `train.sh` and `generate.sh`.


