# Multilingual Sets

This repository is a collection of multilingual test sets. The test sets are generated using the CommonVoice [Common Voice](https://arxiv.org/pdf/1912.06670.pdf) test splits, and a simple concatenation technique is employed to create a multilingual set. The resulting set is a single audio file of approximately 2 hours.

The motivation behind this collection is to provide a multilingual test environment for evaluating multilingual models. Often, the evaluation of multilingual models is performed on monolingual utterances. The goal here is to offer a truly multilingual audio set, resembling scenarios such as meetings, lectures, or discussions. By having a large audio file that needs to be chunked, the data becomes more challenging and representative of real-world multilingual scenarios compared to pre-chunked monolingual data from monolingual sets.

## How we generated Test sets

1. **Distinct Language Utterances:**
   - Each utterance language has to be different from the surrounding ones.

2. **Random Language Spans:**
      - We randomly select a new language and randomly select a span of utterances to stay in the same language before forcing a change of language.

    ## Usage

      The generation script expects you to have already downloaded the CommonVoice test splits and saved them in a text file with tab-separated columns, including at least the following columns:

      ```plaintext
      UID | AUDIO_PATH | TEXT

## Usage/Provided Files

  ## Prepared Data

  We have already prepared the data. However, due to the size of these files, we are unable to share them directly on GitHub. Instead, we provide a script to append the data.

  - **.uid:**
    Contains utterance IDs. Generated by concatenating `client_id` with `file_name` of the audio using "_". Necessary because `client_ids` are not unique.

    - **.lbl:**
    Contains the concatenated target transcripts annotated with the language of the following transcript. (e.g., `<en> some text <de> ein Beispiel`).


  ### Usage

    To append your own data, you need a tab-separated file with:

    1. UIDs as described above: `client_id_audiofilename` (without file extension).
    2. Path to your audio file saved in 16k samplerate.

    Then, execute the following script:

    ```bash
    sh DO.onlyaudio.sh



# TODO

## Downloading Test Data

We are actively working on a script to facilitate the download of the test data. Once the script is available, users will have the convenience of downloading only the `*.lbl` and `*.uids` files. After downloading these files, running the provided script will generate the corresponding audio.

Stay tuned for updates on this feature!


# Citations

@article{ardila2019common,
  title={Common voice: A massively-multilingual speech corpus},
    author={Ardila, Rosana and Branson, Megan and Davis, Kelly and Henretty, Michael and Kohler, Michael and Meyer, Josh and Morais, Reuben and Saunders, Lindsay and Tyers, Francis M and Weber, Gregor},
      journal={arXiv preprint arXiv:1912.06670},
        year={2019}
        }
