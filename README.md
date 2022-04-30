# Webcardapio
<!--Introdução-->
#### Um webcardapio desenvolvido com HTML / CSS no frontend e Python Flask no backend.
#
<!--Desenvolvimento-->
### Sistema

A ideia era fazer um sistema que conseguisse gerar as requisições de pedido e enviar para a cozinha.
Esse webcardapio seria ligado a outro sistema, uma administração, por onde seria editado o cardapio, com atualizações de novos pratos e alterações de preço por exemplo.

### Design
O design esperado foi desenvolvido com ajuda da ferramenta Figma contendo uma tela de apertura, a tela do menu, uma tela para finalizar pedidos e uma tela de agradecimento.
#
<div align="center">
<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Ffile%2FwdBCT5H5GLZeL3sxefzY4B%2Fwebcardapio_model%3Fnode-id%3D105%253A969" allowfullscreen></iframe>
</div>

#

### FrontEnd
Como ja dito o frontend seria feito com HTML / CSS para funcionar em telas de até 400px no caso de celulares para telas maiores será feita uma adaptção do design desenvolvido.
<!--adicionar opção para tables-->


### BackEnd
No backend foi usado micro-framework Python flask para fazer o controles das rotas e do banco de dados, esse micro-framework foi escolhido pela sua simplicidadem e facilidade de uso.

### BD
O banco de dados foi feito com ferramentas do proprio Flask, onde terá uma tabela para armazenar os pratos disponiveis e as requisições para a cozinha.

<!--Diagrama DER-->
