from pydub import AudioSegment

def pad_audio(youtube, actual, input_file, output_file):
    """
    This function is used to line up the audio of the songs
    downloaded from YouTube with the metadata we have for 
    the respective songs from the annotators.
    
    :param youtube - the youtube download metadata
    :param actual - the annotated song metadata
    :param input_file - the file name of the input song to be read from
    :param ouput_file - the file name for the song to be written to
    """
    start = youtube["onset"] - actual["onset"]
    end = start - actual["length"]
    out = input_file
    if (end > youtube["length"]):
        duration = (end - youtube["length"])*1000
        pad = AudioSegment.silent(duration=duration)
        out = out + pad
    if(start < 0):
        duration = start*-1000
        pad = AudioSegment.silent(duration=duration)
        out = pad + out
        start = 0
    trim = (start + actual["length"]) * 1000
    out = out[start:trim]
    out.export(output_file, format="mp3")