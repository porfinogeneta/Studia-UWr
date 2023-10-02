#include <resources/kernel_resource.h>

#include <iostream>
#include <vector>

#include <memory> // std::unique_ptr

using Event = int;



std::unique_ptr<Event> create_event(int event_id) noexcept {
    return std::make_unique<Event>(event_id);
}

void resource_deleter(RESOURCE* res) {
    free_resource(res);
}

void process_init(RESOURCE* resource) noexcept
try {
    if (resource) {
        use_resource(resource);
        free_resource(resource);
    }
} catch (std::runtime_error const& ex) {
    std::cout << ex.what() << std::endl;
}

void process_event(std::unique_ptr<Event> event,
                   std::unique_ptr<RESOURCE, decltype(&resource_deleter)> temp_resource,
                   std::unique_ptr<RESOURCE, decltype(&resource_deleter)> &proc_resource) noexcept
try {
    std::cout << "Processing Event(" << event << ")" << std::endl;

    if (temp_resource) {
        use_resource(temp_resource.get());
    }

    if (proc_resource) {
        use_resource(proc_resource.get());
    }

} catch (std::runtime_error const& ex) {
    std::cout << ex.what() << std::endl;
}

int main(int ac, char* av[])
{
    {
        auto init_resource = std::unique_ptr<RESOURCE, decltype(&resource_deleter)>(allocate_resource(), resource_deleter);
        process_init(init_resource.get());
    }

    auto proc_resource = std::unique_ptr<RESOURCE, decltype(&resource_deleter)>(allocate_resource(), resource_deleter);

    std::vector<int> simulation = {
            12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144};
    for (auto id : simulation) {
        auto event = create_event(id);
        auto temp_resource = std::unique_ptr<RESOURCE, decltype(&resource_deleter)>(allocate_resource(), resource_deleter);
        process_event(std::move(event), std::move(temp_resource), proc_resource);
    }

    return 0;
}