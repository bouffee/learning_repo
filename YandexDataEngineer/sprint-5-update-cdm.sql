INSERT INTO cdm.dm_settlement_report(
	restaurant_id, 
	restaurant_name, 
	settlement_date, 
	orders_count, 
	orders_total_sum, 
	orders_bonus_payment_sum,
	orders_bonus_granted_sum, 
	order_processing_fee, 
	restaurant_reward_sum)
SELECT 
	dr.restaurant_id,
	dr.restaurant_name,
	t.date AS settlement_date,
	COUNT(DISTINCT dor.id) AS orders_count,
	sum(fps.total_sum) AS orders_total_sum,
	sum(fps.bonus_payment) AS orders_bonus_payment_sum,
	sum(fps.bonus_grant) AS orders_bonus_granted_sum,
	sum(fps.bonus_payment) * 0.25 AS order_processing_fee,
	(sum(fps.total_sum) - sum(fps.bonus_payment) * 0.25 - sum(fps.bonus_grant)) AS restaurant_reward_sum
FROM dds.dm_restaurants dr
INNER JOIN dds.dm_orders dor ON dor.restaurant_id = dr.id
INNER JOIN dds.fct_product_sales fps ON fps.order_id = dor.id
INNER JOIN dds.dm_timestamps t ON dor.timestamp_id = t.id
WHERE dor.order_status = 'CLOSED'
GROUP BY dr.restaurant_id, t.date, dr.restaurant_name
ON CONFLICT (restaurant_id, settlement_date)
DO UPDATE SET 
	orders_count = excluded.orders_count,
    orders_total_sum = excluded.orders_total_sum,
    order_processing_fee = excluded.order_processing_fee,
    restaurant_reward_sum = excluded.restaurant_reward_sum,
    orders_bonus_payment_sum = excluded.orders_bonus_payment_sum;

SELECT * FROM cdm.dm_settlement_report;