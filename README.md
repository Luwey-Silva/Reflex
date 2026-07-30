# Reflex

Um jogo sobre o intervalo entre ver e agir — medido em milissegundos.

Um sinal aparece, você responde, o número aparece. Tocar antes do sinal conta
como queima de largada.

## Estado

Em desenvolvimento. Ainda não existe build do jogo neste repositório.

O que existe hoje é a página de apresentação em [`docs/`](docs/), que já inclui
um teste de reação jogável (modo _toque único_) rodando direto no navegador.

## Site

`docs/index.html` é uma página única, sem dependências e sem etapa de build —
todo o CSS e o JavaScript estão embutidos no arquivo.

Para ver localmente, abra o arquivo no navegador ou sirva a pasta:

```sh
python3 -m http.server -d docs 8000
```

Para publicar no GitHub Pages: **Settings → Pages → Source: Deploy from a
branch**, e aponte para a pasta `/docs` da branch escolhida.

### Editando o conteúdo

O texto da página é uma primeira versão — os modos listados (_Cascata_,
_Finta_, _Duelo_) são escopo pretendido, não recursos prontos, e a seção está
rotulada assim na página. As faixas de pontuação em milissegundos ficam na
tabela `#bandsBody` e podem ser ajustadas conforme o jogo tomar forma.

Os tempos de espera do teste ficam no topo do script, em `MIN_WAIT` e
`MAX_WAIT`.

## Licença

MIT © 2026 Luwey Da Silva
