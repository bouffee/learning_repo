-- Итак, в хранилище данных два слоя — стейджинг и витрина данных. По аналогии с примером для таблицы d_customer заполните таблицу для d_city и d_calendar. 
-- Описание модели данных есть в файле Data_model_3_sprint.md
-- Для упрощения задания укажите трансформации табличного уровня:  подготовьте запросы для заполнения таблиц d_city и d_calendar. Обратите внимание, что для заполнения 
-- d_calendar нет источника данных. В таблицу d_calendar должны быть загружены все даты с 1 января 2020 года по 1 января 2022 года.

DROP TABLE IF EXISTS stage.d_city;
DROP TABLE IF EXISTS stage.d_calendar;

CREATE TABLE stage.d_city (
	city_id int, 
	city_name varchar(50)
);

INSERT INTO stage.d_city(city_id, city_name) 
SELECT DISTINCT src.city_id, src.city_name
FROM user_order_log AS src;

CREATE TABLE stage.d_calendar(
	date_id serial,
	day_num smallint,
	month_num smallint,
	month_name varchar(9),
	year_num smallint
);

INSERT INTO stage.d_calendar(day_num, month_num, month_name, year_num)
SELECT
	extract(day from date) AS day_num,
	extract(month from date) AS month_num,
	to_char(date, 'Month') AS month_name,
	extract(year from date) AS year_num
FROM generate_series(date '2020-01-01',
	date '2022-01-01',
	interval '1 day')
AS t(date);

SELECT * FROM stage.d_city;
SELECT * FROM stage.d_calendar;