# Dualidade: Uma Jornada do Eu

Página-trailer e wiki de desenvolvimento do RPG psicológico **Dualidade: Uma
Jornada do Eu** (RPG Maker MV), montada antes do jogo existir.

## O que tem aqui

| Caminho | O que é |
| --- | --- |
| `index.html` | A página, autocontida — fontes e imagens embutidas, zero requisição externa. Abre com duplo clique ou serve direto no GitHub Pages. |
| `docs/DUALIDADE.md` | O material reunido: premissa, cidades, elenco, os 5 atos, a mecânica das perguntas, sidequests, progresso e o que ainda falta decidir. |
| `tools/page.template.html` | O fonte da página, com marcadores `{{...}}` no lugar dos assets. **Edite aqui**, nunca no `index.html`. |
| `tools/build_page.py` | Troca os marcadores por data URIs e gera o `index.html`. |
| `assets/art/` | Key art original e os recortes usados na página. |
| `assets/fonts/` | Bodoni Moda, Fira Sans e Fira Mono (subconjunto latino, woff2). |

## Como editar

```bash
# 1. mexa no template
$EDITOR tools/page.template.html

# 2. regenere a página
python3 tools/build_page.py
```

O `index.html` é gerado — qualquer alteração feita direto nele some no próximo
build.

## Notas de conteúdo

A página é **material de trabalho**, não divulgação oficial. Nada que ainda não
foi decidido aparece como fato: combate, número de finais, duração, preço e data
estão marcados como *a definir*, e a seção **Em aberto** lista as dez decisões
que travam o design daqui pra frente.
