-- Write SQL script that ranks country origins of bands
-- Ordered by the number of (non-unique) fans
-- Column must be origin and nb_fans
-- Script can be executed on any database

SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;
