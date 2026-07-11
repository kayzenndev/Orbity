# Orbity

![Banner](./imgs/banner.png)

[![Version](https://img.shields.io/badge/version-1.0.0.1-blue.svg?style=for-the-badge)](https://github.com/kayzenndev/orbity) [![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/kayzenndev/orbity?style=for-the-badge&logo=github&color=yellow)](https://github.com/kayzenndev/orbity/stargazers) [![GitHub issues](https://img.shields.io/github/issues/kayzenndev/orbity?style=for-the-badge&logo=github&color=red)](https://github.com/kayzenndev/orbity/issues) [![GitHub forks](https://img.shields.io/github/forks/kayzenndev/orbity?style=for-the-badge&logo=github&color=blueviolet)](https://github.com/kayzenndev/orbity/forks) 

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

Posteriormente, será implementada a segunda parte do projeto, responsável por tornar as simulações muito mais precisas e realistas. Nessa etapa, o Orbity passará a utilizar o método numérico de Runge-Kutta juntamente com equações diferenciais, permitindo calcular a trajetória do foguete levando em consideração variáveis físicas mais complexas, como arrasto aerodinâmico, aceleração variável e influência do ambiente no voo. Com isso, o programa evoluirá de uma simulação básica para um sistema mais avançado de modelagem de trajetórias.

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

4. Rode o arquivo

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

4. Instale o thinker para rodar o ambiente gráfico

```bash
sudo apt install python3-tk
```

5. Rode o arquivo

```bash
python3 orbity.py
```

# Notes

Fazeno :/
