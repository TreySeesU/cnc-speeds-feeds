PRAGMA foreign_keys = ON;

-- ==========================================================
-- MATERIALS
-- ==========================================================

CREATE TABLE materials (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    density REAL,

    hardness TEXT,

    chipload_min REAL,

    chipload_max REAL,

    surface_speed REAL,

    depth_factor REAL,

    notes TEXT

);

-- ==========================================================
-- TOOL TYPES
-- ==========================================================

CREATE TABLE tool_types (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE

);

-- ==========================================================
-- TOOLS
-- ==========================================================

CREATE TABLE tools (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    diameter REAL NOT NULL,

    tool_type_id INTEGER NOT NULL,

    flutes INTEGER NOT NULL,

    coating TEXT,

    manufacturer TEXT,

    max_rpm INTEGER,

    description TEXT,

    FOREIGN KEY(tool_type_id)
        REFERENCES tool_types(id)
        ON DELETE CASCADE

);

-- ==========================================================
-- MACHINES
-- ==========================================================

CREATE TABLE machines (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE,

    spindle_max_rpm INTEGER NOT NULL,

    max_feed_rate REAL NOT NULL,

    max_depth REAL,

    notes TEXT

);

-- ==========================================================
-- CUT DIRECTIONS
-- ==========================================================

CREATE TABLE cut_directions (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL UNIQUE

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

    spindle_rpm INTEGER,

    feed_rate REAL,

    chipload REAL,

    surface_speed REAL,

    pass_depth REAL,

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
-- OPTIONAL TOOL LIBRARY
-- ==========================================================

CREATE TABLE tool_library (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    tool_id INTEGER,

    recommended_material INTEGER,

    chipload_min REAL,

    chipload_max REAL,

    recommended_rpm INTEGER,

    notes TEXT,

    FOREIGN KEY(tool_id)
        REFERENCES tools(id),

    FOREIGN KEY(recommended_material)
        REFERENCES materials(id)

);

-- ==========================================================
-- USER SETTINGS
-- ==========================================================

CREATE TABLE settings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    setting_name TEXT UNIQUE,

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

CREATE INDEX idx_history_date
ON calculations(created_at);

CREATE INDEX idx_history_material
ON calculations(material_id);

CREATE INDEX idx_history_tool
ON calculations(tool_id);
