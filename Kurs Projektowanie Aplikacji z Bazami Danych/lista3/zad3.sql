-- update Prices table based on Rates table
-- Prices references to a non-existing row in Rates, remove this row

-- to delete currency from currency table
-- use alter table and diable constraint to get rid of errors00


-- create a temporary table of prices only in PLN
set nocount on -- disable row affected message
DROP TABLE IF EXISTS #PLN_price

-- prices only in PLN
CREATE TABLE #PLN_price (
    ProductID INT,
    Price DECIMAL(10,2)
)

DROP TABLE IF EXISTS #possible_currency

-- table with all possibles currencies
CREATE TABLE #possible_currency (
    Currency VARCHAR(3)
)

-- rates cursor
DECLARE c_rates CURSOR DYNAMIC FOR SELECT Currency, PricePLN FROM Rates

-- vairables for cursor c_rates
DECLARE @currency_rate VARCHAR(3); -- name of curreny
DECLARE @price_pln INT; -- price of currency in PLN

-- prepare a table with all possible currencies
OPEN c_rates;
    FETCH NEXT FROM c_rates INTO @currency_rate, @price_pln;
    WHILE (@@FETCH_STATUS = 0)
        BEGIN
            INSERT INTO #possible_currency (Currency)
            VALUES (@currency_rate)
            FETCH NEXT FROM c_rates INTO @currency_rate, @price_pln;
        END
        CLOSE c_rates  
    
-- prices cursor
DECLARE c_prices CURSOR DYNAMIC FOR SELECT ProductID, Currency, Price 
FROM Prices

-- variables for cursor c_prices
DECLARE @product_id INT;
DECLARE @currency VARCHAR(3);
DECLARE @price DECIMAL(10, 2);

-- prepare table with all prices in PLN
OPEN c_prices
FETCH NEXT FROM c_prices INTO @product_id, @currency, @price
WHILE (@@FETCH_STATUS = 0)
BEGIN
    IF @currency = 'PLN'
    BEGIN
        INSERT INTO #PLN_price (ProductID, Price)
        VALUES (@product_id, @price)
    END
    
    FETCH NEXT FROM c_prices INTO @product_id, @currency, @price
END
CLOSE c_prices


-- dynamic Cursor so it sees changes in Prices table
-- sort values in Prices table before adding them to cursor so they are displayed
-- in ascending order, regarding IDs, and PLN price is displayed on top in each ID group
-- order by changes a cursor to be read only
-- DECLARE c_prices CURSOR DYNAMIC FOR SELECT ProductID, Currency, Price 
-- FROM Prices
-- ORDER BY ProductID ASC,
-- CASE
--     WHEN Currency = 'PLN' THEN 1
--     ELSE 2
-- END,
-- Currency ASC
-- FOR UPDATE OF ProductID, Currency, Price;




OPEN c_prices

-- helper variables
DECLARE @current_pln_price DECIMAL(10, 2);
DECLARE @new_price DECIMAL(10, 2);


FETCH NEXT FROM c_prices INTO @product_id, @currency, @price
WHILE (@@FETCH_STATUS=0)
    BEGIN
        IF @currency <> 'PLN'
        BEGIN
            -- there is not such Currency like the one selected in Rates, delete row which doesn't fit
            DELETE FROM Prices
            WHERE @currency NOT IN (SELECT Currency FROM #possible_currency)
            
            -- get current price in PLN
            SELECT @current_pln_price = Price FROM #PLN_price WHERE ProductID = @product_id;
            -- get currency rate from rates table
            OPEN c_rates;
            FETCH NEXT FROM c_rates INTO @currency_rate, @price_pln;
            WHILE (@@FETCH_STATUS = 0)
                BEGIN
                    -- we found a currency that we want to change
                    IF @currency_rate = @currency
                    BEGIN
                        SET @new_price = @current_pln_price / @price_pln -- count appropriate price
                        UPDATE Prices
                        SET Price=@new_price
                        WHERE CURRENT OF c_prices
                    END
                    FETCH NEXT FROM c_rates INTO @currency_rate, @price_pln;
                END
                CLOSE c_rates  
        END
        FETCH NEXT FROM c_prices INTO @product_id, @currency, @price;
    END

CLOSE c_prices
DEALLOCATE c_prices

DEALLOCATE c_rates

SELECT * FROM Prices