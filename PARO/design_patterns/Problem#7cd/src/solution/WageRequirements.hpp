#pragma once

#include "BetterCandidatesValidator.hpp"
#include "../Candidate.hpp"

class WageRequirements: public BetterCandidatesValidator
{
public:

    WageRequirements (int wage){maxPreferredWage = wage;}

    bool validate(const Candidate& c) const override
    {
        if(candidate.preferredWage > wageThreshold)
        {
            return false;
        }
        return true;
    }
private:
    unsigned maxPreferredWage;
};
