# MySQL Advanced

## Table of Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [More Info](#more-info)
6. [Tasks](#tasks)
7. [Author](#author)

## Introduction

This project is about learning advanced MySQL concepts.

## Resources

- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info

### Comments for your SQL file

```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Use “container-on-demand” to run MySQL

- Ask for container Ubuntu 18.04 - Python 3.7
- Connect via SSH
- Or via the WebTerminal
- In the container, you should start MySQL before playing with it:

```bash
$ service mysql start
 * MySQL Community Server 5.7.30 is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password:
Database
information_schema
mysql
performance_schema
sys
$
```

#### In the container, credentials are root/root

### How to import a SQL dump

```bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

## Tasks

### 0. We are all unique

- Create a table `users` with attributes `id`, `email`, and `name`.
- `id` should be an integer, never null, auto-increment, and the primary key.
- `email` should be a string of 255 characters, never null, and unique.
- `name` should be a string of 255 characters.

[File: 0-uniq_users.sql](./0-uniq_users.sql)

### 1. In and not out

- Similar to the first task but add a `country` attribute.
- `country` should be an enumeration of countries: US, CO, and TN, never null.

[File: 1-country_users.sql](./1-country_users.sql)

### 2. Best band ever

- Import the table dump `metal_bands.sql.zip`.
- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.

[File: 2-fans.sql](./2-fans.sql)

### 3. Old school band

- Import the table dump `metal_bands.sql.zip`.
- List all bands with Glam rock as their main style, ranked by their longevity.

[File: 3-glam_rock.sql](./3-glam_rock.sql)

### 4. Buy buy buy

- Create a trigger that decreases the quantity of an item after adding a new order.

[File: 4-store.sql](./4-store.sql)

### 5. Email validation to sent

- Create a trigger that resets the attribute `valid_email` only when the email has been changed.

[File: 5-valid_email.sql](./5-valid_email.sql)

### 6. Add bonus

- Create a stored procedure `AddBonus` that adds a new correction for a student.

[File: 6-bonus.sql](./6-bonus.sql)

### 7. Average score

- Create a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.

[File: 7-average_score.sql](./7-average_score.sql)

### 8. Optimize simple search

- Create an index `idx_name_first` on the table `names` and the first letter of `name`.

[File: 8-index_my_names.sql](./8-index_my_names.sql)

### 9. Optimize search and score

- Create an index `idx_name_first_score` on the table `names` and the first letter of `name` and the `score`.

[File: 9-index_name_score.sql](./9-index_name_score.sql)

### 10. Safe divide

- Create a function `SafeDiv` that divides the first by the second number or returns 0 if the second number is equal to 0.

[File: 10-div.sql](./10-div.sql)

### 11. No table for a meeting

- Create a view `need_meeting` that lists all students that have a score under 80 and no `last_meeting` or more than 1 month.

[File: 11-need_meeting.sql](./11-need_meeting.sql)

## Author

- **Heather Hayes** - [Heather Hayes](https://github.com/hayes28)
- [LinkedIn](www.linkedin.com/in/heather-hayes)
