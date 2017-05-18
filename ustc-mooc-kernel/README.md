== 2014年春Linux操作系统分析 Topics in Linux Operating Systems,Spring 2014 ==

* Instructors: Mengning（孟宁） and Chunjie Li（李春杰）, Homeworks Checking by Mengning
* Time: 8:00 - 10:25 every Monday and Thursday,from 17 feb. to 10 april.
* Location: Room 239 of Mingde Building(明德楼)
* Homeworks time and location: Tuesday night 19:00 - 21:30 in week 4、5、7、8、9（standby）, Room 318 of Sixian Building (思贤楼)
* Discussions: through [/ticket/487 Teamtrac Ticket] & QQ群229570921
* Examination time and location：2014年4月17日 8:30-10:30,Room 116 of Mingde Building(明德楼)


=== [/raw-attachment/wiki/Linux2013/IntroductionofLinuxSystem.pdf Introduction of Linux System] ===
=== [/raw-attachment/wiki/Linux2013/HowtheComputerWorks.pdf How the Computer Works] ===

Without understanding the basic concepts of Computer, you really can not understand how Operating system works on Computer.

* The stored program computer
* X86 implementation
* The function call stack
* Interrupt and Interrupt Service Routine (ISR)
* [/raw-attachment/wiki/Linux2013/FoundationsForHackingLinux.ppt Foundations For Hacking Linux] - [http://staff.ustc.edu.cn/~xlanchen/ULK2011Spring/slides/1_2_tools.pdf GNUTools]
* Homework 1: [https://github.com/mengning/mykernel mykernel] - It is a platform to write your own OS kernel,its based on Linux Kernel 3.9.4 source code.
  * [http://gcc.gnu.org/ml/gcc-help/2004-03/msg00291.html '$1f' is the next label called '1' in forward direction. See your assembler manual.]
  * [http://stackoverflow.com/questions/14922022/need-to-figure-out-the-meaning-of-following-inline-assembly-code $1f is the address of the 1 label. The f specifies to look for the first label named 1 in the forward direction.]

=== The evolution of operating systems. ===

Without understanding the concepts and theory of Operating system, you really can not understand why Linux kernel is coded in that way.

* [http://brinch-hansen.net/ Per Brinch Hansen] "[http://www.valleytalk.org/wp-content/uploads/2014/01/2001b.pdf The evolution of operating systems.]" In Classic operating systems, pp. 1-34. Springer New York, 2001.
* Homework 2: translated into Chinese, [/wiki/OSEvolution 操作系统进化简史]

=== Understanding the Linux Kernel ===

* [/raw-attachment/wiki/Linux2013/LinuxArchitectureAndSystemExecution.ppt Linux Architecture And System Execution]
* [/raw-attachment/wiki/Linux2012/IntroductionofLinuxKernelSourceCode.pdf Introduction of Linux Kernel Source Code]
* [/raw-attachment/wiki/Linux2012/SystemCall.ppt System Call]
* [/raw-attachment/wiki/Linux2012/ProgramAndProcess.ppt Program And Process]
* Understanding the Linux kernel process management, interrupts, memory management, file systems, device drivers, network architecture, etc. (working with Chunjie Li)
 * [/raw-attachment/wiki/Linux2014/2014%E5%B9%B4linux%E7%A8%8B%E5%BA%8F%E5%88%86%E6%9E%90%E4%B8%BB%E8%A6%81%E7%9F%A5%E8%AF%86%E7%82%B9%E6%80%BB%E7%BB%93byli.doc Summary by Chunjie Li]
 * interrupt processing
  * interrupt(ex:int 0x80) - save cs:eip/esp/eflags(current) to kernel stack,then load cs:eip(entry of a specific ISR) and ss:esp(point to kernel stack). 
  * SAVE_ALL
  * ...
  * RESTORE_ALL
  * iret - pop cs:eip/ss:esp/eflags from kernel stack
* [/raw-attachment/wiki/Linux2013/ProcessSwitching.pdf Process Switching]
* [/raw-attachment/wiki/Linux2013/ProcessScheduling.ppt ProcessScheduling.ppt]
* [/raw-attachment/wiki/Linux2013/LinuxNetworking.pdf LinuxNetworking.pdf]
* Homework 3: add new mac80211/cfg80211 modules as option for Linux Kernel
  * Step 1：[http://teampal.mc2lab.com/projects/fwn/wiki/SetupHostapd Setup WiFi AP]
  * Step 2：[/wiki/UpgradeLinuxKernel Upgrade Linux Kernel from source code] and make sure Step 1 works well
  * Step 3: [/wiki/AddNewModule add new mac80211/cfg80211 module]  and make sure Step 1 works well again, lsmod can find mac80211ext/cfg80211ext module
  * Step 4(Optional): [/raw-attachment/wiki/Linux2013/Linux%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C%E7%B3%BB%E7%BB%9F%E5%88%86%E6%9E%90.ppt Understanding 802.11 Subsystem as WiFi AP/Router] -  draw the outline of initializing flow,normal working flow etc. of [/wiki/mac80211 mac80211]

=== Linux System Architecture ===

* 可执行程序与进程的实现
  * [/raw-attachment/wiki/Linux2012/ProgramAndProcess.ppt 可执行程序与进程的实现]
    * 进程描述符include/linux/sched.h定义[wiki:task_struct struct task_struct]
  * [/raw-attachment/wiki/Linux2012/ProcessCreationExit.ppt 进程创建和撤销过程]
    * [/raw-attachment/wiki/Linux2012/LINUX%E4%B8%AD%E7%9A%84%E8%BF%9B%E7%A8%8B.pdf Linux的进程详解]
    * [/raw-attachment/wiki/Linux2012/Linux-init-process-analyse.pdf init进程详解]
  * [/raw-attachment/wiki/Linux2012/ELF.ppt ELF文件格式与程序的装载]
    * [http://www.muppetlabs.com/~breadbox/software/ELF.txt ELF文件格式] - [http://www.xfocus.net/articles/200105/174.html 翻译版] 
    * 编译运行[wiki:SharedLibDynamicLink 共享库和动态链接相关范例代码]
    * start_thread(regs, elf_entry, bprm->p);实际上它修改了内核堆栈中存储的返回到用户态时适用的的EIP等信息。
* [/raw-attachment/wiki/Linux2013/Inter-ProcessCommunication.ppt Inter-ProcessCommunication.ppt]
* take OpenWRT as an example to figure out Linux System Architecture
  * [/wiki/StartOpenWRTonWR720N Run OpenWRT on TP-Link WR720N]
  * [http://wenku.baidu.com/view/a8bbe60516fc700abb68fc8c.html Run OpenWRT on VMware]
  * [http://teampal.mc2lab.com/issues/739 more about Run OpenWRT]
  * [/wiki/OpenWRTSystemArchitecture OpenWRT System Architecture]
* Homework 4: add [/raw-attachment/wiki/Linux2014/agentapd.tar.gz Agentapd] as option for OpenWRT


=== References ===

* [wiki:"Linux2013" 2013年春Linux操作系统分析]
* [http://brinch-hansen.net/ Per Brinch Hansen] "[http://www.valleytalk.org/wp-content/uploads/2014/01/2001b.pdf The evolution of operating systems.]" In Classic operating systems, pp. 1-34. Springer New York, 2001.
* https://www.kernel.org/
* [http://geek.csdn.net/news/detail/7711 Linux创始人Torvolds荣获2014年IEEE计算机先驱奖]
* [http://bellard.org/jslinux/ Bellard用JavaScript写了一个PC虚拟机Jslinux]。这个虚拟机仿真了一个32位的x86兼容处理器，一个8259可编程中断控制器，一个8254可编程中断计时器，和一个16450 UART。 
