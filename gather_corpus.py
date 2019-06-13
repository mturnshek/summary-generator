import os


if __name__ == '__main__':
    ls = os.listdir('downloaded_summaries')
    all_text = ""
    for filename in ls:
        f = open("downloaded_summaries/" + filename)
        all_text += f.read()
        f.close()

    f = open("downloaded_summaries/all_text.txt", "w+")
    f.write(all_text)