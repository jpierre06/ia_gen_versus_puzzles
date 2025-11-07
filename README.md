## 🎯 Objetivo

Este repositório documenta experimentos e históricos de conversas com IAs generativas usadas para resolver puzzles de lógica. O foco principal é registrar prompts, respostas, iterações e raciocínios das IAs — para comparar abordagens, identificar falhas e extrair lições sobre engenharia de prompt e verificação lógica.

### 🤖 Enigma de Einstein

O primeiro puzzle a ser testado foi o Enigma de Einstein.

Para mais detalhes, [clique aqui](./Enigma_Einstein/Enigma_Einstein.md)

## 🗂️ Conteúdo do repositório

- `Enigma_Einstein/` — Análises e notas sobre o "Teste de Einstein". Contém descrições das tentativas e observações sobre o comportamento de diferentes modelos.
    - `ChatGPT.md` — (reservado para export de uma sessão com o modelo ChatGPT).
    - `Claude.md` — Export de uma sessão com o modelo Claude.ai.
    - `Enigma_Einstein.md` — Texto com descrição, resultados e conclusões.
    - `Gemini_2.5-flash.md` — Export de uma sessão com o modelo Gemini (ex.: tentativa detalhada e saídas).
    - `NotebookLM/` - Diretório com prompt usado pelo NotebookLM.
        - `Prompt.txt` — Prompt usado pelo NotebookLM.
    - `SciSpace.md` — Export de uma sessão com o modelo SciSpace.
    - `SciSpace/` - Diretório com conteúdo gerado pelo SciSpace.
         - `einstein_puzzle.py` — Script Python gerado na primeira tentativa de resolver o puzzle.
         - `einstein_optimized.py` — Script Python gerado na segunda tentativa de resolver o puzzle.
- `Enigma_Nordestino/` — (Pasta reservada para outro puzzle ou conjunto de experimentos relacionados).

## 📌 Motivação e objetivos específicos

- Registrar como diferentes IAs (modelos e versões) resolvem o mesmo problema de lógica.
- Capturar erros comuns, omissões e vieses de raciocínio que aparecem nas respostas geradas.
- Documentar prompts efetivos e estratégias de engenharia de prompt que melhoram precisão e consistência lógica.

## ▶️ Como usar este repositório

1. Abra a pasta `Enigma_Einstein` para ver a análise detalhada do puzzle "Teste de Einstein". O arquivo `Enigma_Einstein.md` resume o experimento e traz a solução final, bem como comparações entre diferentes modelos.
2. Leia os arquivos de export (por exemplo, `Gemini_2.5-flash.md`) para acompanhar a conversa completa e as tentativas interativas.
3. Sempre que for reproduzir os experimentos, mantenha um registro das entradas (prompt), das versões dos modelos e das instruções adicionais fornecidas — esses dados são essenciais para comparar resultados.

## 🔍 Notas sobre reprodutibilidade

- Anote a data, o modelo (nome e versão), e o prompt completo para cada sessão.
- Pequenas mudanças no prompt (formatação, ênfases, ou instruções de verificação) podem alterar significativamente o resultado.

## 🤝 Contribuições

Contribuições são bem-vindas. Sugestões de novos puzzles, comparações entre modelos, correções de análises e scripts para verificar soluções automaticamente são úteis.

Enviar email para:
- jps.data.analise@gmail.com

## 📄 Licença

Este repositório pode ser usado para fins educacionais e de pesquisa. Se desejar, especifique uma licença (por exemplo, MIT) criando um arquivo `LICENSE.md`.

---
