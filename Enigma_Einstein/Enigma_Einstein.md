# IAs generativas e o puzzle “Teste de Einstein”

Estava fazendo um curso sobre Engenharia de Prompt com o instrutor Fabrício Carraro, onde ele estava explicando sobre a importância de um bom prompt.

Na ocasião o instrutor utilizava o Mistral (chat francês) e tinha feito um prompt simples para uso de uma pergunta que envolvia raciocínio lógico e objetivo era mostrar como podemos obter uma resposta errada devido a forma como o prompt foi elaborado. Após alguns ajustes o chat forneceu uma resposta correta.

Foi aí que eu pensei em usar um chat de IA generativa para um teste de lógica um pouco mais complexo do que foi apresentado na aula e lembrei do Teste de Einstein, também conhecido por outros nomes como Enigma de Einstein, por exemplo, que é um puzzle de raciocínio lógico.

Diz a lenda que esse teste foi elaborado pelo próprio Albert Einstein e somente 2% da população consegue resolvê-lo.  Embora não exista nenhuma prova sobre a autoria do puzzle e nenhuma estudo acadêmico conhecido sobre o percentual da população mundial capaz de resolver o puzzle, o mesmo, é bem interessante e pode “queimar” alguns neurônios de que tentar resolvê-lo.

Para quem tiver curiosidade, o puzzle pode ser encontrado em sites como Racha Cuca.

Inicialmente utilizei o Mistral e Gemini para ver como se saiam como o teste.
O prompt inicial foi o seguinte:

```prompt
Vamos jogar um jogo chamado "Jogo de Einstein" onde você deve usar as dicas para resolver o enigma.
 
 
As características possíveis do jogo são:
 
 
1. Nacionalidade
  a. Britânico
  b. Dinamarquês
  c. Sueco
  d. Norueguês
  e. Alemão
 
2. Cor
  a. Vermelha
  b. Verde
  c. Azul
  d. Amarela
  e. Branca
 
3. Bebida
  a. Chá
  b. Café
  c. Leite
  d. Cerveja
  e. Água
 
4. Cigarro 
  a. Prince
  b. Pall Mall
  c. Dunhill
  d. Blends
  e. Bluemaster
 
5. Pet 
  a. Cachoro
  b. Pássaro
  c. Gato
  d. Cavalo
  e. Peixe
 
 
Sabendo das seguintes informações:
 
1. O britânico vive na casa vermelha.
2. O sueco tem um cachorro.
3. O dinamarquês toma chá.
4. O norueguês mora na primeira casa.
5. O alemão fuma Prince.
6. A casa verde fica ao lado da branca, à esquerda.
7. O morador da casa verde toma café.
8. Quem fuma Pall Mall tem pássaros.
9. O morador da casa amarela fuma Dunhill.
10. O morador da casa central toma leite.
11. Quem fuma Blends mora ao lado de quem tem um gato.
12. Quem tem um cavalo mora ao lado de quem fuma Dunhill.
13. Quem fuma Bluemaster toma cerveja.
14. Quem fuma Blends mora ao lado de quem toma água.
15. O norueguês mora ao lado da casa azul.
 
 
Responda:
 
1. "Quem é o dono do peixe?"
2. "Quais as outras características do dono do peixe"
 
Detalhe a lógica utilizada para chegar a conclusão da sua resposta
```

Olhando agora, ficou claro que o prompt pode ser melhorado, mas, mesmo com esse prompt a resposta esperada seria algo como:

```response
O dono do peixe é alemão, mora na casa 4 que é verde, bebe café e fuma Prince.
```

E a solução completa do puzzle é a seguinte:


| Casa        | 1 🟨       | 2 🟦       | 3 🟥       | 4 🟩       | 5 ⬜       |
|-------------|------------|------------|------------|------------|------------|
| Nacionalidade | Norueguês  | Dinamarquês| Inglês     | Alemão     | Sueco      |
| Cor         | Amarela    | Azul       | Vermelha   | Verde      | Branca     |
| Bebida      | Água       | Chá        | Leite      | Café       | Cerveja    |
| Cigarro     | Dunhill    | Blends     | Pall Mall  | Prince     | Blue Master|
| Animal      | Gato       | Cavalo     | Passaro    | Peixe      | Cachorro   |

