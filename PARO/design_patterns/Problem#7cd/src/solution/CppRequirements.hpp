#pragma once

#include "BetterCandidatesValidator.hpp"
#include "../Candidate.hpp"

class CppRequirements: public BetterCandidatesValidator
{
public:
    bool validate(const Candidate& c) const override
    {
        if(candidate.cFluency < cThreshold)
        {
            return false;
        }
        return true;
    }
private:
    unsigned minCppRequirements;
};
