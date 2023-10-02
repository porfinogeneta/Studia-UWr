#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

void print_numbers(std::vector<int*> const& x) noexcept
{
    std::cout << x.size() << " elements: [ ";
    std::transform(x.begin(),
                   x.end(),
                   std::ostream_iterator<int>(std::cout, " "),
                   [](int const* item) -> int { return *item; });
    std::cout << "]" << std::endl;
}

std::vector<int*> create_numbers() noexcept
{
    constexpr int count = 32;

    std::vector<int*> numbers(count);
    for (int i = 0; i < count; ++i) { numbers[i] = new int(12 * i); }

    return numbers;
}

void destroy_numbers(std::vector<int*> const& numbers) noexcept {
    for (auto n : numbers) {
        delete n; // usunięcie pojedynczego wskaźnika
    }
}

int main(int argc, char* argv[])
{
    std::vector<int*> nums = create_numbers();

    print_numbers(nums);

    destroy_numbers(nums);

//    HEAP SUMMARY:
//    2: ==83248==     in use at exit: 0 bytes in 0 blocks
//    2: ==83248==   total heap usage: 35 allocs, 35 frees, 77,184 bytes allocated
//    2: ==83248==
//    All heap blocks were freed -- no leaks are possible

    return 0;
}
