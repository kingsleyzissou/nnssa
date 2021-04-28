import os
import pandas as pd

# Label song sections
INTRO = [
       'intro', 'intro2', 'inrto', 'intro', 'intro3', 'intro4', 'intro5', 'intro6', 
       'intro7', 'intro8', 'intropt2', 'opening' , 'rhythmlessintro', 'introverse'
]
CHORUS = [
       'altchorus', 'chorus', 'chorus1', 'chorus2', 'chorus3', 'chorushalf', 
       'chrous2', 'chrous', 'quietchorus', 'refrain', 'introchorus'
]
VERSE = [
       'verse', 'verse1', 'verse2', 'verse3', 'verse4', 'verse5', 'verse6', 
       'verse7', 'versepart', 'miniverse', 'slowverse',
       'verse10', 'verse11', 'verse1a', 'verse8', 'verse9',
       'verse_slow', 'verseinst', 'vese',
]
BRIDGE = ['bridge', 'bridge1', 'bridge2', 'bridge3']
SOLO = [
       'chorusinst', 'inst', 'inst2', 'instbridge', 'instchorus', 'instrumental', 'solo', 'guitar', 
       'breakdown', 'breakdown2', 'chorus_instrumental', 'choruspart', 'gtr', 'gtr2', 'gtrbreak',
       'guitarsolo', 'instintro', 'instrumental2', 'instrumental3', 'instrumentalverse', 'intchorus',
       'mainriff', 'mainriff2', 'solo2', 'solo3', 'synth', 'drumroll', 'raps', 'oddriff', 'banjo',
       'theme', 'main_theme'
]
TRANSITION = [
       'build', 'postchorus', 'postchorus2', 'prechors', 'prechorus', 'prechorus2', 'prechorus3'
       'prechrous', 'prehorus', 'preverse', 'tranisition', 'transition', 'transition2',
       'transtiion', 'stutter', 'postverse', 'transition1', 'transition2a', 'transition3',
       'prechorus3', 'prechorus5', 'prechrous', 'interlude', 'pre-verse', 'post-chorus', 'pre-chorus',
]
OUTRO = ['outro', 'outro1', 'outro2', 'outro3', 'bigoutro', 'outroa', 'vocaloutro', 'coda']
BREAK = ['break', 'bre', 'break1', 'break2', 'break3']
LIVE = ['applause', 'crowd_sounds', 'spoken_voice', 'stage_sounds', 'stage_speaking', 'voice']

def clean_sections(section):
    section = section.lower()
    if section in INTRO: return 'intro'
    if section in TRANSITION: return 'transition'
    if section in CHORUS: return 'chorus'
    if section in BRIDGE: return 'bridge'
    if section in VERSE: return 'verse'
    if section in SOLO: return 'solo/instrumental'
    if section in OUTRO: return 'outro'
    if section in BREAK: return 'break'
    if section in LIVE: return 'live'
    return 'other'

def load_annotations(row, clean=True, salami=False):
    rawpath = row.First_annotation if row.First_exists else row.Second_annotation
    filepath = os.path.join(rawpath)
    separator = ' ' if not salami else None
    annotations = pd.read_table(filepath, header=None, sep=separator, names=['Time', 'Section'])
    if clean:
        annotations['Section'] = annotations['Section'].map(clean_sections)
        annotations = annotations[annotations['Section'] != 'other']
    return annotations['Time'].values, annotations['Section'].values