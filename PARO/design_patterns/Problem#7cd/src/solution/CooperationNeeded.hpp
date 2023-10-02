#pragma once

#include "BetterCandidatesValidator.hpp"
#include "../Candidate.hpp"

class CooperationNeeded: public BetterCandidatesValidator
{
public:
    bool validate(const Candidate& c) const override
    {
        if(not candidate.cooperative)
        {
            return false;
        }

        return true;
    }
};
