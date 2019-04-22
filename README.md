## Project 1: Project: Logs Analysis
The user-facing newspaper site frontend itself, and the database - `news` - behind it, are already built and running. This _python_ code is an **internal reporting tool** that will use information from the database to discover what kind of articles the site's readers like.
### Documentation
This project uses a PostgreSQL database which is named as `news`.
The news database contains newspaper `articles` and `authors` tables, as well as the web server `log` table for the site. The `log` has a database row for each time a reader loaded a web page.

The program runs from the command line. It takes input from the user and connects the news database, use SQL queries to analyze the log data, and provides answers to select questions.
### Set up
To start the program, you'll need database software (provided by a Linux virtual machine) and the data to analyze.
#### Use a terminal
You'll be using a Unix-style terminal on your computer. If you are using a Mac or Linux system, your regular terminal program will do just fine. On Windows, we recommend using the Git Bash terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com.](https://git-scm.com/downloads)
For a refresher on using the Unix shell, look back at our [Shell Workshop](https://www.udacity.com/course/shell-workshop--ud206).
If you'd like to learn more about Git, take a look at [our course about Git](https://www.udacity.com/course/version-control-with-git--ud123).

#### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.
**Ubuntu users**: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

#### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.
Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
_If Vagrant is successfully installed, you will be able to run `vagrant --version` in your terminal to see the version number._

#### Download the VM configuration
There are a couple of different ways you can download the VM configuration.
You can download and unzip this file: [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called **FSND-Virtual-Machine**. It may be located inside your **Downloads** folder.  
**Note**: If you are using Windows OS you will find a Time Out error, to fix it use the new [Vagrant file configuration](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip) to replace you current Vagrant file.
Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.
Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with `cd`. Inside, you will find another directory called **vagrant**. Change directory to the **vagrant** directory:  

_$ cd Downloads/FSND-Virtual-Machine  
$ cd vagrant/_
#### Start the virtual machine
From your terminal, inside the **vagrant** subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!
#### Logged in!
If you are now looking at a shell prompt that starts with the word `vagrant` (as in the above screenshot), congratulations — you've gotten logged into your Linux VM. If not, take a look at the **Troubleshooting** section below.

#### The files for this project
Inside the VM, change directory to `/vagrant` and look around with `ls`.
The files you see here are the same as the ones in the `vagrant` subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM. Files in the VM's `/vagrant` directory are shared with the `vagrant` folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.
#### Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use the `psql` command-line tool to access it and run SQL statements.
#### Logging out and in
If you type `exit` (or `Ctrl-D`) at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type `vagrant ssh` again. If you reboot your computer, you will need to run `vagrant` up to restart the VM.
________________________________________
### Troubleshooting
**I'm not sure if it worked**.  
If you can type `vagrant ssh` and log into your VM, then it worked! It's normal for the `vagrant up` process to display a lot of text in many colors, including sometimes scary-looking messages in red, green, and purple. If you get your shell prompt back at the end, and you can log in, it should be OK.

`vagrant up` **is taking a long time. Why?**  
Because it's downloading a whole Linux operating system from the Internet.

**I'm on Windows, and when I run `vagrant ssh`, I don't get a shell prompt**.  
Some versions of Windows and Vagrant have a problem communicating the right settings for the terminal. There is a workaround: Instead of `vagrant ssh`, run the command `winpty` `vagrant ssh` instead.

**I'm on Windows and getting an error about virtualization**.  
Sometimes other virtualization programs such as Docker or Hyper-V can interfere with VirtualBox. Try shutting these other programs down first.

In addition, some Windows PCs have settings in the BIOS or UEFI (firmware) or in the operating system that disable the use of virtualization. To change this, you may need to reboot your computer and access the firmware settings. A [web search](https://www.google.com/search?q=enable%20virtualization%20windows%2010) can help you find the settings for your computer and operating system. Unfortunately there are so many different versions of Windows and PCs that we can't offer a simple guide to doing this.

**Why are we using a VM? It seems complicated**.  
It is complicated. In this case, the point of it is to be able to offer the same software (Linux and PostgreSQL) regardless of what kind of computer you're running on.

**I got some other error message**.  
If you're getting a specific textual error message, try looking it up on your favorite search engine. If that doesn't help, take a screenshot and post it to the discussion forums, along with as much detail as you can provide about the process you went through to get there.

**If all else fails, try an older version**.  
Udacity mentors have noticed that some newer versions of Vagrant don't work on all operating systems. Version 1.9.2 is reported to be stabler on some systems, and version 1.9.1 is the supported version on Ubuntu 17.04. You can download older versions of Vagrant from [the Vagrant releases index](https://releases.hashicorp.com/vagrant/).

### Download the data
Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database.

To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:

* `psql` — the PostgreSQL command line program  
* `-d news` — connect to the database named news which has been set up for you  
* `-f newsdata.sql` — run the SQL statements in the file newsdata.sql  

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### Getting an error?
If this command gives an error message, such as —  
`psql: FATAL: database "news" does not exist`  
`psql: could not connect to server: Connection refused`  
— this means the database server is not running or is not set up correctly. This can happen if you have an _older version_ of the VM configuration from before this project was added. To continue, download the virtual machine configuration into a fresh new directory and start it from there.
### Explore the data
Once you have the data loaded into your database, connect to your database using `psql -d` news and explore the tables using the `\dt` and `\d table` commands and `select` statements.

* `\dt` — display tables — lists the tables that are available in the database.  
* `\d table` — (replace table with the name of a table) — shows the database schema for that particular table.  

Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

* The `authors` table includes information about the authors of articles.
* The `articles` table includes the articles themselves.
* The `log` table includes one entry for each time a user has accessed the site.

As you explore the data, you may find it useful to take notes! Don't try to memorize all the columns. Instead, write down a description of the column names and what kind of values are found in those columns.

### Run newsdata.py
The program was written in **python2**. Use the command **python2 newsdata.py** to run the program.
### SQL Documentation
The program uses _two_ **VIEW** tables created by the _sql_ codes below. First, they have to be created in order to be able to run the program.

**splitpath** table:

CREATE VIEW splitpath AS  
SELECT articles.author, articles.title, new.splitpath  
FROM articles, (select split_part(path, '/', 3) AS splitpath  
FROM log) AS new  
WHERE articles.slug = new.splitpath;

**connection** table:

CREATE VIEW connection AS  
SELECT newall.alldate, newall.allcon, newfail.failcon  
FROM (SELECT cast(time as date) AS alldate, count(\*) AS allcon  
FROM log GROUP BY alldate) AS newall,  
(SELECT cast(time as date) AS faildate, count(\*) AS failcon  
FROM log WHERE status = '404 NOT FOUND' GROUP BY faildate) AS newfail  
WHERE newall.alldate = newfail.faildate;


### LICENCE
https://choosealicense.com/
