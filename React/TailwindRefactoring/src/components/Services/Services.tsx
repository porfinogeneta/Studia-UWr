import {ServiceType} from "../../types/CompanyData"


export default function Services({services}: {services: ServiceType[]}) {
    return (
          <>
            <ul className="list-none p-0 m-0">
              {services.map((service) => (
                <li key={service.id} className="mb-8">
                    <h3 className="text-xl font-semibold mb-2">{service.name}</h3>
                    <p className="text-lg">{service.description}</p>
                </li>
                ))}
            </ul>
          </>
    )
}