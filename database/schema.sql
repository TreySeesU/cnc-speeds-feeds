```sql
PRAGMA foreign_keys = ON;

-- ==========================================================
-- DATABASE VERSION
-- ==========================================================

CREATE TABLE database_info (

    id INTEGER PRIMARY KEY,

    version TEXT NOT NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP

);


-- ==========================================================
-- UNITS
-- ==========================================================

CREATE TABLE units (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE

);


-- ==========================================================
-- MATERIAL CATEGORIES
-- ==========================================================

CREATE TABLE material_categories (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE

);


-- ==========================================================
-- MATERIALS
-- ==========================================================

CREATE TABLE materials (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    category_id INTEGER,

    density REAL,

    hardness TEXT,

    chipload_min REAL,

    chipload_max REAL,

    surface_speed_min REAL,

    surface_speed_max REAL,

    depth_factor REAL,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(category_id)
        REFERENCES material_categories(id)

);


-- ==========================================================
-- TOOL TYPES
-- ==========================================================

CREATE TABLE tool_types (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    description TEXT

);


-- ==========================================================
-- TOOL MANUFACTURERS
-- ==========================================================

CREATE TABLE manufacturers (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    website TEXT,

    notes TEXT

);


-- ==========================================================
-- TOOLS
-- ==========================================================

CREATE TABLE tools (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    part_number TEXT,

    manufacturer_id INTEGER,

    tool_type_id INTEGER NOT NULL,

    diameter REAL NOT NULL,

    diameter_unit_id INTEGER NOT NULL,

    flute_count INTEGER NOT NULL,

    cutting_length REAL,

    overall_length REAL,

    stick_out REAL,

    shank_diameter REAL,

    coating TEXT,

    max_rpm INTEGER,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(manufacturer_id)
        REFERENCES manufacturers(id),

    FOREIGN KEY(tool_type_id)
        REFERENCES tool_types(id),

    FOREIGN KEY(diameter_unit_id)
        REFERENCES units(id)

);


-- ==========================================================
-- MACHINES
-- ==========================================================

CREATE TABLE machines (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    manufacturer TEXT,

    spindle_max_rpm INTEGER NOT NULL,

    horsepower REAL,

    max_feed_rate REAL NOT NULL,

    feed_unit_id INTEGER NOT NULL,

    max_depth REAL,

    notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(feed_unit_id)
        REFERENCES units(id)

);


-- ==========================================================
-- CUT DIRECTIONS
-- ==========================================================

CREATE TABLE cut_directions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE

);


-- ==========================================================
-- TOOL / MATERIAL RECOMMENDATIONS
-- ==========================================================

CREATE TABLE tool_material_settings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    tool_id INTEGER NOT NULL,

    material_id INTEGER NOT NULL,

    chipload_min REAL,

    chipload_max REAL,

    recommended_surface_speed REAL,

    max_depth_factor REAL,

    notes TEXT,


    FOREIGN KEY(tool_id)
        REFERENCES tools(id)
        ON DELETE CASCADE,


    FOREIGN KEY(material_id)
        REFERENCES materials(id)
        ON DELETE CASCADE

);


-- ==========================================================
-- CALCULATION HISTORY
-- ==========================================================

CREATE TABLE calculations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    material_id INTEGER,

    tool_id INTEGER,

    machine_id INTEGER,

    cut_direction_id INTEGER,


    depth_of_cut REAL,

    stepover REAL,

    plunge_rate REAL,


    spindle_rpm INTEGER,

    feed_rate REAL,

    plunge_feed REAL,

    chipload REAL,

    surface_speed REAL,


    unit_system TEXT,


    status TEXT,

    warnings TEXT,


    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,


    FOREIGN KEY(material_id)
        REFERENCES materials(id),


    FOREIGN KEY(tool_id)
        REFERENCES tools(id),


    FOREIGN KEY(machine_id)
        REFERENCES machines(id),


    FOREIGN KEY(cut_direction_id)
        REFERENCES cut_directions(id)

);


-- ==========================================================
-- APPLICATION SETTINGS
-- ==========================================================

CREATE TABLE settings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    setting_name TEXT UNIQUE NOT NULL,

    setting_value TEXT

);


-- ==========================================================
-- INDEXES
-- ==========================================================

CREATE INDEX idx_material_name
ON materials(name);


CREATE INDEX idx_tool_name
ON tools(name);


CREATE INDEX idx_machine_name
ON machines(name);


CREATE INDEX idx_calculation_date
ON calculations(created_at);


CREATE INDEX idx_tool_material
ON tool_material_settings(tool_id, material_id);
```
