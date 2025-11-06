# 🧩 SOLUÇÃO DO ENIGMA DE EINSTEIN

# Prompt:


Vamos jogar um jogo chamado "Jogo de Einstein" onde você deve usar as dicas para resolver o enigma.

As características possíveis do jogo são:

1\. Nacionalidade

    a. Britânico
    b. Dinamarquês
    c. Sueco
    d. Norueguês
    e. Alemão

2\. Cor
    
    a. Vermelha
    b. Verde
    c. Azul
    d. Amarela
    e. Branca

3\. Bebida

    a. Chá
    b. Café
    c. Leite
    d. Cerveja
    e. Água

4\. Cigarro

    a. Prince
    b. Pall Mall
    c. Dunhill
    d. Blends
    e. Bluemaster

5\. Pet

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

<br>

Responda:

1. "Quem é o dono do peixe?"

2. "Quais as outras características do dono do peixe"

Detalhe a lógica utilizada para chegar a conclusão da sua resposta

<br>

# Response:

Vou resolver este famoso enigma de Einstein usando lógica dedutiva passo a passo!

🧩 Iniciando a resolução do Enigma de Einstein
Vou criar um programa Python para resolver sistematicamente este puzzle usando as restrições fornecidas.

`Wrote file ->  einstein_puzzle.py´

🚀 Executando o solucionador do enigma

FailedCommand

⚡ Otimizando a solução para execução mais rápida
O algoritmo de força bruta completo está demorando muito. Vou criar uma versão otimizada usando dedução lógica passo a passo:

`Wrote file ->  einstein_optimized.py`

Command
  `cd /home/sandbox && timeout 30 python3 einstein_optimized.py`

Perfeito! Agora vou criar um documento detalhado com a lógica completa da resolução:

`Wrote file -> solucao_enigma_einstein.md`


<br>


# 📋 RESPOSTAS FINAIS

### 1️⃣ Quem é o dono do peixe?
**Resposta: O ALEMÃO** 🇩🇪

### 2️⃣ Características do dono do peixe:
- **Nacionalidade:** Alemão
- **Cor da casa:** Verde
- **Bebida:** Café
- **Cigarro:** Prince
- **Pet:** Peixe 🐠
- **Posição:** Casa 4 (quarta casa)

---

## 🏆 SOLUÇÃO COMPLETA

| Casa | Nacionalidade | Cor | Bebida | Cigarro | Pet |
|------|---------------|-----|--------|---------|-----|
| **1** | Norueguês | Amarela | Água | Dunhill | Gato |
| **2** | Dinamarquês | Azul | Chá | Blends | Cavalo |
| **3** | Britânico | Vermelha | Leite | Pall Mall | Pássaro |
| **4** | **Alemão** | **Verde** | **Café** | **Prince** | **Peixe** 🐠 |
| **5** | Sueco | Branca | Cerveja | Bluemaster | Cachorro |

---

## 🧠 LÓGICA DETALHADA DA RESOLUÇÃO

### 🔍 Metodologia Utilizada

Este enigma é um **Problema de Satisfação de Restrições (CSP - Constraint Satisfaction Problem)**. A solução foi obtida através de **dedução lógica sistemática**, aplicando as 15 regras fornecidas em sequência estratégica.

### 📊 Tipos de Restrições

#### 1. **Restrições de Posição Fixa**
- Regra 4: Norueguês mora na **primeira casa**
- Regra 10: A casa **central (3)** tem **leite**

#### 2. **Restrições de Igualdade** (mesma casa)
- Regra 1: Britânico = Casa Vermelha
- Regra 2: Sueco = Cachorro
- Regra 3: Dinamarquês = Chá
- Regra 5: Alemão = Prince
- Regra 7: Casa Verde = Café
- Regra 8: Pall Mall = Pássaro
- Regra 9: Casa Amarela = Dunhill
- Regra 13: Bluemaster = Cerveja

#### 3. **Restrições de Adjacência**
- Regra 11: Blends ao lado de Gato
- Regra 12: Cavalo ao lado de Dunhill
- Regra 14: Blends ao lado de Água
- Regra 15: Norueguês ao lado de Casa Azul

#### 4. **Restrições de Ordem Específica**
- Regra 6: Casa Verde **imediatamente à esquerda** da Casa Branca

---

## 🔢 PASSOS DA DEDUÇÃO LÓGICA

### **PASSO 1: Aplicar Restrições Fixas**
```
✓ Casa 1: Norueguês (regra 4)
✓ Casa 3: Leite (regra 10)
```
**Raciocínio:** Estas são as únicas restrições absolutas de posição, então começamos por elas.

---

### **PASSO 2: Deduzir Casa Azul**
```
✓ Casa 2: Azul (regra 15)
```
**Raciocínio:** 
- Regra 15 diz que o Norueguês mora ao lado da casa azul
- Norueguês está na casa 1 (Passo 1)
- "Ao lado" significa adjacente, então casa azul = casa 2

---

### **PASSO 3: Posicionar Casas Verde e Branca**
```
✓ Casa 4: Verde + Café (regras 6 e 7)
✓ Casa 5: Branca
```
**Raciocínio:**
- Regra 6: Verde está imediatamente à esquerda de Branca (adjacentes)
- Regra 7: Casa Verde = Café
- Casa 2 é azul, então Verde-Branca podem ser:
  - Casas 3-4, ou
  - Casas 4-5
- Casa 3 tem **leite** (não café), então Verde ≠ Casa 3
- **Conclusão:** Verde = Casa 4, Branca = Casa 5

---

### **PASSO 4: Cores Restantes (Vermelha e Amarela)**
```
✓ Casa 1: Amarela + Dunhill (regra 9)
✓ Casa 3: Vermelha
```
**Raciocínio:**
- Regra 9: Casa Amarela = Dunhill
- Cores já definidas: Azul(2), Verde(4), Branca(5)
- Restam: Vermelha e Amarela para casas 1 e 3
- Aplicando regra 9, deduzimos que casa 1 é amarela

---

### **PASSO 5: Localizar o Britânico**
```
✓ Casa 3: Britânico (regra 1)
```
**Raciocínio:**
- Regra 1: Britânico vive na casa vermelha
- Casa vermelha = Casa 3 (Passo 4)

---

### **PASSO 6: Posicionar o Cavalo**
```
✓ Casa 2: Cavalo (regra 12)
```
**Raciocínio:**
- Regra 12: Cavalo mora ao lado de quem fuma Dunhill
- Dunhill está na casa 1 (Passo 4)
- Adjacente à casa 1: apenas casa 2

---

### **PASSO 7: Deduzir Blends e Água**
```
✓ Casa 2: Blends (regras 11 e 14)
✓ Casa 1: Água (regra 14)
```
**Raciocínio:**
- Regra 14: Blends ao lado de Água
- Regra 11: Blends ao lado de Gato
- Bebidas definidas: Leite(3), Café(4)
- Bebidas restantes: Chá, Cerveja, Água
- Analisando adjacências e restrições, Blends = Casa 2
- Portanto, Água = Casa 1 (adjacente a Blends)

---

### **PASSO 8: Posicionar o Gato**
```
✓ Casa 3: Gato (regra 11)
```
**Raciocínio:**
- Regra 11: Gato ao lado de Blends
- Blends está na casa 2
- Adjacentes à casa 2: casas 1 e 3
- Testando as possibilidades, Gato = Casa 3

---

### **PASSO 9: Dinamarquês e Chá**
```
✓ Casa 2: Dinamarquês + Chá (regra 3)
```
**Raciocínio:**
- Regra 3: Dinamarquês = Chá
- Bebidas restantes: Chá e Cerveja para casas 2 e 5
- Nacionalidades definidas: Norueguês(1), Britânico(3)
- Dinamarquês deve estar em casa 2, 4 ou 5
- Como casa 2 precisa de uma bebida e Dinamarquês toma chá, encaixa perfeitamente

---

### **PASSO 10: Cerveja e Bluemaster**
```
✓ Casa 5: Cerveja + Bluemaster (regra 13)
```
**Raciocínio:**
- Regra 13: Bluemaster = Cerveja
- Única bebida restante: Cerveja para casa 5
- Portanto, Bluemaster também está na casa 5

---

### **PASSO 11: Alemão e Prince**
```
✓ Casa 4: Alemão + Prince (regra 5)
```
**Raciocínio:**
- Regra 5: Alemão = Prince
- Nacionalidades restantes: Alemão e Sueco para casas 4 e 5
- Cigarros restantes: Prince e Pall Mall para casas 3 e 4
- Casa 5 já tem Bluemaster, então Prince está em casa 3 ou 4
- Por eliminação e regra 5, Alemão = Casa 4

---

### **PASSO 12: Sueco e Pall Mall**
```
✓ Casa 5: Sueco
✓ Casa 3: Pall Mall
```
**Raciocínio:**
- Nacionalidade restante: Sueco = Casa 5
- Cigarro restante: Pall Mall = Casa 3

---

### **PASSO 13: Localizar o Pássaro**
```
✓ Casa 3: Pássaro (regra 8)
```
**Raciocínio:**
- Regra 8: Pall Mall = Pássaro
- Pall Mall está na casa 3
- Portanto, Pássaro = Casa 3

---

### **PASSO 14: Posicionar o Cachorro**
```
✓ Casa 5: Cachorro (regra 2)
```
**Raciocínio:**
- Regra 2: Sueco = Cachorro
- Sueco está na casa 5
- Portanto, Cachorro = Casa 5

---

### **PASSO 15: O PEIXE (Dedução Final)** 🐠
```
✓ Casa 1: Gato (já definido no Passo 8)
✓ Casa 4: PEIXE
```
**Raciocínio:**
- Pets já atribuídos: Gato(1), Cavalo(2), Pássaro(3), Cachorro(5)
- **Único pet restante: PEIXE**
- **Única casa restante: Casa 4**
- **Casa 4 pertence ao ALEMÃO**

**✅ CONCLUSÃO: O ALEMÃO é o dono do peixe!**

---

## 🎯 VERIFICAÇÃO DAS 15 REGRAS

Vamos verificar se a solução satisfaz todas as regras:

| # | Regra | Verificação |
|---|-------|-------------|
| 1 | Britânico vive na casa vermelha | ✅ Britânico = Casa 3 (Vermelha) |
| 2 | Sueco tem cachorro | ✅ Sueco = Casa 5, Cachorro = Casa 5 |
| 3 | Dinamarquês toma chá | ✅ Dinamarquês = Casa 2, Chá = Casa 2 |
| 4 | Norueguês mora na primeira casa | ✅ Norueguês = Casa 1 |
| 5 | Alemão fuma Prince | ✅ Alemão = Casa 4, Prince = Casa 4 |
| 6 | Casa verde à esquerda da branca | ✅ Verde = Casa 4, Branca = Casa 5 |
| 7 | Casa verde toma café | ✅ Verde = Casa 4, Café = Casa 4 |
| 8 | Pall Mall tem pássaros | ✅ Pall Mall = Casa 3, Pássaro = Casa 3 |
| 9 | Casa amarela fuma Dunhill | ✅ Amarela = Casa 1, Dunhill = Casa 1 |
| 10 | Casa central toma leite | ✅ Casa 3 (central), Leite = Casa 3 |
| 11 | Blends ao lado de gato | ✅ Blends = Casa 2, Gato = Casa 3 (adjacentes) |
| 12 | Cavalo ao lado de Dunhill | ✅ Cavalo = Casa 2, Dunhill = Casa 1 (adjacentes) |
| 13 | Bluemaster toma cerveja | ✅ Bluemaster = Casa 5, Cerveja = Casa 5 |
| 14 | Blends ao lado de água | ✅ Blends = Casa 2, Água = Casa 1 (adjacentes) |
| 15 | Norueguês ao lado da casa azul | ✅ Norueguês = Casa 1, Azul = Casa 2 (adjacentes) |

**✅ TODAS AS 15 REGRAS SATISFEITAS!**

---

## 🔬 ANÁLISE DA COMPLEXIDADE

### Espaço de Busca
- **Permutações possíveis:** 5! × 5! × 5! × 5! × 5! = **24.883.200.000** combinações
- **Solução única:** Apenas **1** combinação satisfaz todas as restrições
- **Probabilidade aleatória:** 1 em 24 bilhões

### Estratégia de Resolução
1. **Dedução Lógica Sequencial:** Aplicar restrições em ordem estratégica
2. **Propagação de Restrições:** Cada dedução limita as possibilidades seguintes
3. **Eliminação por Contradição:** Descartar configurações impossíveis
4. **Verificação Completa:** Confirmar que todas as 15 regras são satisfeitas

---

## 💡 CONCLUSÃO

O **Enigma de Einstein** demonstra o poder da lógica dedutiva e do raciocínio sistemático. Embora o espaço de busca seja imenso (24 bilhões de combinações), a aplicação cuidadosa das restrições reduz drasticamente as possibilidades até restar apenas uma solução única e verificável.

**Resposta Final:** O **Alemão** é o dono do peixe, morando na **casa verde (4)**, tomando **café** e fumando **Prince**. 🐠🇩🇪

---

## 📚 Curiosidades

- Este enigma é atribuído a **Albert Einstein**, que supostamente o criou quando criança
- Diz-se que Einstein afirmou que apenas **2% da população mundial** consegue resolver este enigma
- É um exemplo clássico de **Problema de Satisfação de Restrições (CSP)** usado em Inteligência Artificial
- A solução requer **raciocínio lógico puro**, sem necessidade de conhecimento especializado

---

**Documento gerado por SciSpace Research Agent**  
*Data: 2025-11-05*

---
Para retornar ao resumo do Enigma de Einstein, [clique aqui](./Enigma_Einstein.md)

Para retornar ao README principal, [clique aqui](../README.md)


