UPDATE [AdventureWorksLT2022].[SalesLT].[Product]
SET
   [ProductCategoryID] = 1
WHERE [ProductID] = 772;

-- połączenie tabel samych z sobą może być użyteczne
SELECT 
    C.[Name] AS CategoryName,
    P.[Name] AS ProductName
FROM [AdventureWorksLT2022].[SalesLT].[Product] AS P
INNER JOIN [AdventureWorksLT2022].[SalesLT].[ProductCategory] AS C1
INNER JOIN [AdventureWorksLT2022].[SalesLT].[ProductCategory] AS C2
ON P.[ProductCategoryID] = C.[ProductCategoryID]
WHERE C.[ParentProductCategoryID] IS NULL
