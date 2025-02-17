import hymns

if __name__ == '__main__':
    for lang in ('eng', 'spa'):
        for size in ('a4', 'letter'):
            hymns.build_pdf(lang, size)
