File named 'requirements.txt'consists of all the dependencies.

signup by api parameters user_id and password.
http://127.0.0.1:8000/signup/?user_id={}&pas={}

login by sending parameters user_id and password.
http://127.0.0.1:8000/login/?user_id={}&pas={}
in response you will get random number only 5 times in a minute,
afterthat thread will wait for one minute to complete.
(After 5 attempts no response will be generated for existing user, sleep mode for one minute.)


Bash script is made to install all dependencies and run server locally.
