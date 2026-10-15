fur=input('У собаки короткая шерсть?')
if fur=='да':
    high1=input('Рост собаки менее 50 см?')
    if high1=='да':
        tale=input('У собаки короткий хвост?')
        if tale=='да':
            print('английский бульдог')
        else:
            ears=input('У собаки длинные уши?')
            if ears=='да':
                print('гончая')
            else:
                body=input('У собаки короткое тело?')
                if body=='да':
                    print('мопс')
                else:
                    print('чихуахуа')
    else:
        wast=input('Собака весит более 50 кг?')
        if wast=='да':
            print('датский дог')
        else:
            print('фоксхаунд')
elif fur=='нет':
    high1 = input('Рост собаки менее 50 см?')
    if high1 == 'да':
        emo=input('У собаки доброжелательный характер?')
        if emo=='да':
            print('кокер-спаниэль')
        else:
            print('ирландский сеттер')
    else:
        high2=input('у собаки рост менее 70см?')
        if high2=='да':
            ears = input('У собаки длинные уши?')
            if ears == 'да':
                print('большой вандейский грифон')
            else:
                print('колли')
        else:
            rij=input('окрас рыжий с белыми отметинами?')
            if rij=='да':
                print('сенбернар')
            else:
                beli=input('Белоснежный окрас?')
                if beli=='да':
                    print('ирландский волкодав')
                else:
                    print('ньюфаундленд')