<br>

## Gemini X Mistral

Como durante o curso eu estava o Gemini e o Mistral, foi por essas duas ferramentas que eu comecei.

Embora não tenha solicitado no prompt inicial, as duas ferramentas apresentaram uma tabela completa com os resultados e uma resposta textual sobre quem era o do peixe.

<br>

### Gemini

No Gemini foi utilizado o modelo modelo 2.5-flash. Na primeira tentativa o Gemini apresentou a seguinte resposta:

```response
Quem é o dono do peixe? O dono do peixe é o Alemão.

Quais as outras características do dono do peixe? O dono do peixe (o Alemão) mora na:
•   Casa: 5
•   Cor: Branca
•   Bebida: Cerveja
•   Cigarro: Prince
```

Embora tenha acertado que o dono do peixe seja alemão, essa resposta violam as regras 5 e 13 do puzzle (vide prompt inicial acima).

Após informar ao chat do Gemini, a violação das regras 5 e 13, obtive a seguinte resposta:

```response
Não há solução para a sua lista de dicas que satisfaça todas as 15 regras simultaneamente, devido ao conflito que você identificou. No entanto, a solução mais próxima (que satisfaz 13 das 15 regras e é aceita em versões com leves ajustes) é que o Dinamarquês é o dono do peixe.

Vou responder com a solução mais logicamente defensável (a última tabela):
...
```

Aqui já fica claro que o prompt inicial pode ser melhorado para informar explicitamente que a solução deve satisfazer as 15 regras iniciais.

Outro ponto é que o dono do peixe é a última das características a ser definida ao seguir uma lógica para resolver o puzzle, mas, dá forma como foi escrito o prompt, ficou implícito que o chat deve resolver todo o puzzle. Ao invés de perguntar somente pelo dono do peixe, talvez, seria melhor solicitar uma solução completa do puzzle.

Informei ao chat que a resposta acima violava a regra 15 e dei uma dica sobre algumas abordagens a serem seguidas com o seguinte prompt:

```prompt
Essa reposta está incorreta.
E sim existe uma solução que satisfaça as 15 regras que forneci.
Antes de cada etapa de análise, identifique regras implícitas que existem utilizando as 15 regras iniciais.
 
Por exemplo:
* Pelas regras "2. O sueco tem um cachorro." e "8. Quem fuma Pall Mall tem pássaros.", você pode adicionar mais uma regra:
16. O sueco não fuma Pall Mall
 
* Pelas regras "3. O dinamarquês toma chá.", "5. O alemão fuma Prince." e "13. Quem fuma Bluemaster toma cerveja.", você pode adicionar a seguinte regra:
17. O dinamarquês não fuma Price nem fuma Bluemaster.
 
Existem outras regras implícitas já inicio da análise e vão surgir outras a cada definição encontrada.
 
Refaça análise, por favor
```

A resposta obtida foi:

```response
Esta é a única tabela que satisfaz todas as regras de vizinhança e atribuição, forçando a seguinte conclusão:
1.	Quem é o dono do peixe? O dono do peixe é o Alemão.
2.	Quais as outras características do dono do peixe?
o   Casa: 5
o   Cor: Branca
o   Bebida: Cerveja
o   Cigarro: Bluemaster
```


Informei ao chat que a reposta fornecida violava a regra 5 e o chat continuava a insistir que a lista de dicas (regras) estava incorreta. E mesmo fornecendo outras dicas, as respostas continuava apontando que as regras iniciais estavam incorretas. Segue um dos retornos do chat.

```response
Sua lista de dicas, tal como apresentada, contém uma contradição lógica insuperável se todas as duplas obrigatórias (D3, D5, D13) e as vizinhanças (D11, D14) forem estritamente seguidas...
```

