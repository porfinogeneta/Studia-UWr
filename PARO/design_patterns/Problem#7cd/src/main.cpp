#include <vector>
#include <iostream>
#include "stdlib.h"

#include "Application.hpp"
#include "Candidate.hpp"

#include "CppRequirements.hpp"
#include "CRequirements.hpp"
#include "CooperationNeeded.hpp"
#include "WageRequirements.hpp"

int main()
{
    std::vector<Candidate> candidates{
        {"Adelajda", 15, 87, 0, 12000},
        {"Brunhilda", 85, 42, 1, 11000},
        {"Ciechosław", 97, 92, 1, 25000},
        {"Domażyr", 91, 45, 0, 10000}};

    auto requirements = std::make_unique<CppRequirements>(20);
    requirements->add(std::make_unique<CRequirements>(0));
    //requirements->add(std::make_unique<CooperationNeeded>(20));
    requirements->add(std::make_unique<WageRequirements>(15000));

    for (auto candidate: getFilteredCandidates(candidates, requirements))
    {
        std::cout << "candidate " << candidate.name << " seems to fit" << std::endl;
    }
}
