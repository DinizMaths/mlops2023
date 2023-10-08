import sys
sys.dont_write_bytecode = True

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

import pendulum
import requests
import xmltodict


def get_episodes():
    data = requests.get("https://www.marketplace.org/feed/podcast/marketplace/")
    feed = xmltodict.parse(data.text)
    episodes = feed["rss"]["channel"]["item"]

    print(f"Found {len(episodes)} episodes.")

    return episodes

# def load_episodes(episodes):
#     load_episodes = SqliteHook(sqlite_conn_id="podcasts")
#     stored_episodes = load_episodes.get_pandas_df("SELECT * from episodes;")

#     new_episodes = []

#     for episode in episodes:
#         if episode["link"] not in stored_episodes["link"].values:
#             filename = f"{ episode['link'].split('/')[-1] }.mp3"

#             new_episodes.append([
#                 episode["link"],
#                 episode["title"],
#                 episode["pubDate"],
#                 episode["descriptio"],
#                 filename
#             ])

#     load_episodes.insert_rows(
#         table="episodes", 
#         rows=new_episodes, 
#         target_fields=[
#             "link", 
#             "title", 
#             "published", 
#             "description",
#             "filename"
#         ]
#     )

with DAG(dag_id="podcast_summary", schedule="@daily", start_date=pendulum.datetime(2023, 8, 10), catchup=False) as dag:
    create_database = SqliteOperator(task_id="create_database", sql=r"""
        CREATE TABLE IF NOT EXISTS episodes (
            link TEXT PRIMARY KEY,
            title TEXT,
            filename TEXT,
            published TEXT,
            description TEXT
        )
        """,
        sqlite_conn_id="podcasts"
    )
    podcast_episodes = PythonOperator(task_id="podcast_episodes", python_callable=get_episodes)
    # load_episodes(podcast_episodes)


create_database.set_downstream(podcast_episodes)