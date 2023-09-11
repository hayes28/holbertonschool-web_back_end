# Pagination Project

## Resources

**Read or watch:**
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)

## Setup: Popular_Baby_Names.csv

[Use this data file](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230912%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230912T034110Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=55b2874b4592c8a16f75d19fb91d0cafae54213b78dbc1cf2e4af98f1fa554a7) for your project.

## Tasks

### 0. Simple helper function

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

- File: `0-simple_helper_function.py`

### 1. Simple pagination

Copy `index_range` from the previous task and implement a method named `get_page`.

- File: `1-simple_pagination.py`

### 2. Hypermedia pagination

Replicate code from the previous task and implement a `get_hyper` method.

- File: `2-hypermedia_pagination.py`

### 3. Deletion-resilient hypermedia pagination

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from the dataset when changing the page.

- File: `3-hypermedia_del_pagination.py`

## How to Install

Clone the repository:
```bash
git clone https://github.com/your_username/your_repository.git