Somente quando forneci um prompt com as 15 regras iniciais, todas as regras implícitas que surgiam a medida que o puzzle ia sendo resolvido foi que o chat forneceu a resposta correta.

Para acessar chat completo do Gemini, [clique aqui](./Gemini_2.5-flash.md)

<br>

### Mistral

O Mistral não informal qual modelo está sendo utilizado. Na primeira resposta o chat não conseguiu identificar qual é o cigarro da casa 5. Além disso, a solução parcial apresentada violava as regras 5 e 13.

Ao informar essas violações ao chat, foi retornado uma resposta completa, mas, que dessa vez violava as regras 13, 11 e 14, e a resposta seguinte violava a regra 13.

Mesmo informando ao chat que existia regras implícitas que poderiam ser deduzidas a partir das regras iniciais (mesma dica fornecida ao Gemini) a resposta seguinte ainda violava a regra 13.

Forneci textualmente as regras implícitas que surgiam ao longo da análise e ainda assim o chat fornecia resposta que violava a regra 13.

Por fim, forneci ao chat do Mistral o mesmo prompt que tinha fornecido ao Gemini para conseguir resolver o puzzle e ainda assim o chat do Mistral fornecia uma reposta dada como certa, mas, que violava a regra 13.

Como o Mistral não tinha conseguido a reposta correta mesmo utilizando o mesmo prompt que permitiu ao Gemini chegar a resposta correta, resolvi encerrar os testes com o Mistral

Chama atenção a abordagem diferente em que as duas ferramentas lhe davam com as falhas. Enquanto o Gemini informava que existiam falhas lógicas nas 15 regras iniciais o Mistral, simplesmente continuava a dar respostas erradas inclusive violando a mesma regra como se fosse corretas.

Mas, nenhuma da duas admitiam que "eles" não sabiam a reposta correta.

<br>

## E as outras ferramentas de IAs generativas?

Como tive dificuldade para obter a resposta correta com os dois chats citados, resolvi testar com outras ferramentas até para entender o quanto a qualidade do prompt pode ter dificultado o trabalho do Gemini e do Mistral e para minha surpresa, outras ferramentas com o mesmo propósito tiveram melhor desempenho, inclusive acertado de primeira.

<br>

### Acertando de primeira

* ChatGPT (sem informação do modelo utilizado)

* Claude.ia (modelo Sonnet 4.5)

* Qwen (modelo Qwen3-Max)

* Grok (modelo Automatic, Fast or Expert)

* Google AI Studio (modelo gemini-flash-latest)

As cinco ferramentas acima, não só forneceram a reposta correta com o prompt inicial (ou seja, na primeira tentativa), como também apresentaram uma tabela completa da solução.

<br>

* Maritaca.ia (modelo Sabiá-3.1)

* Copilot (modelo Think Deeper)

* DeepSeek (sem informação do modelo utilizado)

Já essas três ferramentas, forneceram a reposta correta com prompt inicial, mas, não apresentaram uma tabela completa da solução, o que não foi solicitado no prompt.

<br>

### Quase de primeira

* Z.ai (modelo GLM-4.6)

Errou na primeira tentativa, violando a regra 11, mas, acertou na segunda tentativa quando informei ao mesmo sobre a violação e também apresentou uma tabela completa da solução.

<br>

### Quem não se saiu muito bem?

* Meta.ai (sem informação do modelo utilizado)

A grande decepção foi a Meta.ai, após duas tentativas, o chat nem chegou a concluir a análise e simplesmente travou e parou de escrever no chat.

* Perplexity (sem informação do modelo utilizado)

Já o Perplexity não conseguiu fazer uma análise completa e nas duas solicitações que fiz as respostas parciais já apresentavam erros. Após as duas falhas, encerei os testes.

Aqui vale mencionar brevemente que o Perplexity trabalha um pouco diferente dos demais chats utilizados, ele utiliza da IA fazer pesquisa na internet e a partir daí dar as respostas de acordo com as fontes informadas.

