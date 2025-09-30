import pydub, pydub.playback, pydub.utils

def main() -> None:
    with open("A.mp3", "r") as wav:
        a: pydub.AudioSegment = pydub.AudioSegment.from_file(wav)
    with open("B.mp3", "r") as wav:
        b: pydub.AudioSegment = pydub.AudioSegment.from_file(wav)
    with open("E.mp3", "r") as wav:
        e: pydub.AudioSegment = pydub.AudioSegment.from_file(wav)
    aud = pydub.AudioSegment()
    aud.append(a)
    aud.append(b)
    aud.append(e)
    pydub.playback.play(aud)

if __name__ == "__main__":
    main()