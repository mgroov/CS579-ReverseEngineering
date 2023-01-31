## Week 1 Simple Static Analysis
  summary here

### Lab 1-1
  
##### Executive Summary (Most important takeaways for this malware)
This malware sample is of two programs working in concert. It has a lab1.dll file which seems to launch and run programs on threads. And a lab01 exe that  seems to edit files. 
##### Indicators of Compromise (What to look for to see if you are infected)
 Compilation Dates: 
 lab01-01.dll 12/19/10 \
 lab01-01.exe 1/8/12 
 
 Hashes: \
  .d11: SHA256 Hash      : F50E42C8DFAAB649BDE0398867E930B86C2A599E8DB83B8260393082268F2DBA \
  .exe: SHA256 Hash      : 58898BD42C5BD3BF9B1389F0EEE5B39CD59180E8370EB9EA838A0B327BD6FE47
  

##### Mitigations (Have you discovered anything that could be used to fix this infection?)

Delete files with the same hashes.

##### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

I used strngs to look at the ascii of the files. In dll you can see the creation of threads and mutex. In the exe you can see it acessing files as well as a string saying this program will destroy your computer. In order to see the hashes of the files I used powershells built in function. I also used both peview and dependency checker and was unable to determine more useful information. 


### Lab 1-2

##### Executive Summary (Most important takeaways for this malware)

##### Indicators of Compromise (What to look for to see if you are infected)

##### Mitigations (Have you discovered anything that could be used to fix this infection

##### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)


### Lab 1-3

##### Executive Summary (Most important takeaways for this malware)

##### Indicators of Compromise (What to look for to see if you are infected)

##### Mitigations (Have you discovered anything that could be used to fix this infection

##### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)


### Lab 1-4


##### Executive Summary (Most important takeaways for this malware)

##### Indicators of Compromise (What to look for to see if you are infected)

##### Mitigations (Have you discovered anything that could be used to fix this infection

##### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)
