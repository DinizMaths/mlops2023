# 📝 Description

Airflow is a platform created by Airbnb. It is a very powerful tool that can be used to automate a lot of tasks. 

<img src="https://airflow.apache.org/blog/airflow-2.7.0/graph_in_grid.png">

In this project, we will use Airflow to **download podcasts** from the [**Marketplace**]( https://www.marketplace.org/feed/podcast/marketplace/).



# 📦 Instalation

First, clone the repository:

```bash
$ git clone https://github.com/DinizMaths/mlops2023.git
```

Then, go to the project folder:

```bash
$ cd mlops2023/Python_Essentials_for_MLOps/Project_02/
```

For a better experience, I recommend you to create a virtual environment and activate it. Finally, you need to install the requirements:

```
$ pip install -r requirements.txt
```

Now, you will need to set the `AIRFLOW_HOME` environment variable. You can do this by running the following command:

```bash
export AIRFLOW_HOME=$(pwd)/airflow
```

# 🚀 Usage

After set the Airflow home, you need to initialize the database:

```bash
airflow db init
```

Now, you can run the standalone mode:
    
```bash
airflow standalone
```

(Optional) If you don't want to load the examples, you can change the configuration file. In `./airflow/airflow.cfg`, change the value of `load_examples` to `False`. This will prevent the examples from being loaded.

```bash
sed -i 's/^load_examples = .*/load_examples = False/' airflow.cfg
```

Now in **other terminal**, you can run the following command to create the `episodes` folder:

```bash
mkdir ./airflow/episodes
```

For this project, we will use a SQLite database. To create the database, run the following commands:

```bash
wget https://www.sqlite.org/2023/sqlite-tools-linux-x86-3430100.zip
unzip sqlite-tools-linux-x86-3430100.zip
rm sqlite-tools-linux-x86-3430100.zip
mv ./sqlite-tools-linux-x86-3430100/sqlite3 ./airflow/sqlite3
rm -rf ./sqlite-tools-linux-x86-3430100
```

This will download the SQLite tools and move the `sqlite3` executable to the `airflow` folder. Now, you can create the database:

```bash	
cd airflow
sqlite3 episodes.db
.databases
.quit
cd ../
```

At this point, you can run the following command to create the `podcasts` connection:

```bash
export AIRFLOW_HOME=$(pwd)/airflow
export CONN_HOST=${AIRFLOW_HOME}/episodes.db
airflow connections add 'podcasts' --conn-type 'sqlite' --conn-host "${CONN_HOST}"
```

At last, you can open the [**Airflow UI**](http://localhost:8080/home) in your browser. It will needs a username and password. The default username is `admin` and the password is located in `./airflow/standalone_admin_password.txt`.

Only one step before running the DAG. You need to change the value of `EPISODE_FOLDER` inside `./airflow/dags/podcast_summary.py` to the path of the `episodes` folder. If you want to know the path, you can run the following command:

```bash
echo $(pwd)/airflow/episodes
```
Now, you can run the DAG. After running the DAG called `podcast_summary`, if your result is similar to the following image:

<img src="./imgs/success_airflow.png" >

Your podcasts was downloaded successfully! 🎉

And you can find the downloaded podcasts in `./airflow/episodes/`.

(Optional) You can run other versions of the DAG that uses decorators. The file is `./airflow/dags/podcast_summary_old.py`

# 📚 References

[🌐 **Build an Airflow Data Pipeline to Download Podcasts**](https://app.dataquest.io/c/93/m/999911/build-an-airflow-data-pipeline-to-download-podcasts/)

[🌐 **Apache Airflow**](https://airflow.apache.org)

[🌐 **SQLite**](https://www.sqlite.org/index.html)