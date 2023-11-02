-- dodajemy kolumnę
-- ALTER TABLE [AdventureWorksLT2022].[SalesLT].[Customer]
-- ADD [CreditCardNumber] NVARCHAR(19);

-- dodanie zawartości
-- UPDATE [AdventureWorksLT2022].[SalesLT].[Customer]
-- SET [CreditCardNumber] = CONCAT(
--     -- NEWID generuje randomowe id, potem to przerabiane jest na liczbę, doklejane są
--     -- 0000 gdyby liczba była za krótka i bierzemy 4 znaki z nowego string
--     RIGHT('0000' + CAST(ABS(CHECKSUM(NEWID())) % 10000 AS NVARCHAR(5)), 4),
--     ' ',
--     RIGHT('0000' + CAST(ABS(CHECKSUM(NEWID())) % 10000 AS NVARCHAR(5)), 4),
--     ' ',
--     RIGHT('0000' + CAST(ABS(CHECKSUM(NEWID())) % 10000 AS NVARCHAR(5)), 4),
--     ' ',
--     RIGHT('0000' + CAST(ABS(CHECKSUM(NEWID())) % 10000 AS NVARCHAR(5)), 4)
-- );
-- podgląd
-- SELECT *
-- FROM [AdventureWorksLT2022].[SalesLT].[Customer]

-- zmiana stanu akceptacji karty
-- UPDATE [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader]
-- SET [CreditCardApprovalCode] = 1
-- WHERE [CustomerID] IN (30113, 30102, 30089);

-- podgląd
-- SELECT *
-- FROM [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader]

--podmiana wartości na 'X'
UPDATE C
SET C.[CreditCardNumber] = 'X'
FROM [AdventureWorksLT2022].[SalesLT].[Customer] AS C
JOIN [AdventureWorksLT2022].[SalesLT].[SalesOrderHeader] AS H
ON C.[CustomerID] = H.[CustomerID]
WHERE H.[CreditCardApprovalCode] = 1

SELECT *
FROM [AdventureWorksLT2022].[SalesLT].[Customer]


