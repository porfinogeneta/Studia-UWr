% k naturalne i x rzeczywiste dodatnie

x = 21.12;
k = 30;
G = gamma(k / 2);
function_val = @(x) ((x .^ (k / 2 - 1)) .* exp(-x / 2)) ./ ((2 .^ (k / 2)) .* G);

% obliczenie całki, 3 argument to dokładność przybliżania całki
res = countIntegrals(0, x, 17, function_val);
disp(res);