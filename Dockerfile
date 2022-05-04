# Do Not Change FROM Use Lavan DockerFile
# LavanProjects
FROM erdembey/epicuserbot:latest
RUN git clone https://github.com/LavanderProjects/LavanUserBot /root/LavanUserBot
WORKDIR /root/LavanUserBot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]  
