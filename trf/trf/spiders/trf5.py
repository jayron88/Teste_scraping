import scrapy
import re
from datetime import datetime

class Trf5Spider(scrapy.Spider):
    name = 'trf5'
    '''
        Bom, no start_urls eu coloquei todos os numeros de processos que foi pedido
        no github
    '''
    start_urls = [
        'https://cp.trf5.jus.br/processo/0015648-78.1999.4.05.0000/',
        'https://cp.trf5.jus.br/processo/0012656-90.2012.4.05.0000/',
        'https://cp.trf5.jus.br/processo/0043753-74.2013.4.05.0000/',
        'https://cp.trf5.jus.br/processo/0002098-07.2011.4.05.8500/',
        'https://cp.trf5.jus.br/processo/0460674-33.2019.4.05.0000/',
        'https://cp.trf5.jus.br/processo/0000560-67.2017.4.05.0000'
    ]

    def parse(self, response):

        # Nesta parte utilizei um regex para puxar apenas o número do processo
        numero_processo = response.css('p:nth-child(4)::text').re('\d+-\d+.*')
        numero_legado = response.css("p+ p::text").get(default=None)

        # Uma condição para caso não tenha o número do processo, ser substituida
        if len(numero_processo) == 0:
            numero_processo = numero_legado

        data_atuacao = datetime.strptime(response.css('div').re('\d{2}/\d{2}/\d{4}')[0], '%d/%m/%Y')


        ''' 
        O envolvidos puxa a table inteira, o relator por padrão sempre esta na ultima
        então resolvi apenas pegar a ultima posição da lista "envolvidos", no caso o 
        relator
        '''
        envolvidos = response.xpath('//html/body/table[3]//tr//td//text()').getall()
        relator = str(envolvidos[-1])

        # aqui uma lista de envolvidos, indo de 0::3 pois dessa forma alcança apenas o papel
        lista_envolvidos = envolvidos[0::3]

        yield {
            'numero_processo': numero_processo,
            'numero_legado': numero_legado,
            'data_atuacao': data_atuacao,
            'relator': relator.replace(':', '')
        }

        contador = 0
        for nomes in response.xpath('/html/body/table[3]//tr//b//text()').getall():
            yield {
                'papel': lista_envolvidos[contador],
                'nome': nomes.replace(':', '')
                     }
            contador +=1

        cont = 0
        while True:
            if variavel := response.xpath(f"/html/body/table[{6 + cont}]//tr//td//text()").getall():
                nova_lista = [item for item in variavel if re.sub(r'[\s]', '', item)]
                data = datetime.strptime(re.search('\d{2}\/\d{2}\/\d{4}\s\d{2}:\d{2}', nova_lista[0])[0], '%d/%m/%Y %H:%M')
                texto = ''.join(nova_lista[1:])
                yield {
                    'data': data,
                    'texto': texto
                }
            else:
                break
            cont += 1

