# CS361 Communication Contract

# How to access my microservice
1. I send will over my Capitals_Microservice.py to you through teams.
2. Put the file into the same folder as your project folder.
3. You will then open up a terminal and cd into your project folder where this file is located.
    3a. You will download a virtual environment by typing 'python -m venv env'
    3b. After that you will activate the virtual environment by typing 'source env/bin/activate'
    3c. You will install the zmq module if you have not by typing 'pip install pyzmq'
    3d. You then type "python Capitals_Microservice.py" or ""python3 Capitals_Microservice.py" depending on the version you have.
4. This will then start running the microservice in the background.
5. You open another terminal and run your project on it. 

# How to request data from my microservice
1. Your project should already have the ZeroMQ module imported into your project. 
2. You will change your localhost to port 5555 which is where my microservice will be receiving messages from.
3. Your project will then make a request using ZeroMQ and once my microservice receives your message it will then send back the csv url for the state capitals.
    3a. This request can be any message as long as your socket sends it over.
    3b. For node.js ZeroMQ the request line should look similar to this "await sock.send('Hello').

# How to receive data from my microservice
1. In your project file you will have something similar to this response 'const [result] = await sock.receive()'
    1a. This will receive the return message from my microservice.
2. My microservice will send back a csv url to your 'await sock.receive'.
3. You can then set a result variable to the response.
4. You then can use a method or module to parse the csv file assigned to the result variable and then you can manipulate the data however you want.

![Screen Shot 2023-02-08 at 2 34 42 PM](https://user-images.githubusercontent.com/81591593/217634481-5721e1b6-41a7-4a74-8721-60d98ceba433.png)
