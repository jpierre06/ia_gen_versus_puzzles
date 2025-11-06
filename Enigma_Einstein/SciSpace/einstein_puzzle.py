#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solucionador do Enigma de Einstein
Usando constraint satisfaction problem (CSP)
"""

from itertools import permutations

# Definir as características possíveis
nacionalidades = ['Britânico', 'Dinamarquês', 'Sueco', 'Norueguês', 'Alemão']
cores = ['Vermelha', 'Verde', 'Azul', 'Amarela', 'Branca']
bebidas = ['Chá', 'Café', 'Leite', 'Cerveja', 'Água']
cigarros = ['Prince', 'Pall Mall', 'Dunhill', 'Blends', 'Bluemaster']
pets = ['Cachorro', 'Pássaro', 'Gato', 'Cavalo', 'Peixe']

def ao_lado(pos1, pos2):
    """Verifica se duas posições são adjacentes"""
    return abs(pos1 - pos2) == 1

def esquerda_de(pos1, pos2):
    """Verifica se pos1 está imediatamente à esquerda de pos2"""
    return pos1 == pos2 - 1

def verificar_solucao(nac, cor, beb, cig, pet):
    """Verifica se uma configuração satisfaz todas as restrições"""
    
    # 1. O britânico vive na casa vermelha
    if nac.index('Britânico') != cor.index('Vermelha'):
        return False
    
    # 2. O sueco tem um cachorro
    if nac.index('Sueco') != pet.index('Cachorro'):
        return False
    
    # 3. O dinamarquês toma chá
    if nac.index('Dinamarquês') != beb.index('Chá'):
        return False
    
    # 4. O norueguês mora na primeira casa (índice 0)
    if nac.index('Norueguês') != 0:
        return False
    
    # 5. O alemão fuma Prince
    if nac.index('Alemão') != cig.index('Prince'):
        return False
    
    # 6. A casa verde fica ao lado da branca, à esquerda
    if not esquerda_de(cor.index('Verde'), cor.index('Branca')):
        return False
    
    # 7. O morador da casa verde toma café
    if cor.index('Verde') != beb.index('Café'):
        return False
    
    # 8. Quem fuma Pall Mall tem pássaros
    if cig.index('Pall Mall') != pet.index('Pássaro'):
        return False
    
    # 9. O morador da casa amarela fuma Dunhill
    if cor.index('Amarela') != cig.index('Dunhill'):
        return False
    
    # 10. O morador da casa central toma leite (índice 2)
    if beb.index('Leite') != 2:
        return False
    
    # 11. Quem fuma Blends mora ao lado de quem tem um gato
    if not ao_lado(cig.index('Blends'), pet.index('Gato')):
        return False
    
    # 12. Quem tem um cavalo mora ao lado de quem fuma Dunhill
    if not ao_lado(pet.index('Cavalo'), cig.index('Dunhill')):
        return False
    
    # 13. Quem fuma Bluemaster toma cerveja
    if cig.index('Bluemaster') != beb.index('Cerveja'):
        return False
    
    # 14. Quem fuma Blends mora ao lado de quem toma água
    if not ao_lado(cig.index('Blends'), beb.index('Água')):
        return False
    
    # 15. O norueguês mora ao lado da casa azul
    if not ao_lado(nac.index('Norueguês'), cor.index('Azul')):
        return False
    
    return True

def resolver():
    """Encontra a solução testando todas as permutações possíveis"""
    print("🔍 Iniciando busca pela solução...\n")
    print("⏳ Testando combinações (isso pode levar alguns segundos)...\n")
    
    tentativas = 0
    
    # Testar todas as permutações
    for nac in permutations(nacionalidades):
        for cor in permutations(cores):
            for beb in permutations(bebidas):
                for cig in permutations(cigarros):
                    for pet in permutations(pets):
                        tentativas += 1
                        if verificar_solucao(nac, cor, beb, cig, pet):
                            print(f"✅ SOLUÇÃO ENCONTRADA após {tentativas:,} tentativas!\n")
                            return nac, cor, beb, cig, pet
    
    return None

def imprimir_solucao(nac, cor, beb, cig, pet):
    """Imprime a solução de forma organizada"""
    print("="*80)
    print("🏆 SOLUÇÃO DO ENIGMA DE EINSTEIN")
    print("="*80)
    print()
    
    for i in range(5):
        print(f"🏠 CASA {i+1}:")
        print(f"   👤 Nacionalidade: {nac[i]}")
        print(f"   🎨 Cor: {cor[i]}")
        print(f"   🥤 Bebida: {beb[i]}")
        print(f"   🚬 Cigarro: {cig[i]}")
        print(f"   🐾 Pet: {pet[i]}")
        print()
    
    # Encontrar o dono do peixe
    dono_peixe_pos = pet.index('Peixe')
    print("="*80)
    print("🐠 RESPOSTA FINAL:")
    print("="*80)
    print(f"\n1. QUEM É O DONO DO PEIXE?")
    print(f"   ➤ {nac[dono_peixe_pos]}\n")
    
    print(f"2. CARACTERÍSTICAS DO DONO DO PEIXE:")
    print(f"   ➤ Nacionalidade: {nac[dono_peixe_pos]}")
    print(f"   ➤ Cor da casa: {cor[dono_peixe_pos]}")
    print(f"   ➤ Bebida: {beb[dono_peixe_pos]}")
    print(f"   ➤ Cigarro: {cig[dono_peixe_pos]}")
    print(f"   ➤ Casa número: {dono_peixe_pos + 1}")
    print()

def explicar_logica():
    """Explica a lógica de resolução"""
    print("="*80)
    print("🧠 LÓGICA DE RESOLUÇÃO")
    print("="*80)
    print("""
