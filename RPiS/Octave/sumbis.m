function res = sumbis(a, b, h, f)
    res = 0.5 * (f(a) + f(b));
    node = a + h;
    while node < b
        res += f(node);
        node += h;
    endwhile
endfunction