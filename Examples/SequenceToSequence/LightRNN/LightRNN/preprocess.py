# =============================================================================
# copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root
# for full license information.
# ==============================================================================

import argparse
import os

from converter import generate_vocab_from_source_file
from converter import init_location
from converter import save_to_vocab_location_file
from converter import save_to_vocab_file

parser = argparse.ArgumentParser(description="Language Model with LightRNN")

parser.add_argument('-datadir', '--datadir', default=None, required=True,
                    help='Data Directory where the dataset is located')
parser.add_argument('-outputdir', '--outputdir', default=None, required=True,
                    help='Vocab directory put word allocation and vocab file')
parser.add_argument('-vocab_file', '--vocab_file', default='vocab.txt',
                    help='The file name of vocab file')
parser.add_argument('-alloc_file', '--alloc_file', default='word-0.location',
                    help='The file name of word allocation table')
parser.add_argument('-vocabsize', '--vocabsize', default=10000, type=int,
                    help='The vocab size')

opt = parser.parse_args()


def preprocess():
    # Generate the vocabulary and location
    vocab = generate_vocab_from_source_file(opt.datadir, opt.vocabsize)
    save_to_vocab_file(vocab, os.path.join(opt.outputdir, opt.vocab_file))
    location = init_location(vocab)
    save_to_vocab_location_file(location, os.path.join(opt.outputdir, opt.alloc_file))


def main():
    preprocess()


if __name__ == '__main__':
    main()
