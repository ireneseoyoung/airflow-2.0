from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.subdag_operator import SubDagOperator
from airflow.executors.sequential_executor import SequentialExecutor
from airflow.utils.dates import days_ago

from subdag_factory import subdag_factory

default_args = {
    'start_date': days_ago(1)
}

with DAG('subdag', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:

    extracting = DummyOperator(task_id='extracting')

    processing = SubDagOperator(
        task_id='processing_subdag',
        subdag=subdag_factory('subdag', 'processing_subdag', default_args)
    )

    loading = DummyOperator(task_id='loading')

    extracting >> processing >> loading