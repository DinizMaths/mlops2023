# Description

# Instalation

```bash
$ git clone https://github.com/DinizMaths/mlops2023.git
```

```bash
$ cd mlops2023/Python_Essentials_for_MLOps/"Project 02"/
```

```
$ pip install -r requirements.txt
```

```bash
export AIRFLOW_HOME=$(pwd)

export AIRFLOW_VERSION=2.7.1
export PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow db init

airflow standalone
```

In airflow.cfg, change the following lines:

```bash
load_examples = False
```

```bash
mkdir dags
```

```bash
wget https://www.sqlite.org/2023/sqlite-tools-linux-x86-3430100.zip
unzip sqlite-tools-linux-x86-3430100.zip
rm sqlite-tools-linux-x86-3430100.zip
```

```bash	
cd sqlite-tools-linux-x86-3430100
sqlite3 ../episodes.db
.databases
.quit
cd ../
```

```bash
export CONN_HOST=$(pwd)/episodes.db
airflow connections add 'podcasts' --conn-type 'sqlite' --conn-host "${CONN_HOST}"
airflow connections get 'podcasts'
```

# References

[🌐 **Build an Airflow Data Pipeline to Download Podcasts**](https://app.dataquest.io/c/93/m/999911/build-an-airflow-data-pipeline-to-download-podcasts/)