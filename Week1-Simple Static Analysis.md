# Week 1 Simple Static Analysis
  This week focused on the static analysis of various pieces of malware. By using tools such as strings,    PEview, dependency walker, PEiD, and upx. Some of the main takeaways included how to determine when a file is packed using tools like PEiD. As well as how to use system calls revealed by those tools to determine the nature of the malware. Finally, how to use static analysis to devise actionable countermeasures to viruses. 

## Lab 1-1
  
#### Executive Summary (Most important takeaways for this malware)
This malware sample is of two programs working in concert. It has a lab1.dll file which seems to launch and run programs on threads. And a lab01 exe that  seems to edit files. This malware is for a Windows sytem but a system that is runnin windows defender will most likely catch the program.
#### Indicators of Compromise (What to look for to see if you are infected)
 Compilation Dates: 
 lab01-01.dll 12/19/10 \
 lab01-01.exe 1/8/12 
 
 Hashes: \
  .d11: SHA256 Hash      : F50E42C8DFAAB649BDE0398867E930B86C2A599E8DB83B8260393082268F2DBA \
  .exe: SHA256 Hash      : 58898BD42C5BD3BF9B1389F0EEE5B39CD59180E8370EB9EA838A0B327BD6FE47
  

#### Mitigations (Have you discovered anything that could be used to fix this infection?)

Delete files with the same hashes.

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

I used strngs to look at the ascii of the files. In dll you can see the creation of threads and mutex. In the exe you can see it acessing files as well as a string saying this program will destroy your computer. In order to see the hashes of the files I used powershells built in function. I also used both peview and dependency checker and was unable to determine more useful information. 

## Lab 1-2

#### Executive Summary (Most important takeaways for this malware)

This lab consisted of a singlur executable that was packed in the upx format. Once unpacked it does multiple things.

1) Creates threads and reads and messes with files 
2) Opens a service control manager
3) opens a url to http://www.malwareanalysisbook.com via Internet Explorer

This is dangerous because it will launch again every time you restart your computer via the scmanager.

#### Indicators of Compromise (What to look for to see if you are infected)

compiation date: 1/19/2011 

lab01-02.exe \
SHA256 Hash: C876A332D7DD8DA331CB8EEE7AB7BF32752834D4B2B54EAA362674A2A48F64A6

unwaranted connection to http://www.malwareanalysisbook.com

#### Mitigations (Have you discovered anything that could be used to fix this infection

blocking/firewalling acess to the website http://www.malwareanalysisbook.com

Deleting any files matching that hash 


#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)
While using strings I noticed the executable pointing to http://www.malwareanalysisbook.com. It also uses internet explorer. The string also reveals that the program creates a file and processes in memory. In strings I uwe also see it launching a ```StartServiceCtrlDispatcherA
 OpenSCManagerA```. This is a runtime service control. presuming the malware will relaunch each time you run your computer. I also used both dependency walker and peveiew as well but did not gain any more relevent information.

## Lab 1-3

#### Executive Summary (Most important takeaways for this malware)

This virus consists of a single executable lab1-03.exe. It appears to access the data segments in memory and import libraries. The file is packed in a FSG 1.0 format. Therefore,  I would need more time and research to be able to further determine the full extent of this virus. 


#### Indicators of Compromise (What to look for to see if you are infected)

lab01-03.exe:
SHA256      	7983A582939924C70E3DA2DA80FD3352EBC90DE7B8C4C427D484FF4F050F0AEC

Compilation date: 3/26/2011


#### Mitigations (Have you discovered anything that could be used to fix this infection

Set a filter to delete any files matching the above listed hash.

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

Running strings on the file did not reveal much. It accesses the ```@.data``` and ``` `.rdata ```  loads the kernel32.dll and a library. As well as get the address of a process. Due to the limited amount of information available I attempted to run upx depacking on the file. The packer software returned that the packed type was not upx hinting that the file was packed but not in upx format. I also looked at the file through dependency walker and PEview and was unable to determine more about the file. Using PEid reveals that the file is packaged in FSG 1.0. I was unable to analyse further. 


## Lab 1-4


#### Executive Summary (Most important takeaways for this malware)

This virus consisted of a single executable ```lab01-04.exe```. It appears to act as a launcher for a web downloaded resource. The virus modifies file permissions. Then creates and places a file called ``` \system32\wupdmgrd.exe ``` in the target machine's directory. It then reaches out to a web resource to download a file presumably to both get updates and launch the attack. It is recommended to block the specific file creation and set firewall rules against the web resource. More time would be needed to determine what occurs after download and launch.

#### Indicators of Compromise (What to look for to see if you are infected)
lab01-04.exe: 
SHA256      	0FA1498340FCA6C562CFA389AD3E93395F44C72FD128D7BA08579A69AAF3B126

Compilation Date: 7/5/2011

``` \system32\wupdmgrd.exe ```

access to: 

```http://www.practicalmalwareanalysis.com/updater.exe ```  



#### Mitigations (Have you discovered anything that could be used to fix this infection

Filter for the hash of the executable as shown below. 
Create a firewall rule to block the web resource. 
Look for and bock the creation of the system 32 file listed in evidence. 


#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

First I ran strings the large amount of readable data suggested that this file is unpacked. In strings we can see that the virus creates a thread then runs a program using win exec. It then writes, creates, and moves a file into presumably ``` \system32\wupdmgrd.exe ``` . We can also see in strings the code attempting to modify the process token and debug privileges. Finally, in string we see a command called to download a from url ``` http://www.practicalmalwareanalysis.com/updater.exe ```  

