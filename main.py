from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from colorama import Fore
from sys import argv


def main():
    youtube_link = ''

    try:
        youtube_link = argv[1]
    except:
        youtube_link = input("Insert youtube link: ")

    folder_path = "/"
    yt_title = YouTube(youtube_link).title

    def progress_func():
        print(Fore.YELLOW + f'\rDownloading {yt_title}...', end="")

    try:
        YouTube(
            youtube_link,
            on_progress_callback=progress_func(),
            use_oauth=False,
            allow_oauth_cache=True
        ).streams.get_highest_resolution().download(folder_path)

        print(Fore.GREEN + f'\nDownload Completed and saved in {folder_path}')
    except VideoUnavailable:
        print(
            f'\n{Fore.RED}Video {youtube_link} is either unavaialable or restricted.')


main()
