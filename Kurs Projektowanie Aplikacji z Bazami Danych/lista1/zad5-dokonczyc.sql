SELECT
    H.SalesOrderID,
    H.[SalesOrderNumber],
    H.[PurchaseOrderNumber],
    (SUM (D.[OrderQty] * D.[UnitPrice])) AS OrderWithoutDiscount,
    (SUM (D.[LineTotal])) AS OrderWithDiscount,
    SUM (D.LineTotal) OVER (PARTITION BY D.SalesOrderID) AS TotalOrderWithDiscount
FROM
    [AdventureWorksLT2022].[SalesLT].[SalesOrderDetail] AS D
INNER JOIN
    [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader] AS H
ON D.[SalesOrderID] = H.[SalesOrderID]
GROUP BY
    H.SalesOrderID, D.SalesOrderID, H.SalesOrderNumber, H.PurchaseOrderNumber, D.LineTotal