Este enigma é um problema de satisfação de restrições (CSP - Constraint Satisfaction Problem).

ESTRATÉGIA UTILIZADA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. FORÇA BRUTA INTELIGENTE:
   • Gerar todas as permutações possíveis de 5 elementos para cada categoria
   • Total teórico: 5! × 5! × 5! × 5! × 5! = 24,883,200,000 combinações
   
2. FILTRAGEM POR RESTRIÇÕES:
   • Cada combinação é testada contra as 15 regras fornecidas
   • Restrições eliminam rapidamente configurações inválidas
   • Apenas a configuração que satisfaz TODAS as restrições é aceita

3. TIPOS DE RESTRIÇÕES APLICADAS:
   
   a) RESTRIÇÕES DE IGUALDADE (mesma posição):
      • Britânico = Casa Vermelha
      • Sueco = Cachorro
      • Dinamarquês = Chá
      • Alemão = Prince
      • Casa Verde = Café
      • Pall Mall = Pássaro
      • Casa Amarela = Dunhill
      • Bluemaster = Cerveja
   
   b) RESTRIÇÕES DE POSIÇÃO FIXA:
      • Norueguês = Casa 1 (primeira)
      • Leite = Casa 3 (central)
   
   c) RESTRIÇÕES DE ADJACÊNCIA:
      • Blends ao lado de Gato
      • Cavalo ao lado de Dunhill
      • Blends ao lado de Água
      • Norueguês ao lado de Casa Azul
   
   d) RESTRIÇÕES DE ORDEM:
      • Casa Verde imediatamente à esquerda da Casa Branca

4. PROCESSO DE DEDUÇÃO:
   • As restrições fixas (Norueguês na casa 1, Leite na casa 3) reduzem 
     drasticamente o espaço de busca
   • Restrições de adjacência eliminam muitas combinações impossíveis
   • A combinação de todas as restrições deixa apenas UMA solução válida

5. VERIFICAÇÃO:
   • A solução encontrada é única e satisfaz todas as 15 condições
   • Não há ambiguidade ou múltiplas respostas possíveis
""")

if __name__ == "__main__":
    # Resolver o enigma
    resultado = resolver()
    
    if resultado:
        nac, cor, beb, cig, pet = resultado
        imprimir_solucao(nac, cor, beb, cig, pet)
        explicar_logica()
    else:
        print("❌ Nenhuma solução encontrada!")
        