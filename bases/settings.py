DB_HOST = "61.70.21.140"
DB_USER = "web104"
DB_PASSWORD = "cnap*74182"
DB_DATABASE = "PCM"
DB_PORT = 3307

SLEEP_TIME = 30  # Seconds

CREATE_TABLE_SQL = """create table if not exists demo (
	data_date VARCHAR(8) NULL DEFAULT NULL,
	data_time VARCHAR(8) NULL DEFAULT NULL,
	sen1 FLOAT NULL DEFAULT NULL,
	sen2 FLOAT NULL DEFAULT NULL,
	sen3 FLOAT NULL DEFAULT NULL,
	sen4 FLOAT NULL DEFAULT NULL,
	sen5 FLOAT NULL DEFAULT NULL,
	sen6 FLOAT NULL DEFAULT NULL,
	set1 FLOAT NULL DEFAULT NULL,
	set2 FLOAT NULL DEFAULT NULL,
	set3 FLOAT NULL DEFAULT NULL,
	set4 FLOAT NULL DEFAULT NULL,
	set5 FLOAT NULL DEFAULT NULL,
	set6 FLOAT NULL DEFAULT NULL,
	set7 FLOAT NULL DEFAULT NULL
);
"""