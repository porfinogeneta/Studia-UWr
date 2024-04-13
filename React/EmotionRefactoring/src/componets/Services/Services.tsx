import {ServiceType} from "../../types/CompanyData"
import styled from "@emotion/styled"

const ServicesStyle = styled.ul`
    list-style: none;
    padding: 0;
    margin: 0;

    li {
      margin-bottom: 20px;
      text-align: left;
    }

    h3 {
      font-size: 1.8em;
      margin-bottom: 10px;
    }
`

export default function Services({services}: {services: ServiceType[]}) {
    return (
          <>
            <ServicesStyle>
              {services.map((service) => (
                <li key={service.id}>
                  <h3>{service.name}</h3>
                  <p>{service.description}</p>
                </li>
              ))}
            </ServicesStyle>
          </>
    )
}