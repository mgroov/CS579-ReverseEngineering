# CS479/579 Reverse Engineering at NMSU

This repo will hold a collection of reports on reverse engineering malware samples and what can be learned from them. These samples will come from  "Practical Malware Analysis". by Michael Sikorski and Andrew Honing. For each sample a seperate report will be made describing the process as well as what was learned by reverse engineering that sample. 

### Malware Analysis Setup
####  Isolation
In order to properly isolate the samples I am going to reverse engineer I took multiple steps. The first of which is to dual boot a windows machine with a Linux distribution. To further hardware isolate the samples I installed a Type 2 Hypervisor. For this course I choose VirtualBox both for familarity as well as teacher reccommendation. In this imported a Windows machine that will act as an target machine. In the type 2 Hypervisor I disabled all network connections. This will network isolate the target system such that the malware samples cannot further escape via the network. Furthermore I created a Snapshot of the new virtual machine in order to ensure a clean running enviorment after analysis is finished.

#### Why Isolate?
I isolated the target system so that I can run dangerous malware and analyze their effects. Most importantly by isolating we prevent damage to our hardware as well as dangerous software such as worms from spreading to our entire network. Without proper isolation I can potentially damage and loose a piece of hardware or unintentionally unleash an attack on a network. 

#### Analysis Tool(s)
Visual Studio Code
strings
PEview
dependency walker
PEiD
upx
ghidra 
