
import random
import os
import argparse
import ast
import numpy as np
import soundfile as sf

parser = argparse.ArgumentParser()
parser.add_argument('-stms', nargs='+', help="path to test sets", type=str, required=True)
parser.add_argument('-uids', help="file containing utterance ids", type=str, required=True)
parser.add_argument('-ididx', help='column index of utterance id', type=int, default=0)
parser.add_argument('-wavidx', help='column index of path to audio file', type=int, default=1)
parser.add_argument('-outa', help="output audio file", type=str)
args = parser.parse_args()


random.seed(66)

stm_sets = {}
used_ids = {}
for stm_file in args.stms:
    with open(stm_file, "r") as stmf:
        for line  in stmf:
            line = line.strip()
            tokens = line.split("\t")
            uid = tokens[args.ididx]
            wav_path = tokens[args.wavidx]
            tmp = list()
            stm_sets[uid] = wav_path


def read_wav(file_path):
    # Read WAV file using soundfile
    try:
        data, samplerate = sf.read(file_path)
    except Exception as e:
        print(e)
        print(file_path)
        print(type(file_path))
        print(ASD)

    return data, samplerate

def write_wav(file_path, data, samplerate):
    # Write WAV file using soundfile
    sf.write(file_path, data, samplerate)

def write_transcript(file_path, transcript):
    with open(file_path, "w") as of:
        of.write(transcript+"\n")
        
def write_audio_list(file_path, audio_lst):
    with open(file_path, "w") as of:
        for e in audio_lst:
            of.write("{}\n".format(e))

def random_lang(past_lang):
    lang, utts_lst = random.choice(list(stm_sets.items()))       
    while lang == past_lang:
        lang, utts_lst = random.choice(list(stm_sets.items()))       
    return lang, utts_lst

def random_select(past_lang, used_ids):
    lang, utts_lst = random_lang(past_lang)
    i = random.choice(range(len(utts_lst)))
    uid, wav_path, text = utts_lst[i][0]
    while uid in used_ids[lang]:
        i = random.choice(range(len(utts_lst)))
        uid, wav_path, text = utts_lst[i][0]

    del utts_lst[i]
    return uid, wav_path, text, lang
    

def random_span_select(utts_lst, used_ids, lang):
    i = random.choice(range(len(utts_lst)))
    uid, wav_path, text = utts_lst[i][0]
    while uid in used_ids[lang]:
        i = random.choice(range(len(utts_lst)))
        uid, wav_path, text = utts_lst[i][0]

    del utts_lst[i]
    print("left utts: {}".format(len(utts_lst)))
    return uid, wav_path, text


def generate_set(stm_sets, used_ids, args):
    combined_transcript = ""
    list_of_audios = list()
    samplerate = 16000
    combined_duration = 0.0
    combined_data = np.array([], dtype=np.float32)
    past_lang, past_uid = None, None
    span = 0
    max_span = -1
    while combined_duration < 7200:
        if args.mix_style == "utt":
            uid, wav_path, text, lang = random_select(past_lang, used_ids)
        elif args.mix_style == "long":
            if span >= max_span:
                lang, utts_lst = random_lang(past_lang)
                max_span = random.randint(5, 10)
                span = 0
            else:
                lang = past_lang
                utts_lst = stm_sets[lang]

            uid, wav_path, text = random_span_select(utts_lst, used_ids, lang)
            span += 1
        data, samplerate = read_wav(wav_path)
        combined_data = np.concatenate([combined_data, data])
        combined_duration = len(combined_data) / samplerate
        list_of_audios.append(uid)
        combined_transcript = "{} <{}> {}".format(combined_transcript, lang, text)      
        past_lang = lang
        used_ids[lang][uid] = 1
        print("{}\{} current lang: {} uid: {}".format(combined_duration, 7200, lang, uid))

    write_wav(args.outa, combined_data, samplerate)
    write_transcript(args.outt, combined_transcript)
    write_audio_list(args.outl, list_of_audios) 

def concat_audio(stm_sets, args):
    samplerate = 16000
    combined_duration = 0.0
    combined_data = np.array([], dtype=np.float32)
    with open(args.uids, "r") as f:
        for line in f:
            line = line.strip()
            wav_path = stm_sets[line]
            data, samplerate = read_wav(wav_path)
            combined_data = np.concatenate([combined_data, data])
            combined_duration = len(combined_data) / samplerate
            print("{}\{} ".format(combined_duration, 7200))

    write_wav(args.outa, combined_data, samplerate)

concat_audio(stm_sets, args)
