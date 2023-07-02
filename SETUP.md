# Hadoop with Docker

## Preliminaries
### Docker
You need docker installed on your laptop. \
The installation process is different for each system:
- Linux: `sudo apt install docker`
- Windows: [Link](https://docs.docker.com/desktop/install/windows-install/)
- Mac: [Link](https://docs.docker.com/desktop/install/mac-install/)

You can check whether Docker is correctly installed by opening a terminal and trying to execute 
```
docker version
```

It should display a line like this:
```
albert@albert-Thinkpad-t440p:~$ docker version
Client:
 Version:           20.10.21
 API version:       1.41
 Go version:        go1.18.1
 Git commit:        20.10.21-0ubuntu1~22.04.3
[...]
```

### Docker-Compose
Docker-compose is an extension to Docker that allows for easy starting and controlling of Docker containers. \
On Windows and Mac Systems it typically comes bundled with Docker Desktop. \
However, on Linux Systems, you need to install is separately on your laptop. \
The installation process on Linux Systems is as follows:
- Linux: `sudo apt install docker-compose`

You can check wether docker-compose is correctly installed by opening a terminal and trying to execute 
```
docker-compose version  
```

It should display a line like this:
```
albert@albert-Thinkpad-t440p:~$ docker-compose version  
docker-compose version 1.29.2, build unknown
docker-py version: 5.0.3
CPython version: 3.10.6
OpenSSL version: OpenSSL 3.0.2 15 Mar 2022
```

## Starting the Docker Image
1. Download the hadoop_docker_nlp.zip file and extract it
2. Open a terminal on your laptop (You can use the terminal inside PyCharm or VSCode)
3. Navigate to the `hadoop_docker_nlp` folder
4. Execute `docker-compose up --build`
   - The first time you do this will probably take a few minutes
   - If successful, the terminal will display 
   ```
   Creating hadoop_docker_nlp_hadoop_1 ... done
   Attaching to hadoop_docker_nlp_hadoop_1
   ```
5. Make sure that the container stays running
   - You don't see a line like `hadoop_docker_nlp_hadoop_1 exited with code 0`
   - You see the container when executing `docker ps`
   ```
   albert@albert-Thinkpad-t440p:~/PersonalProjects/MapReduce/NLP$ docker ps
    CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS          PORTS     NAMES
    8383cb765f57   hadoop_docker_nlp_hadoop   "/usr/local/bin/dumb…"   48 seconds ago   Up 47 seconds             hadoop_docker_nlp_hadoop_1
   ```

## Connecting to the Docker Image
1. Open a **second** terminal (PyCharm and VSCode allow you to open multiple terminals as well)
2. Find the container_id of your docker image via `docker ps` (See above)
3. Connect to the container via `docker exec -it <container_id> bash`
   - You should see output like this
   ```
   albert@albert-Thinkpad-t440p:~/PersonalProjects/MapReduce/NLP$ docker exec -it 8383cb765f57 bash
   [root@8383cb765f57 hadoop]#
   ```
4. You can now execute commands within the running docker container
5. Navigate to the code directory via `cd code`
6. Check if all files are synchronized via `ls`
   - You should see at least
   ```
   [root@8383cb765f57 hadoop]# cd code
   [root@8383cb765f57 code]# ls
   README.md  inpt.txt  mapper.py  reducer.py  run.sh
   ```

## Writing the Hadoop program
- Without modifications the docker container can only host one docker program at a time.
So you are required to copy & paste this folder for each MapReduce job and repeat the previous steps for each folder
- You are required to use the provided `mapper.py` and `reducer.py` to write your program
- Execute your program in the **second** terminal that you prepared in the previous section
  - From the `code` directory execute `sh run.sh`
  - You will see lots of output
  - The script should conclude with the output of your hadoop program
  ```
  [root@8383cb765f57 code]# sh run.sh 
  [...]
  2023-04-28 13:17:06 INFO  StreamJob:1029 - Output directory: out
  20      1
  house   2
  is      1
  no      1
  number  1
  [root@8383cb765f57 code]# 
  ```
  - You can always re-visit the log of your last run locally on your laptop
    - Open `part-00000` in the `out` folder as a text file
