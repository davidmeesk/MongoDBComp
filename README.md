<h1 align="center">Comparação eficiência PostgreSQL</h1>

<p align="center">
  <p align="center">Comparação de SGBDs para um TCC</p>
  <a href="#-como-instalar">Como instalar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## 🤓 Como instalar
* Crie o **virtual environment** dentro do diretório do repositório<br>
`$ python3 -m venv nba_env`<br>

* Ativando o **virtual environment**<br>
`$ source nba_env/bin/activate` (MacOS e Linux) **ou** <br>
`$ nba_env\Scripts\activate` (Windows)<br>

* Instalando as dependências (repetir esses 2 passos a cada vez que um novo pacote for instalado)<br>
`$ /usr/local/opt/postgres/bin/createuser -s postgres` (***apenas se*** utiliza MacOS + HomeBrew)<br>
`$ pip install -r requirements.txt`

* Inicie o servidor do MongoDB<br>
`$ sudo systemctl start mongod.service`
`$ sudo systemctl status mongod`


## 💻 Como executar
* Rodar o back-end<br>
`$ export FLASK_APP=app`
`$ flask run`

## 🎯 Consultas disponibilizadas por endpoints
*  `http://localhost:5000/api/<Nome Função>`
