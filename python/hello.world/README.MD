# run



to install docker rabbit 
# latest RabbitMQ 4.x
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management

#create first a venv
check if venv exist
```python -m venv --help
if not exist run code
```sudo apt-get install python3-venv
create venv
```python -m venv venv

#so to run the environment in windows run 
```venv\Scripts\activate.bat

#install pika
python -m pip install pika --

#first example
using receive.py and send.py

#second example work queues
using new_task.py and worker.py

