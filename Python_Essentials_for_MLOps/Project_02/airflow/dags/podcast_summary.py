import os
import requests
import xmltodict
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook


PODCAST_URL = "https://www.marketplace.org/feed/podcast/marketplace/"
EPISODE_FOLDER = "/home/matheus/mlops2023/Python_Essentials_for_MLOps/Project_02/airflow/episodes"
FRAME_RATE = 16000

def get_episodes():
    data = requests.get(PODCAST_URL)
    feed = xmltodict.parse(data.text)
    episodes = feed["rss"]["channel"]["item"]

    print(f"Found { len(episodes) } episodes.")

    return episodes

def download_episodes(episodes):
    audio_files = []

    for episode in episodes:
        name_end = episode["link"].split('/')[-1]
        filename = f"{ name_end }.mp3"
        audio_path = os.path.join(EPISODE_FOLDER, filename)

        if not os.path.exists(audio_path):
            print(f"Downloading {filename}")

            audio = requests.get(episode["enclosure"]["@url"])

            with open(audio_path, "wb+") as f:
                f.write(audio.content)

        audio_files.append({
            "link": episode["link"],
            "filename": filename
        })

    return audio_files

def load_episodes(episodes):
    hook = SqliteHook(sqlite_conn_id="podcasts")
    stored_episodes = hook.get_pandas_df("SELECT * from episodes;")
    new_episodes = []

    for episode in episodes:
        if episode["link"] not in stored_episodes["link"].values:
            filename = f"{ episode['link'].split('/')[-1] }.mp3"

            new_episodes.append([
                episode["link"], 
                episode["title"], 
                episode["pubDate"], 
                episode["description"], 
                filename
            ])

    hook.insert_rows(
        table="episodes", 
        rows=new_episodes, 
        target_fields=[
            "link", 
            "title", 
            "published", 
            "description", 
            "filename"
        ]
    )

    return new_episodes


with DAG(dag_id="podcast_summary", schedule_interval="@daily", start_date=pendulum.datetime(2023, 10, 9), catchup=False) as dag:
    task_create_table_sql = SqliteOperator(
        task_id="create_table_sqlite",
        sql=r"""
        CREATE TABLE IF NOT EXISTS episodes (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT,
            transcript TEXT
        );
        """,
        sqlite_conn_id="podcasts"
    )
    task_get_episodes = PythonOperator(
        task_id="get_episodes",
        python_callable=get_episodes
    )
    task_download_episodes = PythonOperator(task_id="download_episodes", python_callable=download_episodes)
    task_load_episodes = PythonOperator(task_id="load_episodes", python_callable=load_episodes)

task_create_table_sql.set_downstream(task_get_episodes)
task_get_episodes.set_downstream([
    task_download_episodes,
    task_load_episodes
])