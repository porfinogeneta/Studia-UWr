SELECT
    PM.[Name] AS ProductName,
    COUNT(P.[ProductModelID]) AS NumberOfProducts
FROM
    [AdventureWorksLT2022].[SalesLT].[Product] AS P
INNER JOIN
    [AdventureWorksLT2022].[SalesLT].[ProductModel] AS PM
ON
    PM.[ProductModelID] = P.[ProductModelID]
GROUP BY 
    PM.[Name]
HAVING
    -- zliczamy wszystko
    COUNT(*) > 1
