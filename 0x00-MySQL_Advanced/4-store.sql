-- Script to create triggers
-- Update table when a new order is added
delimiter //
CREATE TRIGGER update_inventory
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = items.quantity - 1
WHERE name = NEW.item_name;