# Orbity

![Logo](./imgs/logo.png)

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge)](https://github.com/rwvthrdev/orbity) [![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/rwvthrdev/orbity?style=for-the-badge&logo=github&color=yellow)](https://github.com/rwvthrdev/orbity/stargazers) [![GitHub issues](https://img.shields.io/github/issues/rwvthrdev/orbity?style=for-the-badge&logo=github&color=red)](https://github.com/rwvthrdev/orbity/issues) [![GitHub forks](https://img.shields.io/github/forks/rwvthrdev/orbity?style=for-the-badge&logo=github&color=blueviolet)](https://github.com/rwvthrdev/orbity/forks) 

## Description

Orbity is a program that performs theoretical numerical calculations, using formulas and concepts from classical thermodynamics and mechanics as a basis. In the context of experimental academic rocket launches, more is said about modeling and describing the rocket's trajectory, but something very important is left aside: the functioning of the launch pad.

At first glance, it seems like something to go unnoticed, however, within the base there are also physical phenomena, related mainly to thermodynamics: air expansion, pressure, efficiency. The rocket can be perfectly built, however, if the base delivers an unbalanced launch angle and very low efficiency, the rocket will not have its maximum result and will not reach its best speed and range.

That's what Orbity was created for! It will basically show you, through data, how the rocket and base must behave to achieve their best result. However, it is worth noting that Orbity disregards factors such as: climate and air resistance.

# Installation


<details>
<summary style="font-size:14pt; font-weight: bold;">Requirements</summary>

<br>

- **Git**: To clone repositore. -> [Git Site](https://git-scm.com)
- **Python**: Version 3.13 or higher. ->  [Python Site](https://www.python.org/downloads/)

- Important! On Windows, During Python installation check the "Add Python to PATH" option!

</details>

## Windows

1. Abra o cmd (prompt de comando) e verifique se o git e o python estão instalados

```bash
git --version
```
```bash
python --version
```

2. Clone o repositório

```bash
git clone https://github.com/rwvthrdev/Orbity.git
```

3. Entre na pasta do repositório

```bash
cd orbity
```

4. Crie um ambiente virtual

```bash
python -m venv .venv
```

5. Ative o ambiente virutal

```bash
.venv\Scripts\activate
```

6. Atualize o pip (recomendado)

```bash
python -m pip install --upgrade pip setuptools wheel
```

7. Instale as dependências

```bash
pip install -r requirements.txt
```

8. Rode o arquivo

```bash
python orbity.py
```

## 🐧 Linux

1. Open bash

2. Inside the bash, type

```bash
cd ~/Documents

git clone https://github.com/rwvthrdev/Orbity.git
```

3. Go to the project folder

```bash
cd orbity
```

4. Create a virtual environment

```bash
python3 -m venv .venv
```

5. Activate

```bash
source .venv\bin\activate
```

6. Install the dependencies.

```bash
pip install -r requirements.txt
```

7. Run the project

```bash
python3 orbity.py
```

## Follow me

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://instagram.com/rwvthrdev) 


