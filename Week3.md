# Week 3: Dynamic Analysis 
 This week we focused on setting up a dynamic analysis system. This focused on a internal network reaching to a secondary virtual machine that acted as a complete internet connection allowing us to run programs without fear of damage spreading to outside systems. Throughout this week I learned how to use tools such as procmon wireshark to analyse what malware does as it runs. 
## Lab 3-1
  
#### Executive Summary (Most important takeaways for this malware)\
This malware appears to be a launcher that uses a web resource to either update or download more code. It does this by reaching out to praticalmalware analysis.com. We also know that it creates or edits a file in system 32. I could not tell more as it was packed in PENinja. 

#### Indicators of Compromise (What to look for to see if you are infected)
lab3-01.exe: SHA-256 eb84360ca4e33b8bb60df47ab5ce962501ef3420bc7aab90655fd507d2ffcedd 

#### Mitigations (Have you discovered anything that could be used to fix this infection?)
The first mitigation is to take the hash of the file and prevent it from running or being downloaded. The second is to set a firewall rule against the outside resource. 

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)
 First I ran strings then saw that the file was poining to a website as well as some specific files. The lack of imports implied that the file is packed. Running it through virustotal it pinged as malware and that is packed by PENinja. Further research would need to be done to unpack it. From the strings we can tell it reaches out to praticalmalwareanalysis.com.  While wireshark confirms that the malware reaches out I would need more time to figure out why. From strings we can see it acesses a file in system32. 

## Lab 3-2
  
#### Executive Summary (Most important takeaways for this malware)
 This virus appears to be a launcher that creates and deletes services. Then it connects to the internet and downloads a specific resource.

#### Indicators of Compromise (What to look for to see if you are infected)
lab3-02.dll: SHA-256 5eced7367ed63354b4ed5c556e2363514293f614c2c2eb187273381b2ef5f0f9 

#### Mitigations (Have you discovered anything that could be used to fix this infection?)
Set firewall rule to block the domain listed. As well as antivirus to block the file. 

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

First I ran strings. The file appears to call a serve.html as well as praticalmalwareanalysis.com. It also refrences INA and IRIP. I then looked at the file using dependency walker from this we see a bunch of imports centered arround creating and destroying services. I did not figure out how to run the dll. More time would be needed to properly run and analyze. 

## Lab 3-3
  
#### Executive Summary (Most important takeaways for this malware)

Using dynamic analysis I learned that this malware is a keylogger. It creates a orphaned svchost.exe that stores all keylogs into praticalmalwareanalysis.log. 

#### Indicators of Compromise (What to look for to see if you are infected)

lab03-03.exe:SHA-256 ae8a1c7eb64c42ea2a04f97523ebf0844c27029eb040d910048b680f884b9dce 

A orphaned: svchost.exe

praticalmalwareanalysis.log

#### Mitigations (Have you discovered anything that could be used to fix this infection?)

We should set our antivirus software to delete any orphaned svchost.exe processes not in service. As well as delete any files with matching hashes to lab03-03.exe.

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

By following what was shown in the book using procmon. I was able to see that the exe creates and orphans a process svchost.exe. The malware also uses deception by having the image of the process look like a clean process. Conversely in memory we can see it is acting differently in the strings of memory we can see the create file of praticalmalwareanalysis.log. I also saw key strokes such ```[SHIFT]```. This means that most likely our malware is a keylogger.  
