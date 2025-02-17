import hymns
import itertools

if __name__ == '__main__':
    lang_choices = size_choices = []

    parser = hymns.arg_parser()
    for action in parser._actions:
        if action.dest == 'lang':
            lang_choices = action.choices
        elif action.dest == 'size':
            size_choices = action.choices

    for (lang, size) in itertools.product(lang_choices, size_choices):
        print(f'Generating document for lang:{lang} and size:{size}')
        hymns.build_pdf(lang, size)
