# 📋 Python Todo & Log Management CLI

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pickle](https://img.shields.io/badge/Serialization-Pickle-orange?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-CLI-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A robust command-line interface (CLI) application built in Python for managing time-sensitive tasks, tracking records, and filtering expiring entries. Designed with clean modular functions, persistent binary storage, and defensive user input validation.

---

## ✨ Features

- **Persistent Storage:** Automatically serializes and deserializes task records using Python's built-in `pickle` module.
- **Interactive Menu:** Intuitive terminal navigation loop supporting viewing, adding, removing, clearing, and exporting tasks.
- **Defensive Input Handling:** Built-in loops and exception handling (`try-except`, type checking, and date parsing with `datetime`) to gracefully handle invalid user inputs.
- **Expiration Tracking:** Filters and flags tasks that exceed a customizable threshold (default: 10 days) relative to the current date.
- **Structured Logging Model:** Relies on a dedicated `Log` data model to encapsulate dates, titles, and descriptions.

---

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.12+
- **Standard Libraries:** `os`, `pickle`, `datetime`
- **Architecture:** Procedural CLI control flow with modular separation of concerns (`load`, `save`, `add`, `remove`, `view`).

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.12+** installed on your workstation.

### Installation & Execution

1. Clone the repository:
   ```bash
   git clone [https://github.com/burloi-ship-it/python-todo-cli.git](https://github.com/burloi-ship-it/python-todo-cli.git)
   cd python-todo-cli