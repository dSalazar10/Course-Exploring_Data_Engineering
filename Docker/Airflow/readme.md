# How to test a DAG from the airflow cli

## This will give you a shell in the docker container

`docker exec -it $(docker container ls -q) bash`

## This will list all of the DAGs: 

`airflow list_dags`

## This will list the task_id associated with the dag name from above ($DAG=lesson1.solution1):

`airflow list_tasks $DAG`

## This will execute the DAG ($DAG=lesson1.solution1, $TASK=hello_world_task)

`airflow test $DAG $TASK $(date +%F)`


## Example Results:
[2020-06-20 05:07:10,604] {{__init__.py:51}} INFO - Using executor SequentialExecutor
[2020-06-20 05:07:10,604] {{dagbag.py:403}} INFO - Filling up the DagBag from /usr/local/airflow/dags
[2020-06-20 05:07:10,725] {{taskinstance.py:655}} INFO - Dependencies all met for <TaskInstance: lesson1.solution1.hello_world_task 2020-06-20T00:00:00+00:00 [None]>
[2020-06-20 05:07:10,736] {{taskinstance.py:655}} INFO - Dependencies all met for <TaskInstance: lesson1.solution1.hello_world_task 2020-06-20T00:00:00+00:00 [None]>
[2020-06-20 05:07:10,737] {{taskinstance.py:866}} INFO - 
--------------------------------------------------------------------------------
[2020-06-20 05:07:10,738] {{taskinstance.py:867}} INFO - Starting attempt 1 of 1
[2020-06-20 05:07:10,738] {{taskinstance.py:868}} INFO - 
--------------------------------------------------------------------------------
[2020-06-20 05:07:10,741] {{taskinstance.py:887}} INFO - Executing <Task(PythonOperator): hello_world_task> on 2020-06-20T00:00:00+00:00
[2020-06-20 05:07:10,755] {{helloworld.py:9}} INFO - Hello World!
[2020-06-20 05:07:10,755] {{python_operator.py:114}} INFO - Done. Returned value was: None
[2020-06-20 05:07:10,762] {{taskinstance.py:1048}} INFO - Marking task as SUCCESS.dag_id=lesson1.solution1, task_id=hello_world_task, execution_date=20200620T000000, start_date=20200620T050710, end_date=20200620T050710