# Back End API Project

## Background Context

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.

### 0-gather_data_from_an_API.py

A Python script that gathers data from a REST API to show the progress of an employee's TODO list.

### 1-export_to_CSV.py

Using what you did in the task #0, extend your Python script to export data in the CSV format.

### 2-export_to_JSON.py

Using what you did in the task #0, extend your Python script to export data in the JSON format.

### 3-dictionary_of_list_of_dictionaries.py

Using what you did in the task #0, extend your Python script to export data in the JSON format.

## Usage

To use the scripts, clone the repository and run the scripts as follows:

Example:

```bash
python3 0-gather_data_from_an_API.py <employee_id>
