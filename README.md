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

## Publicação

O site sai em **https://luwey-silva.github.io/Reflex/**.

A publicação é automática: todo push na `main` que toque em `index.html`,
`assets/` ou `tools/` dispara `.github/workflows/pages.yml`, que regenera a
página a partir do template e publica. Dá pra rodar à mão também, em
**Actions → Publicar site → Run workflow**.

O workflow liga o GitHub Pages sozinho na primeira execução
(`configure-pages` com `enablement: true`) — não precisa mexer em Settings. Se a
organização bloquear isso, o caminho manual é **Settings → Pages → Source →
GitHub Actions** e rodar o workflow de novo.

Como o `index.html` é autocontido e está na raiz, o modo antigo
(**Settings → Pages → Deploy from a branch → `main` / `/root`**) também
funciona — o `.nojekyll` na raiz está lá para isso.

## Notas de conteúdo

A página é **material de trabalho**, não divulgação oficial. Nada que ainda não
foi decidido aparece como fato: combate, número de finais, duração, preço e data
estão marcados como *a definir*, e a seção **Em aberto** lista as dez decisões
que travam o design daqui pra frente.
