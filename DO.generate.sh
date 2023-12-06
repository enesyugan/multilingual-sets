export PATH="/home/eugan/miniconda3/envs/mms/bin:$PATH"

de_stm=
en_stm=
out=de.en
mkdir -p $out
python make_multidata_set.py \
    -stms $de_stm $en_stm \
    -langs de en \
    -outa $out/de.en.wav -outt $out/de.en.stm -outl $out/de.en.uids 
    #&

# Store the process ID (PID) of the first script
pid_script1=$!
echo "PID for script1: $pid_script1"

python make_multidata_set.py \
    -stms $de_stm $en_stm \
    -langs de en \
    -mix_style long \
    -outa $out/de.en.long.wav -outt $out/de.en.long.stm -outl $out/de.en.long.uids # &

# Store the PID of the second script
pid_script2=$!
echo "PID for script2: $pid_script2"


# Wait for both scripts to finish
#wait $pid_script1
#wait $pid_script2

echo "Both Python scripts have completed."
