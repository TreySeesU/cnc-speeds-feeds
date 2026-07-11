# CNC Speeds & Feeds Manager
Speeds and Feeds for CNC Machines
**Version:** 1.0.0 (Development)

An open-source CNC Router Speeds & Feeds Management System written in **Python**, **PHP**, and **SQLite**.

This application is designed for CNC router operators, hobbyists, educators, and professional shops who want a centralized database of materials, tooling, machines, and cutting parameters while automatically calculating safe and efficient spindle speeds and feed rates.

---

## Features

* Material Database
* Tool Database
* Machine Database
* Automatic Speed & Feed Calculator
* Chip Load Calculator
* Surface Speed Calculator
* Recommended Pass Depth Calculator
* Material-Specific Recommendations
* Tool Library Management
* Calculation History
* Metric and Imperial Unit Support
* Responsive Web Interface
* SQLite Database
* Python Calculation Engine
* PHP Web Interface
* CSV Import / Export (planned)
* Database Backup / Restore (planned)

---

## Project Goals

The goal of this project is to create a free, open-source alternative to commercial speeds and feeds management software while remaining simple enough for hobby CNC users.

The calculation engine is designed to be modular so that future versions can include advanced machining features such as:

* Adaptive Clearing
* Dynamic Chip Thinning
* Tool Deflection Calculations
* Horsepower Estimation
* Spindle Load Estimation
* Manufacturer Tool Libraries
* Material Libraries
* G-Code Verification

---

## Technology Stack

Backend

* Python 3.12
* PHP 8.3
* SQLite 3
* Apache (LAMP)

Frontend

* HTML5
* CSS3
* JavaScript (Vanilla)

Operating System

* Linux

---

## Project Structure

```text
cnc-speeds-feeds/

README.md
LICENSE
.gitignore

database/
    schema.sql
    initialize_database.py
    cnc.db

python/
    calculator.py
    formulas.py
    database.py
    units.py
    validators.py
    warnings.py
    config.py

api/
    calculate.php
    materials.php
    tools.php
    machines.php
    history.php
    settings.php
    db.php

web/
    index.php

    materials.php
    material_edit.php

    tools.php
    tool_edit.php

    machines.php
    machine_edit.php

    settings.php

    history.php

    css/
        style.css

    js/
        app.js

uploads/

logs/
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/TreySeesU/cnc-speeds-feeds.git
```

Enter the project directory.

```bash
cd cnc-speeds-feeds
```

Create the SQLite database.

```bash
python3 database/initialize_database.py
```

Configure Apache so the `web/` directory is the document root or is served as part of your existing virtual host.

---

## Current Development Status

The project is under active development.

Current version:

**v1.0.0-dev**

---

## Planned Versions

### Version 1.0

* Material Database
* Tool Database
* Machine Database
* Speed Calculator
* Feed Calculator
* Unit Conversion
* History

### Version 1.1

* CSV Import
* CSV Export
* Database Backup
* Tool Manufacturers

### Version 1.2

* Material Database Import
* Tool Library Import
* Search Improvements

### Version 2.0

* Adaptive Clearing
* Radial Chip Thinning
* Tool Wear Tracking
* REST API

---

## License

This project is released under the MIT License.

See the LICENSE file for details.

---

## Contributing

Pull requests, feature requests, and bug reports are welcome.

Please open an issue before submitting major feature changes.

---

## Author

Project maintained by TreySeesU.

Built with Python, PHP, SQLite, and Apache for Linux.
