#pragma once
#include "Rectangle.hpp"
#include "FancyRectangle.hpp"
#include "RegularRectangle.hpp"

class FancyToRegular: public Rectangle
{
public: FancyToRegular(fancyToRegular){};
    virtual std::vector<Point> getCorners() const {
        fancyToRegular.width/2
    }
};

