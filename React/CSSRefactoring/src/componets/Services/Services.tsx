import {ServiceType} from "../../types/CompanyData"
import "./styles.module.scss"

export default function Services({services}: {services: ServiceType[]}) {
    return (
          <>
            <ul>
              {services.map((service) => (
                <li key={service.id}>
                  <h3>{service.name}</h3>
                  <p>{service.description}</p>
                </li>
              ))}
            </ul>
          </>
    )
}