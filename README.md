##Tartaruga cliente-servidor

Exemplo de comunicação cliente-servidor utilizando protocolo UDP e mensagens codificadas em JSON.
Um exemplo de aplicação utilizando o pacote turtle do Python.

Descrição do formato das mensagens entre Cliente e Servidor:
As mensagens trocadas em forma de String tem a seguinte forma: 

(<Comando : String>, <arg1,arg2,arg3 : int>) : String

Tal que o cliente envia um comando (denotando a instrução a ser executada) seguido de uma vírgula com uma sequência de inteiros separados por vírgulas, estes inteiros servirão de argumentos para as funções a serem executadas. Na maioria das vezes tais valores é automaticamente "plugado" na chamada da função na aplicação servidor, entretanto outros casos exigem um pouco de pré-processamento de tais inteiros. Por exemplo, a fim de alterar a cor o cliente entra com os seguintes argumentos: 255,0,0,0,255,0. O programa servidor por sua vez separa tal string em um array de inteiros de 6 posições (usual para todas as funções) e cria 2 triplas, convertendo-as de notação RGB para HEX (consulte a linha 38 da aplicação servidor para mais detalhes).

O uso do programa é simples, escolha a operação de acordo com o menu, após isso insira os argumentos para a função, lembre-se que todos os argumentos são inteiros e devem ser separados por vírgula, mesmo que a função não tenha argumentos um valor deve ser passado.
