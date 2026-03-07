SELECT 
    cashier, 
    created_at as receipt_date,
    name as product_name, 
    price_per_kilo, 
    amount
FROM product_receipt pre
JOIN product pr
ON pr.id = pre.product_id
JOIN receipt re
ON re.id = pre.receipt_id 
WHERE cashier = 'Vincent'
ORDER BY receipt_date desc;