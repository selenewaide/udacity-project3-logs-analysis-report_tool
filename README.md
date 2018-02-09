# Logs Analysis Reporting Tool 

This is a reporting tool for a newspaper site where the frontend itself, and the database behind it, are already built and running. This internal reporting tool will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activity.

The scripts in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

## Table of Contents
1. Getting Started
2. Issues
3. Author
4. Acknowledgments
 

## 1. Getting Started

These instructions will get you a copy of the code. 

### Prerequisites

* Python 3 - to run the scripts that query the database and generate reports
* PostgreSQL database and support software
* newsdata.sql file to populate the database - NOT provided here.

Note: This is a Udacity project for which the PostgreSQL database and support software were already provided on a virtual machine. This repo only contains the Python code for the  project.

### Install & Run

###### Step 1
Clone the project from [Github Logs Analysis Reporting Tool](https://github.com/selenewaide/udacity-project3-logs-analysis-report_tool.git)
```
git clone https://github.com/selenewaide/udacity-project3-logs-analysis-report_tool.git
```

###### Step 2 - For Udacity Review
Set up the PostgreSQL database and support software on a virtual machine.
Ensure the 'news' database contains the required tables and data.

###### Step 3 - For Udacity Review
On the command line, run the python script 'questions_all.py' to generate all three reports.
```
python3 questions_all.py
```

Each report can be generated individually by running the question file directly. For example, to generate the report for the first question, run 'question_1.py'
```
python3 question_1.py
```

## 2. Issues

* There is limited error handling.
* There are no automated tests for this code.

## 3. Author

Selene Waide

## 4. Acknowledgments

Udacity Full Stack Nanodegree 

