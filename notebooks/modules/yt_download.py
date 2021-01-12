import youtube_dl

def download_video(filename, outputdir, url, format):
    """
    This function is used to download items
    from YouTube. The function can be made
    more generic and can also download playlists.
    This function will be used in WIT's TutorStack
    for media management purposes
    :param filename - output filename
    :param outputdir - output directory
    :param url - youtube url
    """
    ydl_opts = {
        'ignoreerrors': True, ## carry on downloading if errors are encountered
        'format': format, ## set the format preference
        'outtmpl': outputdir + filename + '.%(ext)s' ## set the file name
    }
    print(ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])