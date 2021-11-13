Being an astronauts has been my dream since I was a kid.  
The beautiful night sky always attracts me.  
But now I am old, useless, and afraid of not being able to become an astronaut, so I decided to take a look at those astronauts' ages to build some confidence.  

## crawler.py

The main function.  
I look at the [wikipedia page that has all the astronauts](https://en.wikipedia.org/wiki/List_of_astronauts_by_name), wondering how I can reach each astronaut's page and get their ages.  
So the first thing is their names.  

### mw-parser-output
![image](https://user-images.githubusercontent.com/19412420/141602049-53189078-44c3-41e6-997c-d2c4e8f7c5d6.png)  
The class name `mw-parser-output` is unique enough IMO so I take it as the starting point.

### ul 
The element `ul` does not represents sections of each character except **A**, which has two `ul`. I don't know why either.  

### li
An astronaut's name along with other information lays
