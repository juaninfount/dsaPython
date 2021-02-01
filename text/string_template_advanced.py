import string

class MyTemplate(string.Template):
    delimiter = '%'  # nombre de atributo invariable
    idpattern = '[a-z]+_[a-z]+' # nombre de atributo invariable

template_text = '''
    Delimiter: %%
    Replaced : %with_underscore
    Ignored  : %not_underscored
'''

d = {
    'with_underscore':'replaced',
    'not_underscored': 'not replaced'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))