## Dualidade: Uma Jornada do Eu

Página-trailer e wiki de desenvolvimento do RPG psicológico **Dualidade: Uma
Jornada do Eu** (RPG Maker MV), montada antes do jogo existir.

| Caminho | O que é |
| --- | --- |
| `index.html` | A página, autocontida — fontes e imagens embutidas, zero requisição externa. **Gerado**: não edite direto. |
| `docs/DUALIDADE.md` | O material reunido: premissa, cidades, elenco, os 5 atos, a mecânica das perguntas, sidequests, progresso e o que ainda falta decidir. |
| `tools/page.template.html` | O fonte da página, com marcadores `{{...}}` no lugar dos assets. **Edite aqui.** |
| `tools/build_page.py` | Troca os marcadores por data URIs e gera o `index.html`. |
| `assets/art/` | Key art original e os recortes usados na página. |
| `assets/fonts/` | Bodoni Moda, Fira Sans e Fira Mono (subconjunto latino, woff2). |

```sh
# 1. mexa no template
$EDITOR tools/page.template.html

# 2. regenere a página
python3 tools/build_page.py
```

A página é **material de trabalho**, não divulgação oficial. Nada que ainda não
foi decidido aparece como fato: combate, número de finais, duração, preço e data
estão marcados como *a definir*, e a seção **Em aberto** lista as dez decisões
que travam o design daqui pra frente.

---

## Publicação

As duas páginas saem juntas em **https://luwey-silva.github.io/Reflex/**, pelo
workflow `.github/workflows/pages.yml`. Ele roda a cada push na `main` que toque
qualquer uma delas, regenera o `index.html` a partir do template e publica.
Também dá pra rodar à mão em **Actions → Publicar site → Run workflow**.

### Ligar o Pages (uma vez só)

O workflow não consegue ligar o Pages sozinho — o `GITHUB_TOKEN` não tem essa
permissão. Antes do primeiro deploy, vá em:

**Settings → Pages → Build and deployment → Source: GitHub Actions**

Depois disso todo push na `main` publica sozinho.

## Licença

MIT © 2026 Luwey Da Silva
