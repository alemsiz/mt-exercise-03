#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data

mkdir -p $data

tools=$base/tools

# link default training data for easier access

mkdir -p $data/wikitext-2

for corpus in train valid test; do
    absolute_path=$(realpath $tools/pytorch-examples/word_language_model/data/wikitext-2/$corpus.txt)
    ln -snf $absolute_path $data/wikitext-2/$corpus.txt
done

# download a different interesting data set!

mkdir -p $data/dante

mkdir -p $data/dante/raw

wget https://www.gutenberg.org/files/8800/8800-0.txt
mv 8800-0.txt $data/dante/raw/divine_comedy.txt

# preprocess slightly

cat $data/dante/raw/divine_comedy.txt | python $base/scripts/preprocess_raw.py > $data/dante/raw/divine_comedy.cleaned.txt

# tokenize, fix vocabulary upper bound

head -n 10133 $data/dante/raw/divine_comedy.cleaned.txt | python $base/scripts/preprocess.py --vocab-size 5000 --tokenize --lang "en" > \
    $data/dante/raw/divine_comedy.preprocessed.txt

# split into train, valid and test

head -n 1133 $data/dante/raw/divine_comedy.preprocessed.txt | tail -n 1000 > $data/dante/valid.txt
head -n 2133 $data/dante/raw/divine_comedy.preprocessed.txt | tail -n 1000 > $data/dante/test.txt
head -n 10133 $data/dante/raw/divine_comedy.preprocessed.txt | tail -n 8000 > $data/dante/train.txt
