#pragma once
#include <iostream>
#include <chrono>
#include <thread>
#include <string>

#include "Updater.hpp"
#include "GreeterUpdater.hpp"

class LazyUpdater: public Updater{
public:

    void checkForUpdates(){
        GreaterUpdater greaterUpdater;
        greaterUpdater.checkForUpdates();
    }
};
