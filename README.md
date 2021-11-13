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
![image](https://user-images.githubusercontent.com/19412420/141612589-c630320e-4b75-48cf-81fd-06b3d6d4459d.png)  
An astronaut's name along with other information is placed in `li` and each item is placed in `a`.  

### a
![image](https://user-images.githubusercontent.com/19412420/141612600-19d80cf2-7460-43eb-bcf4-5ce7ef7480df.png)  
If it is an `img`, then it means that it is a national flag, so we drop it and continue to the next `a`.  
And if we found the name in `a`, we not only take the name as an variable, but also get the link, which is stored in `href`, to the personal page.   

### noprint ForAgeToShow
![image](https://user-images.githubusercontent.com/19412420/141612564-a7d5e480-76c1-45be-84c7-5e6adc75ef0c.png)  
We can see the astronaut's age is placed in the class `noprint ForceAgeToShow`, so we use `select_one` to get it. (The class is unique.)  
![image](https://user-images.githubusercontent.com/19412420/141612675-eea4e985-c5ee-42a9-b9bd-d16e8469d68c.png)  
And if an astronaut is dead, the age will not be in the class, so I decided not to take those ages.  

### age.text.split()[1][:-1]
The age will be something like `(age 54)`, I think it is simple enough so I just use `split()` and `[:-1]` to drop the right bracket.  

## data.txt and data_age.txt
The raw result is also stored in a data.txt file, and the sorted result by age is stored in data_age.txt.  
Format: `{name} {age}`

## Reference
[Python 網路爬蟲 Web Crawler 教學 — Beautiful Soup 篇](https://seanchien0525.medium.com/python-requests-beautifulsoup-%E7%88%AC%E8%9F%B2%E6%95%99%E5%AD%B8-83d146faa9e8)  
