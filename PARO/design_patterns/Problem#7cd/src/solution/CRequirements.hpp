#pragma once

#include "BetterCandidatesValidator.hpp"
#include "../Candidate.hpp"

class CRequirements: public BetterCandidatesValidator
{
public:

    CRequirements (int crequire){cFluency = crequire;}

    bool validate(const Candidate& c) const override
    {
        if(candidate.cFluency < cThreshold)
        {
            return false;
        }
        return true;
    }
private:
    unsigned minCRequirements;
};
