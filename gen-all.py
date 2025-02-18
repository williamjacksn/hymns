import hymns
import itertools

if __name__ == '__main__':
    for (lang, size) in itertools.product(hymns.lang_choices, hymns.size_choices):
        print(f'Generating document for lang:{lang} and size:{size}')
        hymns.build_pdf(lang, size)
