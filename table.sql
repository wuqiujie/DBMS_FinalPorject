CREATE TABLE aircraft(
	aircraft_code VARCHAR PRIMARY KEY NOT NULL,
	company VARCHAR NOT NULL,
	aircraft_type VARCHAR NOT NULL, -- REFERENCES aircraft_performance(aircraft_type)
	departure_airport VARCHAR NOT NULL,
	arrival_airport VARCHAR NOT NULL,
	stopover_airport VARCHAR,
	departure_time timestamp NOT NULL,
	arrival_time timestamp NOT NULL,
	flight_weight INTEGER NOT NULL,
	CONSTRAINT flights_check CHECK ((arrival_time > departure_time))
);

CREATE TABLE airport(
	name VARCHAR PRIMARY KEY NOT NULL,
	aircraft_code VARCHAR NOT NULL, -- REFERENCES aircraft(aircraft_code)
	situation VARCHAR NOT NULL,
	runway INTEGER NOT NULL,
	sequence INTEGER NOT NULL,
	wait_time INTEGER NOT NULL
);

CREATE TABLE environment(
	aircraft_code VARCHAR PRIMARY KEY NOT NULL, -- REFERENCES aircraft(aircraft_code)
	weather VARCHAR NOT NULL,
	landform VARCHAR NOT NULL,
	humidity INTEGER NOT NULL,
	wind_scale INTEGER NOT NULL,
	wind_direction VARCHAR NOT NULL
);

CREATE TABLE aircraft_condition(
	aircraft_code VARCHAR PRIMARY KEY NOT NULL, -- REFERENCES aircraft(aircraft_code)
	coordinates POINT NOT NULL,
	flight_attitude INTEGER NOT NULL,
	flight_direction VARCHAR NOT NULL,
	oil_remaining INTEGER NOT NULL,
	time_flown INTEGER NOT NULL,
	mile_flown INTEGER NOT NULL,
	if_breakdown BOOLEAN NOT NULL,
	if_off_course BOOLEAN NOT NULL,
	if_arrival BOOLEAN NOT NULL,
	if_pass_restricted BOOLEAN NOT NULL
);

CREATE TABLE aircraft_performance(
	aircraft_type VARCHAR PRIMARY KEY NOT NULL,
	max_attitude INTEGER NOT NULL,
	max_fuel_load INTEGER,
	cruise INTEGER NOT NULL,
	climb_rate INTEGER NOT NULL,
	flight_duration INTEGER NOT NULL,
	max_speed INTEGER NOT NULL,
	min_speed INTEGER NOT NULL,
	takeoff_distance INTEGER NOT NULL,
	landing_distance INTEGER NOT NULL,
	safe_disdance INTEGER NOT NULL
	CONSTRAINT speed_check CHECK ((max_speed > min_speed))
);
