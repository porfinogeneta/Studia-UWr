SELECT
    A.City AS CityName,
    COUNT(DISTINCT CA.CustomerID) AS NumberOfCustomers,
    COUNT(DISTINCT C.SalesPerson) AS NumberOfSalesPeople
FROM
    [AdventureWorksLT2022].[SalesLT].[Address] AS A
INNER JOIN
    [AdventureWorksLT2022].[SalesLT].[CustomerAddress] AS CA
    ON A.AddressID = CA.AddressID
INNER JOIN
    [AdventureWorksLT2022].[SalesLT].[Customer] AS C
    ON CA.CustomerID = C.CustomerID
GROUP BY
    A.City
