# multilingual-sets
Collection of multilingual test sets

We use the CommonVoice [1] test splits and use a simple concatenation to create a multilingual set.
The set is a single audio file of about 2 hours.

As the evaluation of multilingual models is often kept on monolingual utterances our goal is to provide a multilingual test to evaluate multilingual models on a truly multilingual audio how it may occur in meetings, lectures or discussions. Having one large audio which needs to be chunked the data is more challengelling and multilingual than pre chunked monolingual data from monolingual sets.

We provide two test sets.
    1. Each utterance language has to be different from the surrounding ones.
    2. We randomly select a new language and randomly select a span of utterances to stay in the same language before forcing a change of language

Currently our generation script expects to have already download the CommonVoice test splits already and have them saved in a text file, tab seperated columns, with at least the following columns:
    UID AUDIO_PATH  TEXT


We provide files:
    *.uid: Contains utterance ids. We generate them by concatenating client_id with file_name of the audio. This is because clien_ids are not unique
    *.lbl: Contains the concatenated target transcripts we annotate them with the language of the follwing transcript i.e. <en> some text <de> ein Beispiel.

We already prepared the data.
As we can not share this size files on github we provide a script to only append the data.
You need a tab-sperated file with:
    UIDs as describe above: client\_id\_audiofilename (without file extension)
    Path to your audio file saved in 16k samplerate

Then you can execute 
    DO.onlyaudi.sh
script.

TODO
    Work on script to also download the test data and for user to only download the *.lbl *.uids and run the script to generate audio.


#Citations
@article{ardila2019common,
  title={Common voice: A massively-multilingual speech corpus},
    author={Ardila, Rosana and Branson, Megan and Davis, Kelly and Henretty, Michael and Kohler, Michael and Meyer, Josh and Morais, Reuben and Saunders, Lindsay and Tyers, Francis M and Weber, Gregor},
      journal={arXiv preprint arXiv:1912.06670},
        year={2019}
        }