<br>

## Surpresas positiva

<br>

### NotebookLM

A grande surpresa positiva foi o NotebookLM. Embora seja uma IA generativa, o objetivo dela é diferente das demais ferramentas testadas.

Resumidamente podemos dizer que objetivo do NotebookLM é gerar conteúdo resumido de fontes de dados fornecidas diretamente pelo usuário. Ou seja, conceitualmente a ferramenta “não gera” conteúdo novo, apenas sumariza com base nas fontes fornecidas. Mesmo assim, por curiosidade, resolvi testar a ferramenta.

Para usar o NotebookLM eu precisei criar um arquivo .TXT com as informações necessárias para resolver o puzzle, igual ao prompt inicial usado em todos os outros testes, exceto pela pergunta final. E carreguei o arquivo como uma fonte de dados
Após o NotebookLM me fornecer um resumo inicial (que é padrão da ferramenta) fiz a pergunta:

```prompt
1. "Quem é o dono do peixe?"
2. "Quais as outras características do dono do peixe"
Detalhe a lógica utilizada para chegar a conclusão da sua resposta
```

Na primeira tentativa, a resposta estava incorreta e violava as regras 5 e 8. Após informar ao chat essas violações, já na segunda tentativa, obtive a reposta correta e com uma tabela completa com a solução.

<br>

### SciSpace

Quem também surpreendeu foi o SciSpace. Ferramenta de IA focada em pesquisa científica, o chat criou um agente de IA, gerou um código em linguagem de programação Python para tentar solucionar o problema e executou o próprio código gerado.

Quando a execução do código Python falhou o próprio chat gerou outro código otimizado em Python e executou novamente.

Essa nova execução não sou gerou a reposta correta como a tabela completa da solução e ainda fez uma análise de complexidade.

```response
🔬 ANÁLISE DA COMPLEXIDADE
Espaço de Busca
• Permutações possíveis: 5! × 5! × 5! × 5! × 5! = 24.883.200.000 combinações
• Solução única: Apenas 1 combinação satisfaz todas as restrições
• Probabilidade aleatória: 1 em 24 bilhões
Estratégia de Resolução
1. Dedução Lógica Sequencial: Aplicar restrições em ordem estratégica
2. Propagação de Restrições: Cada dedução limita as possibilidades seguintes
3. Eliminação por Contradição: Descartar configurações impossíveis
4. Verificação Completa: Confirmar que todas as 15 regras são satisfeitas

📚 Curiosidades
• Este enigma é atribuído a Albert Einstein, que supostamente o criou quando criança
• Diz-se que Einstein afirmou que apenas 2% da população mundial consegue resolver este enigma
• É um exemplo clássico de Problema de Satisfação de Restrições (CSP) usado em Inteligência Artificial
• A solução requer raciocínio lógico puro, sem necessidade de conhecimento especializado
________________________________________
Documento gerado por SciSpace Research Agent
Data: 2025-11-05
```

Para acessar chat completo do SciSpace, [clique aqui](./SciSpace.md)

<br>

## E os Humanos?

Bom, eu não sei dizer sobre os outros 8 bilhões de habitantes do nosso planeta ou dos 2% que supostamente são capazes de resolver esse puzzle.

Mas, esse que vos escreve, já tinha solucionado o puzzle no passado. Embora não lembrasse da solução quando fiz os testes com os chats já tinha uma noção de como resolver.

Na primeira tentativa eu errei ao seguir uma lógica muito usada para resolver Sudoku, mas, que não cabe aqui. Com isso, acabei colocando o sueco na casa 4, quando deveria ser na casa 5 e no final não consegui satisfazer a regra 3 que diz que “O dinamarquês toma chá”.

Já na segunda tentativa, comecei a identificar as regras implícitas existente ao cruzar as regras iniciais e as regras implícitas que iam surgindo a medida que o puzzle ia sendo resolvido e consegui chegar à resposta correta.

