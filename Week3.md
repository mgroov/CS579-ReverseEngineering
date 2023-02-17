# Week 3: Dynamic Analysis 
 This week we focused on setting up a dynamic analysis system. This focused on a internal network reaching to a secondary virtual machine that acted as a complete internet connection allowing us to run programs without fear of damage spreading to outside systems. 
## Lab 3-1
  
#### Executive Summary (Most important takeaways for this malware)\
This malware appears to be a launcher that uses a web resource to either update or download more code. It does this by reaching out to praticalmalware analysis.com. We also know that it creates or edits a file in system 32. I could not tell more as it was packed in PENinja. 

#### Indicators of Compromise (What to look for to see if you are infected)
lab3-01.exe: 

#### Mitigations (Have you discovered anything that could be used to fix this infection?)
The first mitigation is to take the hash of the file and prevent it from running or being downloaded. The second is to set a firewall rule against the outside resource. 

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)
 First I ran strings then saw that the file was poining to a website as well as some specific files. The lack of imports implied that the file is packed. Running it through virustotal it pinged as malware and that is packed by PENinja. Further research would need to be done to unpack it. From the strings we can tell it reaches out to praticalmalwareanalysis.com.  While wireshark confirms that the malware reaches out I would need more time to figure out why. From strings we can see it acesses a file in system32. 

## Lab 3-2
  
#### Executive Summary (Most important takeaways for this malware)

#### Indicators of Compromise (What to look for to see if you are infected)

#### Mitigations (Have you discovered anything that could be used to fix this infection?)

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)

## Lab 3-3
  
#### Executive Summary (Most important takeaways for this malware)

#### Indicators of Compromise (What to look for to see if you are infected)

#### Mitigations (Have you discovered anything that could be used to fix this infection?)

#### Evidence (How did you find each of the above? You can mention here any work you did that did not yield any results.)
