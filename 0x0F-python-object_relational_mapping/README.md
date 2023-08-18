# Python Object-Relational Mapping

## Project Description

This repository contains my solutions and implementations for the ALX Higher Level Programming Python Object-Relational Mapping (ORM) tasks. The tasks focus on utilizing Python and SQLAlchemy to interact with databases, perform CRUD (Create, Read, Update, Delete) operations, and establish relationships between tables.

The tasks cover a range of topics, including querying databases, creating data models, managing relationships between tables, implementing ORM concepts, and ensuring data integrity.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Task Descriptions](#task-descriptions)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Installation

To run and test the scripts in this repository, you'll need to have Python and the necessary dependencies installed. You can set up the environment using the following steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Dr-dyrane/alx-higher_level_programming/0X0F-Python-object-relational-mapping.git
   cd 0X0F-Python-object-relational-mapping
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Each task is organized into separate script files. You can run the scripts using the following commands:

```bash
python script_name.py
```

Replace `script_name.py` with the actual name of the script you want to run. Make sure to provide any required command-line arguments, as specified in the task descriptions.

## Task Descriptions

Here's a brief overview of the tasks covered in this repository:

| Task ID | Description | Script File |
|---------|-------------|-------------|
| Task 0  | Lists all states from the database `hbtn_0e_0_usa`. | 0-select_states.py |
| Task 1  | Lists all states with a `name` starting with the letter `N` from the database `hbtn_0e_0_usa`. | 1-filter_states.py |
| Task 2  | Displays all values in the states where `name` matches the argument from the database `hbtn_0e_0_usa`. | 2-my_filter_states.py |
| Task 3  | Displays all values in the states where `name` matches the argument from the database `hbtn_0e_0_usa`. This time the script is safe from MySQL injections! | 3-my_safe_filter_states.py |
| Task 4  | Lists all cities from the database `hbtn_0e_4_usa`. | 4-cities_by_state.py |
| Task 5  | Lists all City objects from the database `hbtn_0e_4_usa`. | 5-filter_cities.py |
| Task 6  | Defines a State class and a Base class to work with MySQLAlchemy ORM. | 6-model_state.py |
| Task 7  | Lists all State objects from the database `hbtn_0e_6_usa`. | 7-model_state_fetch_all.py |
| Task 8  | Prints the first State object from the database `hbtn_0e_6_usa`. | 8-model_state_fetch_first.py |
| Task 9  | Lists all State objects that contain the letter `a` from the database `hbtn_0e_6_usa`. | 9-model_state_filter_a.py |
| Task 10 | Lists a State object from the database `hbtn_0e_6_usa` using its `id`. | 10-model_state_my_get.py |
| Task 11 | Inserts a new State object into the database `hbtn_0e_6_usa`. | 11-model_state_insert.py |
| Task 12 | Updates a State object's name in the database `hbtn_0e_6_usa`. | 12-model_state_update_id_2.py |
| Task 13 | Deletes a State object from the database `hbtn_0e_6_usa`. | 13-model_state_delete_a.py |
| Task 14 | Prints all City objects from the database `hbtn_0e_14_usa`. | 14-model_city_fetch_by_state.py |
| Task 15| Adds a State object `California` and a City object `San Francisco` to the database `hbtn_0e_6_usa`. | 100-relationship_states_cities.py |
| Task 16| Lists all State objects and corresponding City objects contained in the DB. | 101-relationship_states_cities_list.py |
| Task 17| Lists all City objects from the database `hbtn_0e_101_usa`. | 102-relationship_cities_states_list.py |


For detailed explanations and requirements for each task, please refer to the individual script files and their respective comments.

## Files

This section provides a list of the files included in this repository:

| File Name |
|-----------|
| [0-select_states.py](0-select_states.py) |
| [1-filter_states.py](1-filter_states.py) |
| [2-my_filter_states.py](2-my_filter_states.py) |
| [3-my_safe_filter_states.py](3-my_safe_filter_states.py) |
| [4-cities_by_state.py](4-cities_by_state.py) |
| [5-filter_cities.py](5-filter_cities.py) |
| [6-model_state.py](6-model_state.py) |
| [7-model_state_fetch_all.py](7-model_state_fetch_all.py) |
| [8-model_state_fetch_first.py](8-model_state_fetch_first.py) |
| [9-model_state_filter_a.py](9-model_state_filter_a.py) |
| [10-model_state_my_get.py](10-model_state_my_get.py) |
| [11-model_state_insert.py](11-model_state_insert.py) |
| [12-model_state_update_id_2.py](12-model_state_update_id_2.py) |
| [13-model_state_delete_a.py](13-model_state_delete_a.py) |
| [14-model_city_fetch_by_state.py](14-model_city_fetch_by_state.py) |
| [100-relationship_states_cities.py](100-relationship_states_cities.py) |
| [101-relationship_states_cities_list.py](101-relationship_states_cities_list.py) |
| [102-relationship_cities_states_list.py](102-relationship_cities_states_list.py) |
| [model_city.py](model_city.py) |
| [model_state.py](model_state.py) |
| [relationship_city.py](relationship_city.py) |
| [relationship_state.py](relationship_state.py) |
| [README.md](README.md) |

## Contributing

Contributions to this repository are welcome. If you find any issues, want to add improvements, or have suggestions for new features, feel free to open a pull request. Please make sure to follow the code style guidelines and provide clear descriptions for your contributions.

## License

This project is licensed under the [MIT License](LICENSE).

## Author
Author: [Alexander Udeogaranya](https://github.com/Dr-dyrane/alx-higher_level_programming/0X0F-Python-object-relational-mapping)
