from url_utils import gen_from_urls

urls = ('https://gizmodo.com.br', 'https://adrenaline.com.br', 'https://otakupt.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)
    
url_res = {url: size for size, _, url in gen_from_urls(urls)}
#Cria um dicionario atraves de um dictcomp, utilizando o generator no modulo importado
#_ ignora status. chave: url, valor: size

import pprint

pprint.pprint(url_res)