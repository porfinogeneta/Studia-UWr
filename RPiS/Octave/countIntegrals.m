function result = countIntegrals(a, b, M, f)
    K = 20 - M;
    T = zeros(1, 21);

    for i = 1:21
        hk = (b - a) / (2 ^ (i-1));
        T(i) = hk * sumbis(a, b, hk, f);
    end

    if M == 0
        result = T(K + 1);
        return;
    end

    for m = 1:20
        for k = (20 - m):-1:1
            T(k+1) = (4^m * T(k+1) - T(k)) / (4^m - 1);
            if m == M && k == K
                result = T(m + 1);
                return;
            end
        end
    end

    result = T(M + 1);
end