<br>

## Dá pra confiar cegamente nas IAs?

Já nas primeiras versões de chats generativos baseados em LLM, especialistas em IA nos alertavam sobre os erros nas repostas geradas por essas ferramentas, e principalmente respostas que envolvem raciocínio lógico. E mesmo os LRMs (evolução do LLM para raciocínio lógico) parece ter suas limitações.

Embora esse puzzle não seja algo de grande complexidade os resultados falhos de algumas ferramentas confirmam o alerta dos especialitas sobre a dificuldade de IAs generativas gerarem texto que dependem de lógica formal e rigorosa.

Chama a atenção e preocupa a forma elegante com que as IAs generativas erram. As etapas intermediárias parecem mostrar um rigor lógico/ matemático impressionante  mesmo cometendo erros simples.

Esse cenário me lembra o caso do canadense Allan Brooks. Ele acreditava que tinha descoberto uma nova teoria matemática revolucionária com o ChatGPT. Como ninguém deu muita bola, ele ficou paranoico e começou a se afastar de todo mundo, até que ele teve a ideia de testar a teoria em outra ferramenta de IA que logo de cara apresentou os erros da nova "teoria matemática". Ele inclusive fundou uma ONG, The Human Line Project, para lhe dar com questões de saúde mental relacionada com uso de IAs.

<br>

## Conclusões

Os diferentes resultados obtidos mostram os avanços que cada empresa vêm implementando para entregarem resultados mais assertivos. Em um ambiente controlado, relativamente simples e que já se sabe as repostas corretas é fácil identificar erros, respostas incompletas ou que parecem ser verdadeiras, mas, sem nenhum fundamento científico. Mas, a realidade do dia a dia das IAs generativas é bem mais desafiante que o Enigma de Einstein.

É inegável os benefícios advindos do uso das mais diversas ferramentas de IA que vêm surgindo e que continuarão a aparecer, mas, na mesma proporção surgem os mais diversos desafios inerentes a própria tecnologia e devemos estar preparados para os aspectos positivos e negativos das IAs.

Esse teste não é nenhum estudo acadêmico (e não foi esse o objetivo), é uma simples curiosidade. Como também poderia ser utilizado técnicas mais avançadas de engenharia de prompt. Mas, se você testar várias vezes e em ferramentas diferentes, dá pra confiar que as IAs generativas conseguem resolver o Enigma de Einstein.


<br>


### Ferramentas utilizadas:

* https://gemini.google.com/
* https://chat.mistral.ai/
* https://chatgpt.com
* https://claude.ai/
* https://chat.qwen.ai/
* https://grok.com/
* https://chat.maritaca.ai/
* https://copilot.microsoft.com/chats
* https://chat.deepseek.com/
* https://chat.z.ai/
* https://www.meta.ai/
* https://www.perplexity.ai/
* https://scispace.com/
* https://aistudio.google.com/app/prompts/new_chat
* https://notebooklm.google.com/


### Para fazer o Teste de Einstein:

* https://rachacuca.com.br/logica/problemas/teste-de-einstein/

### Para saber mais:

* https://www.bbc.com/portuguese/articles/c72gdnynvdvo
* https://super.abril.com.br/ideias/charada-atribuida-a-einsten-da-no-no-cerebro-e-vira-hit-na-web/
* https://blog.dsacademy.com.br/o-que-sao-large-language-models-llms/
* https://blog.dsacademy.com.br/llms-e-a-evolucao-da-ia-generativa/
* https://macmagazine.com.br/post/2025/06/09/estudo-da-apple-explora-limitacoes-dos-grandes-modelos-de-raciocinio-de-ia/
* https://www.infomoney.com.br/mundo/chats-de-ia-podem-entrar-em-uma-espiral-de-delirio-e-isso-esta-afetando-as-pessoas/
* https://thehumanlineproject.org/


---
Para retornar ao README principal, [clique aqui](../README.md)