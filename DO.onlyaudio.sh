export PATH="/home/eugan/miniconda3/envs/mms/bin:$PATH"

de_stm=
en_stm=
python only_audio_concat.py \
    -stms $de_stm $en_stm \
    -uids de.en/de.en.long.uids
    -outa test.wav
