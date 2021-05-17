from html import HTML
from hash import Hash

m = {'Вода': 457,
     'Сок': 876,
     'Кола': 826,
     'Апероль': 235,
     'Смузи': 174}

table = Hash()
for k, v in m.items():
    table.__setitem__(k, v)
print(table.__getitem__('Сок'))
for k, v in m.items():
     print(k+"   "+str(table.__getitem__(k)))

html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
            with html.div():
                html.p('Xtndthnf строка.')
        with html.div():
            html.p('Третья строка.')