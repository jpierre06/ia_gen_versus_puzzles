# Solução do Enigma de Einsten

Segue minha solução para o Enigma de Einsten seguindo apenas racíocinio lógico

<br>

## As caracterísitcas dos moredores de cada e as regras gerais são:

As características possíveis do jogo são:

1. Nacionalidade

    a.Britânico

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

<br>

## Regras iniciais obrigatórias

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

<br>

## Das regras gerais temos as seguintes regras implícitas:

16. O sueco não fuma Pall Mall (derivado das regras 2 e 8).
17. O dinamrquês não fuma Price e nem fuma Bluemaster (derivado das regras 3, 5 e 13).
18. O morador da casa amarela não bebe cerveja (derivado das regras 9 e 13).
19. O morador da casa amarela não é sueco (derivado das regras 2 e 9).
20. O morador da casa amarela não têm pássaros (derivado das regras 8 e 9).
21. Quem fuma Bluemaster toma cerveja não é dinamarquês e nem alemão (derivado das regras 3, 5 e 13).
22. A Casa 3 não pode ser verde (derivado das regras 7 e 10).
23. O dinamrquês não mora nas casas 1 ou 3 (derivado das regras 3, 4 e 10).

<br>

## Solução passa a passo

Para manter uma lógica fácil de entendimento em cada etapa é analisada as regras gerais e as consequentes deduções em ordem em que aparecem as 15 regras inicias.

Ao fim das análises de cada etapa o processo é reiniciado.

<br>

### 1. Etapa

* Passo 1, regra 4. O norueguês mora na primeira casa.
* Passo 2, regra 10. O morador da casa central toma leite.
* Passo 3, regra 15. O norueguês mora ao lado da casa azul.

<br>

### 2. Etapa

* Passo 4, das regras 6, 7 e 22, temos:
    * A combinação verde-branca não pode ser casas 1-2 ou 2-3, porque a casa 2 é azul;
    * A combinação verde-branca não pode ser casas 3-4, porque o morador da casa 3 bebe leite;
    * Casa 4 é verde e bebe café, Casa 5 é branca;

<br>

### Regras implícitas

24. Quem fuma Bluemaster e toma cerveja não mora nas casa 3 e 4.
* Porque na casa 3 bebe leite e na casa 4 bebe café

<br>

### 3. Etapa

* Passo 5, da regra 1, temos:
    * O norueguês mora na casa 1 e a casa 2 é azul, casa 4 é verde e casa 5 é branca;
    * O inglês mora casa 3 que é vermelha
    * Consequentemente a casa 1 é amarela `(todas as cores resolvidas)`
* Passo 6, regra 9. O morador da casa amarela fuma Dunhill.
* Passo 7, regra 12. Quem tem um cavalo mora ao lado de quem fuma Dunhill, na casa 2

<br>

### Regras implícitas

25. O sueco não fuma Pall Mall nem Dunhill, não mora na casa 2, bebe cerveja e fuma Bluemaster
* Porque o dinamarquês bebe chá, o inglês bebe cerveja
* O norueguês fuma Dunhill e o alemão fuma Prince

26. O dinamrquês não fuma Price, Bluemaster e nem Dunhill (derivado das regras 17, 5 e 13).

<br>

### 4. Etapa

* Passo 8, das regras 2 e 25, temos:
    * O sueco não pode estar na casa 1, é noruguês
    * O sueco não pode estar na casa 2, lá tem cavalos
    * O sueco não pode estar na casa 3, é inglês
    * O sueco não pode estar na casa 4, lá bebe café
    * O sueco está na casa 5, bebe cerveja, fuma Bluemaster e tem cachorro `(casa 5 resolvida)`

* Passo 9, da regra 3, temos:
    * Não pode ser as casas 1, 3 e 5 que são respectivamente norueguês, inglês e sueco
    * Não pode ser casa 4 porque bebe café
    * O dinamarquês vive na casa 2 e bebe chá
    * Consequentemente o norueguês bebe água `(todas as bebidas resolvidas)`
    * Consequentemente o alemão mora na casa 5 `(todas as nacionalidades resolvidas)`

* Passo 10, da regra 5, temos:
    * O alemão fuma Prince na casa 4.

* Passo 11, da regra 8, temos:
    * Não pode ser casas 1, 4 e 5 que respecitivamente fumam Dunhill, Prince e Bluemaster
    * Não pode ser casa 2, tem cavalos
    * Quem fuma Pall Mall e tem pássaros mora na casa 3 `(casa 3 resolvida)`
    * Consequentemente quem fuma Blends mora na casa 2 `(todas os cigarros resolvidos)` e `(casa 2 resolvida)`

* Passo 12, das regras 11 e 14, temos:
    * Como Blends está na casa 2 e na casa 3 tem pássaro
    * O Gato está na casa 1 `(casa 1 resolvida)`
    * `Consequentemente o peixe está na casa 4 (enigma resolvido)`

<br>

### Solução completa

| Casa        | 1 🟨       | 2 🟦       | 3 🟥       | 4 🟩       | 5 ⬜       |
|-------------|------------|------------|------------|------------|------------|
| Nacionalidade | Norueguês  | Dinamarquês| Inglês     | Alemão     | Sueco      |
| Cor         | Amarela    | Azul       | Vermelha   | Verde      | Branca     |
| Bebida      | Água       | Chá        | Leite      | Café       | Cerveja    |
| Cigarro     | Dunhill    | Blends     | Pall Mall  | Prince     | Blue Master|
| Animal      | Gato       | Cavalo     | Passaro    | Peixe      | Cachorro   |

<br>

### Etapas e passos da análise

Como segui uma abordagem de analisar sequencialmente cada uma das 15 regras iniciais, a ordem na qual as regras se apresentam podem alterar as descrições de etapas e passos que foram descritos aqui

<br>

---
Para retornar ao resumo do Enigma de Einstein, [clique aqui](./Enigma_Einstein.md)

Para retornar ao README principal, [clique aqui](../README.md)
