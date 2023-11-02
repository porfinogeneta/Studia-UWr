SELECT
   C.LastName AS LastName,
   C.FirstName AS FirstName,
   SUM(PD.UnitPriceDiscount * PD.OrderQty) AS SavedMoney
FROM
    [AdventureWorksLT2022].[SalesLT].[Customer] AS C
INNER JOIN
    [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader] AS SI
    ON SI.CustomerID = C.CustomerID
INNER JOIN
    [AdventureWorksLT2022].[SalesLT].[SalesOrderDetail] AS PD
    ON SI.SalesOrderID = PD.SalesOrderID
GROUP BY
    C.FirstName, C.LastName