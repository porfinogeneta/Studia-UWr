-- żeby przykład działał trzeba zrestartować połączenie do serwera w jednym i drugim pliku!!!

SELECT *
FROM brands
WITH (NOLOCK) -- uruchamiamy (NOLOCK), czyli pozwalamy na czytanie nie zacommitowanych danych
-- rzeczywiście udało się odczytać nie zacommitowane dane

-- SELECT *
-- FROM brands
-- mamy nieskończoną kwerendę, nie możemy nic odczytać bo przez isolation level jest założona blokada na tabelce