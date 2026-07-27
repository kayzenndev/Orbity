# Orbity

![Banner](./imgs/banner.png)

[![Version](https://img.shields.io/badge/version-1.0.0.1-blue.svg?style=for-the-badge)](https://github.com/kayzenndev/orbity) [![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/kayzenndev/orbity?style=for-the-badge&logo=github&color=yellow)](https://github.com/kayzenndev/orbity/stargazers) [![GitHub issues](https://img.shields.io/github/issues/kayzenndev/orbity?style=for-the-badge&logo=github&color=red)](https://github.com/kayzenndev/orbity/issues) [![GitHub forks](https://img.shields.io/github/forks/kayzenndev/orbity?style=for-the-badge&logo=github&color=blueviolet)](https://github.com/kayzenndev/orbity/forks) [![Made in Brazil](https://img.shields.io/badge/MADE_IN_BRAZIL-BR-009739?style=for-the-badge)](https://github.com/kayzenndev/orbity)

## Description

O **Orbity** é um programa que realiza cálculos numéricos teóricos, usando fórmulas e conceitos da **termodinâmica e mecânica clássicas** como base. No contexto de lançamentos acadêmicos experimentais de foguetes, fala-se mais sobre modelagem e descrição da trajetória do foguete, mas algo muito importante é deixado de lado: **o funcionamento da plataforma de lançamento**.

À primeira vista, parece algo que passa despercebido, porém **dentro da base também ocorrem fenômenos físicos**, relacionados principalmente à termodinâmica: expansão do ar, pressão, eficiência. O foguete pode ser perfeitamente construído, no entanto, se a base oferecer um **ângulo de lançamento desequilibrado e eficiência muito baixa**, o foguete não terá seu resultado máximo e não atingirá sua melhor velocidade e alcance.

Foi para isso que o Orbity foi criado! Ele basicamente mostrará a você, por meio de dados, como o foguete e a base devem se comportar para alcançar seu melhor resultado. Entretanto, vale ressaltar que a Orbity desconsidera fatores como: clima e resistência do ar.

## Context

A **MOFOG e a OBAFOG** são iniciativas educacionais ligadas ao ensino de ciência, tecnologia e física de forma prática e interativa. A MOBFOG (Mostra Brasileira de Foguetes), organizada junto da Olimpíada Brasileira de Astronomia e Astronáutica, desafia estudantes a construírem e lançarem foguetes utilizando materiais simples, **aplicando conceitos científicos na prática, como pressão, aerodinâmica, impulso e as Leis de Newton.**

Durante o desenvolvimento dos foguetes, os participantes precisam analisar fatores como estabilidade, alcance, velocidade e trajetória, transformando teoria em experimentação real. Além do aprendizado científico, a competição incentiva criatividade, trabalho em equipe, pensamento lógico e resolução de problemas.

Foi nesse contexto que surgiu o Orbity, um programa desenvolvido para auxiliar na organização, análise e acompanhamento de lançamentos e informações relacionadas aos foguetes. O objetivo do Orbity é aproximar ainda mais os estudantes da tecnologia e da exploração espacial, oferecendo uma ferramenta moderna que complementa a experiência prática da MOFOG e da OBAFOG.

## Development Status

O desenvolvimento do Orbity foi dividido em duas etapas principais. Nesta primeira fase, o programa realiza cálculos de trajetória utilizando um modelo físico simplificado, considerando apenas as variáveis básicas do movimento e desconsiderando fatores mais complexos, como resistência do ar, vento e outras interferências externas. Dessa forma, o sistema consegue gerar simulações iniciais de maneira mais simples e didática, facilitando o entendimento dos conceitos fundamentais da física aplicada aos foguetes.

Agora, também foi implementada a segunda parte do projeto, responsável por tornar as simulações muito mais precisas e realistas. Nessa etapa, o Orbity passará a utilizar o método numérico de Runge-Kutta juntamente com equações diferenciais, permitindo calcular a trajetória do foguete levando em consideração variáveis físicas mais complexas, como arrasto aerodinâmico, aceleração variável e influência do ambiente no voo. Com isso, o programa evoluirá de uma simulação básica para um sistema mais avançado de modelagem de trajetórias.

# Installation

<details>
<summary>Requirements</summary>


- **Git**: To clone repositore. -> [Git Site](https://git-scm.com)
- **Python**: Version 3.13 or higher. ->  [Python Site](https://www.python.org/downloads/)

- Important! On Windows, During Python installation check the "Add Python to PATH" option!

</details>

## Windows

1. Abra o prompt de comando e verifique se o git e o python estão instalados

```bash
git --version
python --version
```
2. Entre na pasta de downloads e clone o repo

```bash
cd Downloads
git clone https://github.com/kayzenndev/Orbity.git
```

3. Entre na pasta do repositório crie um ambiente virtual e ative-o

```bash
cd orbity
python -m venv .venv
.venv\Scripts\activate
```

4. Atualize o pip (recomendado) e instale as dependências

```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
5. Rode o arquivo

```bash
python orbity.py
```

## Fedora 44

1. Abra o konsole e digite os comandos

```bash
ls 
cd ~/Downloads 
git clone https://github.com/kayzenndev/Orbity.git
cd Orbity
```
2. Crie um ambiente virtual e ative-o

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Instale o tkinter para rodar o ambiente gráfico

```bash
sudo dnf install python3-tkinter
```

5. Rode o arquivo

```bash
python3 orbity.py
```

## Ubuntu 24.4.3 LTS

1. Abra o terminal e digite os comandos

```bash
ls 
cd ~/Downloads 
git clone https://github.com/kayzenndev/Orbity.git
```
2. Crie um ambiente virtual e ative-o

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

4. Instale o tkinter para rodar o ambiente gráfico

```bash
sudo apt install python3-tk
```

5. Rode o arquivo

```bash
python3 orbity.py
```

# Agradecimentos

A jornada até aqui foi longa. Foram longos meses pesquisando, testando e aprimorando o programa. Períodos de testes durante nossa oficina no X Encontro de Iniciação Científica, nos mostraram o quão longa inda seria essa jornada. 

Com muita determinação, correção de erros, aprendizados, testes, foi possível chegar até aqui e entregar esse programa. Por isso, gostaria de agradecer a cada um dos apoiadores. Ao nosso professor e apoiador Dr. Karciano José, pela oportunidade e pelos ensinamentos. E a todos que utilizam e contribuem com testes para que esse projeto funcione de maneira correta.

Espero que possamos contribuir com a comunidade científica, de modo a ampliar os conhecimentos e as pesquisas.

A Deus, toda honra e toda glória para sempre!

"A fé na vitória deve ser inabalável" - O RAPPA, Anjos pra quem tem fé.

# Contribua com o projeto
Avaliação de erros: https://forms.gle/KWKoMNjBv1nr7RFK6

Pesquisa de Avaliação: https://forms.gle/ySar9SAhd379FQxeA

## Redes sociais 

<a href="https://www.instagram.com/kayzenndev" target="_blank">
    <img src="./imgs/kayzendev.png" alt="Perfil do instagram" width='128px'>
</a>
<a href="https://www.instagram.com/matheusramos9_" target="_blank">
    <img src="./imgs/matheus.png" alt="Perfil do instagram" width='128px'>
</a>
<a href="https://www.instagram.com/g.u.i.l.h.e.r.m.e.0.2" target="_blank">
    <img src="./imgs/guilherme.png" alt="Perfil do instagram" width='128px'>
</a>
<a href="https://www.instagram.com/_karciano" target="_blank">
    <img src="./imgs/karciano.png" alt="Perfil do instagram" width='128px'>
</a>

---

# Notas

- Última atualização: 27 de Julho de 2026.
- IDE: Visual Studio Code
- Livros: Tópicos de Física, HELOU, GUALTER, NEWTON. Volume 1 e 2 : Mecânica e Termodinâmica.

---
```                                                       
██ ▄█▀  ▄▄▄  ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄▄ ▄▄  ▄▄ ▄▄  ▄▄ ▄▄▄▄  ▄▄▄▄▄ ▄▄ ▄▄ 
████   ██▀██ ▀███▀   ▄█▀ ██▄▄  ███▄██ ███▄██ ██▀██ ██▄▄  ██▄██ 
██ ▀█▄ ██▀██   █   ▄██▄▄ ██▄▄▄ ██ ▀██ ██ ▀██ ████▀ ██▄▄▄  ▀█▀                                         
```
---