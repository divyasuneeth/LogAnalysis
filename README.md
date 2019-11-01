# LogAnalysis

This project will run from the command line. It is a reporting tool. It doesn't take any input from the user. Instead, it will connect to that database, analyzes the log data, and prints out the answers to some questions.

# Quickstart


## To install vargrant :
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from vagrantup.com. Install the version for your operating system.

If Vagrant is successfully installed, you will be able to run vagrant --version
in your terminal to see the version number.

## working on vagrant
run `vargrant up`
followed by `vargrant ssh`
to login into the newly installed virtual machine.

** Change Directory to vagrant **
run `cd /vagrant`


## Downlaod database
The database used is called newsdata and can be downloaded here.
download newsdata.sql (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
copy database into the vagrant directory on your system.

## TO LOAD DATA:
cd into the vagrant directory and use the command
psql -d news -f newsdata.sql
Here's what this command does:

psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql

## Explore the data
Once you have the data loaded into your database, connect to your database using `psql -d news` and explore the tables using the `\dt` and `\d` table commands and select statements.

* \dt — display tables — lists the tables that are available in the database.
* \d table — (replace table with the name of a table) — shows the database schema for that particular table.
Get a sense for what sort of information is in each column of these tables.

The database includes three tables:

* The ** authors ** table includes information about the authors of articles.
* The ** articles ** table includes the articles themselves.
* The ** log ** table includes one entry for each time a user has accessed the site.


## Download LogAnalysis directory into vagrant directory.
To run the python file LogAnalysisdb.py

from commandline promp:
`cd /vagrant/LogAnalysis` directory
run command :`python LogAnalysisdb.py` to view the output.
