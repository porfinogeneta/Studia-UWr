function result = gamma(num)
    if num == 0.5
        result = sqrt(pi);
    elseif num == 1
        result = 1;
    else
        result = (num - 1) * gamma(num - 1);
    end
end
