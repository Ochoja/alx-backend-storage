-- Ranks country origin and bands from metal_band.sql
-- Select distict countries, sums the fans and orders them
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands GROUP BY origin 
ORDER BY nb_fans DESC;