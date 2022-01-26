# Teste_scraping

Bom, primeiramente para rodar você deve acessar o path /trf/trf/spiders/ e utilizar o comando:

*scrapy runspider trf5.py -o scrap.json*

O comando acima irá gerar um .json, que foi o modo que escolhi para persistir os dados.
Com o scrap.json, você deve rodar o *json_to_csv.py* para converter o scrap.json para um csv.
Escolhe o CSV pois ficou de maneira mais clara e limpa de se enxergar os dados do scrapy.

# Dentro do código também coloquei alguns comentários relacionados ao código *trf5.py* e *json_to_csv.py*


*Requisitos:*

pandas - last version

scrapy - last version

re - last version

# FORMA DE VISUALIZAÇÃO 

Bom, escolhi .json, convertido para csv através do Pandas para visualizar os dados extraídos.

acredito que seja isso, muito obrigado de toda forma pela oportunidade.
