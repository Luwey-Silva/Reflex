# Desenvolvimento — a página de Dualidade

Como a página publicada é gerada e como ela vai ao ar. O conteúdo do jogo em si
está no [README](../README.md) e em [`DUALIDADE.md`](DUALIDADE.md).

## Estrutura

| Caminho | O que é |
| --- | --- |
| `index.html` | A página, autocontida — fontes e imagens embutidas, zero requisição externa. **Gerado.** |
| `tools/page.template.html` | O fonte da página, com marcadores `{{...}}` no lugar dos assets. **É aqui que se edita.** |
| `tools/build_page.py` | Troca os marcadores por data URIs e gera o `index.html`. |
| `assets/art/` | Key art original e os recortes usados na página. |
| `assets/fonts/` | Bodoni Moda, Fira Sans e Fira Mono (subconjunto latino, woff2). |
| `docs/DUALIDADE.md` | O material reunido: premissa, cidades, elenco, os 5 atos, a mecânica das perguntas, sidequests, progresso e o que ainda falta decidir. |

> **Não edite o `index.html` direto.** Ele é regenerado a partir do template a
> cada publicação — qualquer alteração feita nele some no próximo deploy, sem
> aviso.

## Editar

```sh
# 1. mexa no template
$EDITOR tools/page.template.html

# 2. regenere a página
python3 tools/build_page.py
```

O `build_page.py` não tem dependência nenhuma: só a biblioteca padrão do Python.
Ele falha com mensagem clara se faltar um asset ou sobrar um marcador não
resolvido, então um build que passa é um build íntegro.

Para ver o resultado, abra o `index.html` no navegador — ele funciona offline,
inclusive por `file://`.

## Publicação

O workflow [`.github/workflows/pages.yml`](../.github/workflows/pages.yml) roda
a cada push na `main` que toque a página, regenera o `index.html` a partir do
template e publica no GitHub Pages. Também dá pra rodar à mão em
**Actions → Publicar site → Run workflow**.

Duas páginas vão ao ar juntas:

| Caminho | Página | Fonte |
| --- | --- | --- |
| `/` | Wiki de Dualidade | `index.html` |
| `/reflex/` | Teste de tempo de reação | `docs/index.html` |

### Ligar o Pages (uma vez só)

O workflow não consegue ligar o Pages sozinho: o `GITHUB_TOKEN` não tem
permissão para criar o site, e o deploy falha com `404 — Ensure GitHub Pages has
been enabled`. Antes do primeiro deploy, vá em:

**Settings → Pages → Build and deployment → Source: GitHub Actions**

Depois disso todo push na `main` publica sozinho.
