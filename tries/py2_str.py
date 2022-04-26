










if __name__ == "__main__":

    date = "May 11 2022"
    track = "GPGPU"
    room = "O-RGY"
    title = "Effects of Hard P"
    abstract = "We go ahead and tried some techniques over the problem. Found out some of them prove better than others. Therefore this is a research article. Have fun"
    keywords = "Hard P, GPGPU, Keys"


    tex = r"""
    \begin{{abstract_basarim}}
    {{{}}}
    {{%{}}}
    \end{{abstract_basarim}}
    """.format(date, track, room, title, abstract, keywords)

    print(tex)
