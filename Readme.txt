 pip install flask
 pip install flask_restful
 pip install celery
 pip install sqlalchemy   #for backend database



 If using rabbitmq as a broker then first install it:-         #### if using celery then you need broker
    pip install rabbitmq       #if using pycharm then inside pycharm open Terminal and write this command
    sudo service rabbitmq-server start # from terminal
    sudo service rabbitmq-server status #from terminal check status
    sudo service rabbitmq-server stop
    if face any problem in installing then install it manually:- https://www.rabbitmq.com/download.html


 To start flask app:-
            run it manually   or write  in terminal:-
                                           python yourfilename.py
                                           ### example for this project:-
                                                                    python main.py

 To start worker run command:-
            celery -A yourfilename.celery worker --loglevel=info
            ### example for this project:-
                                celery -A application.celery worker --loglevel=info
            ### yourfilename = name of that file in which your celery app is running




broker='amqp://guest:@localhost:5672//'   ### for rabbitmq
backend='db+sqlite:///db.sqlite3'         ### Sqlite database as backend
backend='rpc://'                          ### rabbitmq as backend
backend='amqp'

If you face error like:-
           1)  if you star celery worker and face this error
                    Error:
                    Unable to load celery application.
                    'flask' object has no attribute 'user_options'

              Then check your file name, backend url, and most import check you written command like this in your app or not:- celery = make_celery(app)



