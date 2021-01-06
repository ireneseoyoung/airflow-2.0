# create connection fs_default with {"path":"/usr/local/airflow/"}
# sensor.py

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.sensors.filesystem import FileSensor
from airflow.hooks.filesystem import FSHook
from airflow.operators.python_operator import PythonOperator

import logging
import json

default_args = {
    'start_date': days_ago(1),
}

FILENAME = 'bitcoin.json'


def _processing():
    path = FSHook(fs_conn_id='fs_default').get_path()
    logging.info(f'{path}/{FILENAME}')


def _storing():
    logging.info('storing data')


with DAG('sensor', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    sensors = [
        FileSensor(
            task_id=f'waiting_for_file_{sensor_id}',
            filepath=FILENAME,
            fs_conn_id='fs_default'
        ) for sensor_id in range(1, 10)
    ]

    processing = PythonOperator(
        task_id='processing',
        python_callable=_processing
    )

    storing = PythonOperator(
        task_id='storing',
        python_callable=_storing
    )

    sensors >> processing >> storing
