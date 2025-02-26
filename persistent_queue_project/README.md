# Persistent Queue Project

## Overview

Welcome to the Persistent Queue Project! This system is designed to handle tasks efficiently and reliably, even if something goes wrong. Think of it as a smart to-do list that ensures every task gets done, no matter what.

## What You Need

- A computer with internet access.
- Basic knowledge of using the command line (don't worry, we'll guide you!).

## Setting Up the Project

### Step 1: Open Your Terminal

First, open your terminal or command prompt. This is where you'll type all the commands to get the project up and running.

### Step 2: Navigate to the Project Folder

Type the following command to go to the project folder:

```bash
cd ~/bootcamp-srinivas/persistent_queue_project
```

### Step 3: Install Dependencies

Next, you'll need to install some tools and libraries that the project depends on. Run these commands one by one:

```bash
pip install --user poetry
poetry install --with dev
poetry env activate
```

**Note:** The `poetry env activate` command activates a virtual environment, which is like a safe space for the project to run without affecting other parts of your computer.

### Step 4: Create Necessary Folders

The project needs some folders to store data and logs. Run this command to create them:

```bash
mkdir -p data/files logs && chmod 777 data/files logs
```

## Running the Application

### Starting the Workers

The workers are the ones who process the tasks. Start them by running:

```bash
poetry run supervisord -c supervisord.conf
```

### Launching the Manager UI

The Manager UI lets you control and manage the tasks. Start it with:

```bash
poetry run python -m streamlit run src/ui/manager.py
```

- **Access the Manager UI**: Open your web browser and go to [http://localhost:8501](http://localhost:8501).
- **Login Credentials**: Use `admin123` as the password.

### Launching the Operations (Ops) UI

The Ops UI allows you to monitor the progress of the tasks. Start it with:

```bash
poetry run python -m streamlit run src/ui/ops.py
```

- **Access the Ops UI**: Open your web browser and go to [http://localhost:8502](http://localhost:8502).

## How It Works

Here’s a simple explanation of how everything fits together:

```
+----------------+       +----------------+       +----------------+
|   Producer     | ----> | Persistent     | <---- |   Consumers    |
| (Creates Jobs) |       | Queue (SQLite) |       | (Processes Jobs)|
+----------------+       +----------------+       +----------------+
                           |         |
                           v         v
+----------------+       +----------------+
|   Manager UI   | <---- |    Ops UI      |
| (Control Jobs) |       | (Monitor Jobs) |
+----------------+       +----------------+
```

- **Producer**: This is where tasks (like files) are added to the queue.
- **Queue**: This is a storage area (using SQLite) that keeps track of all the tasks.
- **Consumers**: These are the workers that process the tasks from the queue.
- **Manager UI**: This is your control panel where you can manage and control the tasks.
- **Ops UI**: This is your monitoring panel where you can see how the tasks are progressing.

## Stopping the Application

To stop the application, simply press `Ctrl + C` in the terminal where each service is running.

## Troubleshooting

### Nothing Happens?

If nothing seems to be working, check the logs in the `logs/` directory. For example, you can look at `logs/producer.log` to see if there are any errors.

### Cannot Log In?

Make sure you are using the correct password: `admin123`.

### Still Facing Issues?

Run the following command to check if everything is set up correctly:

```bash
poetry run pytest tests/ -v
```


## Frequently Asked Questions (FAQ)

### 1. **What happens if a consumer crashes while processing a job?**
The system uses a heartbeat mechanism to detect stalled jobs. If a consumer crashes, the job is reset to `PENDING` status after 5 minutes, allowing another consumer to pick it up.  

---

### 2. **How does the system handle jobs that repeatedly crash consumers?**
Jobs that cause repeated crashes are retried up to 3 times. After the third failure, the job is marked as `UNPROCESSABLE` and excluded from further processing.  

---

### 3. **Can I swap out the SQLite backend for another database?**
Yes! The system uses a factory pattern (`get_queue()`) to abstract the backend implementation. You can replace SQLite with another database (e.g., Redis) by modifying only the `get_queue()` function.  

---

### 4. **How do I monitor the status of jobs?**
The Ops UI provides real-time monitoring of job statuses. Access it at [http://localhost:8502](http://localhost:8502).  

---

### 5. **What happens if the system crashes entirely?**
All jobs are stored persistently in the SQLite database. When the system restarts, it resumes processing from where it left off.  

---

### 6. **How do I increase the number of workers?**
You can scale the system by adding more workers. Update the `supervisord.conf` file to include additional worker configurations.  

---

### 7. **Where are the logs stored?**
Logs are stored in the `logs/` directory. You can check `logs/producer.log` and `logs/consumer.log` for detailed information.  

---

### 8. **How do I change the admin password for the Manager UI?**
The default password is `admin123`. To change it, modify the relevant configuration file in the project.  

---


