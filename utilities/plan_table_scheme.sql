DROP TABLE IF EXISTS plans;

CREATE TABLE plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    validity TEXT NOT NULL,
    operator TEXT NOT NULL,
    type TEXT NOT NULL,
    extra TEXT NOT NULL,
    benefits TEXT NOT NULL,
    amount TEXT NOT NULL,
    description TEXT NOT NULL,
    circle_name TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);