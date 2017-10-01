import json


def clear_avito_json(json_file):
    with open('./data/avito.json', 'rb') as f:
        avito_json = json.load(f)
    avito_json_clear = []
    avito_unic_urls = []
    for t_p in avito_json:
        if t_p['title'] is not None:
            t_p_title = t_p['title'].strip()
            t_p_price = t_p['price'].strip()
            t_p_url = t_p['url'].strip()
            t_p_clear = {
                'title': t_p_title,
                'price': t_p_price,
                'url': t_p_url,
            }
            if t_p_url not in avito_unic_urls:
                avito_unic_urls.append(t_p_url)
                avito_json_clear.append(t_p_clear)

    for item in avito_json_clear:
        print(item)
    print('\nCount items: {}'.format(len(avito_json_clear)))
    with open('./data/{}_clear.json'.format(json_file), 'w', encoding='utf-8') as f:
        json.dump(avito_json_clear, f, ensure_ascii=False)


if __name__ == '__main__':
    print('Testing charset')
    clear_avito_json('avito_buisness')
    print()
