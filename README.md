# To run the test in BDD
```
behave 
```
Cum vedem toate packetele?
```commandline
pip freeze > requirments.txt
behave --tags=smoke -f html -o raport.html
behave .\features\checboxes.feature (pentru a rula un anumit feature)
```
